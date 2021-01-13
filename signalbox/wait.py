"""
A long-running program to run as a test
process for the signalbox program.
"""

import datetime
import time


def main():
    while True:
        print(f"{datetime.datetime.now()}: Waiting...")
        time.sleep(1)


if __name__ == '__main__':
    main()
