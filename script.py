import os
import sys
import ctypes
import tkinter as tk

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def disable_button():
    os.system('powercfg -setacvalueindex SCHEME_CURRENT 4f971e89-eebd-4455-a8de-9e59040e7347 7648efa3-dd9c-4e3e-b566-50f929386280 0')
    os.system('powercfg -SetActive SCHEME_CURRENT')

def enable_button():
    os.system('powercfg -setacvalueindex SCHEME_CURRENT 4f971e89-eebd-4455-a8de-9e59040e7347 7648efa3-dd9c-4e3e-b566-50f929386280 1')
    os.system('powercfg -SetActive SCHEME_CURRENT')

if is_admin():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    disable = tk.Button(frame, 
                       text="Disable Button", 
                       fg="red",
                       command=disable_button)
    disable.pack(side=tk.LEFT)

    enable = tk.Button(frame,
                       text="Enable Button",
                       command=enable_button)
    enable.pack(side=tk.LEFT)

    root.mainloop()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
