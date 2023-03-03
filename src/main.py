from Pomodoro import Pomodoro
from read_single_keypress import read_single_keypress
from clearNLines import clearNLines

print('Pomodoro CLI 🍅')

print('Press any key to start...')
read_single_keypress()
clearNLines(1)

pomodoro = Pomodoro()
pomodoro.startCycle()

print('Program ended')