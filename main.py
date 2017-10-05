#!/usr/bin/env python3

import time
import random

def getInt(text=''):
    while True:
        try:
            i = int(input(text))
            break # Exit while loop if i is a number
        except ValueError:
            print('A number please..')

    return i


def test():
    # Get time interval
    min = getInt('min (s): ')
    max = getInt('max (s): ')

    # Main loop
    while True:
        sleepTime = random.uniform(min, max)
        print(sleepTime)
        time.sleep(sleepTime)


def main():
    # Get time interval
    min = getInt('min (s): ')
    max = getInt('max (s): ')

    # Main loop
    diff = 0.0
    while True:
        sleepTime = random.uniform(min, max)
        time.sleep(sleepTime - diff) # FIXME sleepTime - diff must be a positive number

        start = time.time()
        input('Drink!\a')
        end = time.time()
        diff = end - start


if __name__ == '__main__':
    print('CTRL-C (KeyboardInterrupt) to exit')

    try:
        main()
    except KeyboardInterrupt:
        print()
        pass # exit script
