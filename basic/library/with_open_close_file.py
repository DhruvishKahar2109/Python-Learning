import subprocess
import time

with open("hellofile1.txt","x") as f:
    f.write("Hello Dhruvish.!")

process = subprocess.Popen(["notepad.exe", "hello.txt"])

time.sleep(2)

process.terminate()

