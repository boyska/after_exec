import os
import sys

import time

SLEEP_TIME = 2
def process_exist(pid):
    try:
        os.kill(pid, 0)
    except OSError, e:
        return False
    else:
        return True

if __name__ == '__main__':
    while process_exist(int(sys.argv[1])):
        time.sleep(SLEEP_TIME)
    if len(sys.argv) > 2:
        os.system(' '.join(sys.argv[2:]))
