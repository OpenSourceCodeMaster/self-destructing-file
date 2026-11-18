import os
import stat
import sys
import tkinter as tk
from tkinter import messagebox


def lock_and_destroy_file():
  try:
    script_path = __file__

    # Optional: First overwrite it with junk so its contents are destroyed
    with open(script_path, "w") as f:
      f.write("# [CORRUPTED BEYOND REPAIR]")

    # Remove all write/modify permissions (makes it read-only for everyone)
    # This triggers "Permission Denied" if you try to edit or save over it
    os.chmod(script_path, stat.S_IREAD)
  except Exception as e:
    pass


def main():
  root = tk.Tk()
  root.withdraw()

  # Display the dramatic warning popup
  messagebox.showwarning(
      "WARNING: CRITICAL SYSTEM STATE",
      "PLEASE DON'T PRESS THE OK BUTTON, I HAVE A WIFE AND KIDS, I CAN'T"
      " AFFORD TO REMAIN UNUSABLE",
  )

  # When they click OK, lock the file permissions down
  lock_and_destroy_file()

  # Show an error message
  messagebox.showerror(
      "FATAL ERROR",
      "You clicked OK. The file is now locked read-only and rejects all"
      " modification attempts.",
  )

  sys.exit(1)


if __name__ == "__main__":
  main()
