import ctypes

# Flags
SHERB_NOCONFIRMATION = 0x00000001
SHERB_NOPROGRESSUI = 0x00000002
SHERB_NOSOUND = 0x00000004

try:
    ctypes.windll.shell32.SHEmptyRecycleBinW(
        None,
        None,  # None = all drives
        SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND
    )
    print("Recycle Bin emptied successfully.")
except Exception as e:
    print(f"Error: {e}")