from Pomodoro import Pomodoro
from argparse import ArgumentParser
from os import path
import subprocess

parser = ArgumentParser(
    prog='Pomodoro CLI',
    description='A simple CLI thats serves as a minimal interface for the pomodoro concentration technique'
)
parser.add_argument('-u', '--update', action='store_true', help='update the app')
args = parser.parse_args()

if args.update:
    print('Updating the Pomodoro CLI!')
    dirName = path.realpath(path.dirname(__file__))
    subprocess.call(['bash', f'{dirName}/../scripts/update.sh'])
    exit()

print('Pomodoro CLI 🍅')

pomodoro = Pomodoro()
pomodoro.waitForKeyPress()
pomodoro.startCycle()

print('Program ended')
