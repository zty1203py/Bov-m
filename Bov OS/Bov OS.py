import os
import sys
import time
from pyfiglet import Figlet
fig = Figlet(font='slant')

ascii_art = fig.renderText('Bov OS')
print(ascii_art)
print('-'*40)

import time


def log_message(phase, message, delay=1):
    timestamp = time.time()
    print(f"[{timestamp:.9f}]({phase}) {message}")
    time.sleep(delay)


def boot_system():
    print("Welcome to Bov-T!")

    log_message("Phase 1", "Loading packages...")
    log_message("0.883178087157870", "OpenPy_Core-v1.0, PyFilesystem, colorama, time, os, sys, wget, random")
    log_message("1.220519711874608", "Enabling 'OpenPy_Core'...")
    log_message("1.649296575891091", "Packages enabled successfully(8)")
    log_message("2.123197247219186", "WARNING! 'OpenPy_Core' has an update available(v1.0-->v1.0)")
    log_message("2.573675329079889",
                "WARNING! 'Bov OS_core' is deprecated and will be replaced by 'OpenPy' in further versions")

    log_message("Phase 2", "Booting system...")
    log_message("2.809674971546694", "Loading system components...")
    log_message("3.158177104225294", "command_input, time_box, keyboard_driver, shutdown, reboot")

    print("\nSystem booted successfully!")

if __name__ == "__main__":
    boot_system()

from pyfiglet import Figlet
fig = Figlet(font='banner')

ascii_art = fig.renderText('welcome!')
print(ascii_art)
print('-'*50)

# 启动另一个Python程序
os.system("python system16\password.py")