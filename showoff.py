import os
from time import gmtime, sleep, strftime, time

os.system("")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
start = time()
i = 0
while i < 96:
    print(bcolors.OKBLUE + f"{time() - start:.0f} seconds remaining " + animation[i % len(animation)] + bcolors.ENDC,
          end="\r")
    i += 1
    sleep(0.2)
print('\n')
