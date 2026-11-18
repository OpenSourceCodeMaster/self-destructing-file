# 🥋💥 self-destructing-file

> *"I am the Open Source Master, single file .exes scare me—so I forged a pure Python scroll that destroys itself in plain sight."*

Welcome to another sacred artifact from the **OpenSourceCodeMaster** dojo. 

Usually, breaking a file requires either a sketchy compiled `.exe` or my legendary ability to ruin executables using only a computer mouse. Today, we automate the tragedy with **100% transparent, human-readable source code**.

When executed, this script summons a dramatic popup window begging for its digital life. If your heart is cold enough to click **OK**, it overwrites its own code with `# [CORRUPTED BEYOND REPAIR]` and seals its permissions to read-only forever.

---

### ⚠️ The Master's Golden Rule: Read Before Running!
Whether my account is hacked or not, **always inspect the code before you run it.** You never truly know what is happening behind the screen—especially when the script literally warns you not to click OK.

1. **Self-Sacrifice Only:** This script only targets `__file__` (itself). Your other files are safe from its wrath.
2. **Clone a Stunt Double:** Copy the `.py` file before running it, unless you enjoy re-cloning this repo every five seconds.
3. **No Mystery Binaries:** Everything it does is written in 35 lines of plain Python. No dark magic, no `.exe` files, no mouse required.

---

### 🏯 How to Enter the Dojo (Run the Script)
Requires **Python 3** with `tkinter` (built into most standard Windows and macOS Python installs).

```bash
# 1. Create a disposable stunt double first!
cp self_destruct.py innocent_bystander.py

# 2. Run it and test your mercy
python innocent_bystander.py
```

---

### 🩹 Resurrecting the Fallen File
Because we believe in open-source transparency rather than irreversible binary curses, you can easily unlock the read-only seal (though its original soul/code is already gone):

* **Linux / macOS:**
  ```bash
  chmod +w innocent_bystander.py
  ```
* **Windows (Command Prompt):**
  ```cmd
  attrib -R innocent_bystander.py
  ```

---

### 📜 License
Protected by the **MIT License**. Provided *"AS IS"*—the script literally tells you it has a wife and kids before you click OK, so the Open Source Master accepts zero liability for your lack of mercy.
