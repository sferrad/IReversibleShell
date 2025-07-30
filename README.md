# 🌀 IReversibleShell – Educational Reverse Shell in Python

> ⚠️ This project is for **educational and ethical** purposes only.  
> It is designed to demonstrate how reverse shells work in **controlled environments**, such as CTFs or personal labs.

## 📚 Table of Contents

- [Disclaimer](#-disclaimer)
- [What is a Reverse Shell?](#-what-is-a-reverse-shell)
- [Usage (for labs only)](#-usage-for-labs-only)
- [Requirements](#-requirements)
- [How it Works](#-how-it-works)
- [Safety Features](#-safety-features)
- [Author](#-author)

## ❗ Disclaimer

This code is not intended for malicious use. Running this script against machines you do not own or have authorization for is **illegal** and against GitHub's [Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service).

**Use at your own risk and only in legal, ethical contexts.**

---

## 🧠 What is a Reverse Shell?

A reverse shell is a connection initiated by a target machine to an attacker's machine, allowing the attacker to execute commands remotely. This is often used in security research, penetration testing, and CTFs.

---

## 🛠 Usage (for labs only)

1. **Start a listener** on your attacker machine (e.g. using `nc -lvnp 4444`).
2. Edit `reverse_shell.py`:
   ```python
   TARGET_HOST = "127.0.0.1"
   TARGET_PORT = 4444
   ENABLED = True
3. Run the script on the target (lab VM):
```bash
python3 reverse_shell.py
```

## 🧪 Requirements

   - Python 3.x

   - Windows (for PowerShell usage) — can be adapted for Linux
## 🔍 How it Works

This script:

1. Creates a TCP socket and continuously tries to connect to a remote host.
2. Once connected, it waits for shell commands from the attacker machine.
3. Supports `cd` commands to change directories.
4. Executes all other commands via PowerShell (on Windows).
5. Sends the output back to the remote listener.
6. Automatically reconnects if the connection is dropped.

## 🛡 Safety Features

- Execution is disabled by default (`ENABLED = False`)
- IP and port must be manually configured
- Includes a `__name__ == "__main__"` guard to prevent accidental execution when imported
- Legal warning included in the script and this README

## 👤 Author

**sferrad**  
Student at [42_PARIS](https://profile-v3.intra.42.fr/users/sferrad) 

- 📧 sferrad@student.42.fr

- 🔗 [Linkedin](https://www.linkedin.com/in/sabry-ferrad-722ba6354/)
