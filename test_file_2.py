import subprocess
import os
import io

global p
p = subprocess.Popen(r"C:\Users\kiasd\Desktop\jake stuff\Minecraft 1.19.4 Server\start.bat", creationflags=subprocess.CREATE_NEW_CONSOLE, stdin=subprocess.PIPE, text=True)
