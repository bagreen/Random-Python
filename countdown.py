#! python3

import subprocess, time

timeLeft = 30
while timeLeft > 0:
    print(timeLeft, end='')
    print('')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['cvlc', 'alarm.wav'])
