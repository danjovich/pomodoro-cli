from Pomodoro import Pomodoro
from argparse import ArgumentParser
from os import path
import subprocess

parser = ArgumentParser(
    prog='Pomodoro CLI',
    description='A simple CLI thats serves as a minimal interface for the pomodoro concentration technique'
)
parser.add_argument('-u', '--update', action='store_true',
                    help='update the app')
parser.add_argument('-c', '--concentration-length',
                    help='the length of the concentration time in minutes')
parser.add_argument('-s', '--short-length',
                    help='the length of the short interval in minutes')
parser.add_argument('-l', '--long-length',
                    help='the length of the long interval in minutes')
parser.add_argument('-cy', '--cycle',
                    help='the cycle in which to start')
parser.add_argument('-m', '--mode',
                    choices=['r', 'c'],
                    default='c',
                    help='start in rest mode "r" or concentration mode "c" (default)')
args = parser.parse_args()

if args.update:
    print('Updating the Pomodoro CLI!')
    dirName = path.realpath(path.dirname(__file__))
    subprocess.call(['bash', f'{dirName}/../scripts/update.sh'])
    exit()

concentrationTimeLength = int(
    args.concentration_length) if args.concentration_length is not None else 25
shortIntervalLength = int(
    args.short_length) if args.short_length is not None else 5
longIntervalLength = int(
    args.long_length) if args.long_length is not None else 15
cycle = int(args.cycle) if args.cycle is not None else 0


print('Pomodoro CLI 🍅')

pomodoro = Pomodoro(concentrationTimeLength,
                    shortIntervalLength,
                    longIntervalLength,
                    cycle,
                    args.mode)
pomodoro.waitForKeyPress()
pomodoro.startCycle()

print('Program ended')
