import subprocess
import time

while True:
    subprocess.run(
        ["python", "jak.py"]
    )
    time.sleep(60*24*24)