from time import sleep
from clearNLines import clearNLines
from typing import Literal
import subprocess

class Pomodoro:
    cycles = 0
    currentState: Literal['concentration',
                          'short-rest', 'long-rest'] = 'concentration'

    def __init__(self, concentrationTimeLenght: int = 25, shortIntervalLength: int = 5, longIntervalLength: int = 15):
        self.concentrationTimeLenght = concentrationTimeLenght
        self.shortIntervalLength = shortIntervalLength
        self.longIntervalLength = longIntervalLength

    def startCycle(self):
        while True:
            totalMinutes: int
            match self.currentState:
                case 'concentration':
                    totalMinutes = self.concentrationTimeLenght
                case 'short-rest':
                    totalMinutes = self.shortIntervalLength
                case 'long-rest':
                    totalMinutes = self.longIntervalLength

            remainingSeconds = totalMinutes * 60

            print(f'{self.currentState.capitalize()} timer started!')
            print('Time remaining:')

            while remainingSeconds >= 0:
                self.printMinutesAndSeconds(remainingSeconds)
                sleep(1)
                remainingSeconds -= 1
                if remainingSeconds >= 0:
                    clearNLines(1)

            if self.currentState.endswith('rest'):
                self.cycles += 1

            cyclesUntilLongRest = f'({4 - (self.cycles % 4)} cycles until long rest)'
            self.notify(
                f'{self.currentState.capitalize()} timer ended {cyclesUntilLongRest}')

            if self.currentState == 'short-rest' or self.currentState == 'long-rest':
                self.currentState = 'concentration'
            else:
                self.currentState = 'short-rest' if self.cycles == 0 or self.cycles % 4 != 0 else 'long-rest'

            ans = input(
                f'The timer is over! Go to a {self.currentState} timer {cyclesUntilLongRest} [y|n]? ')

            if ans.lower() != 'y' and ans.lower() != 'yes':
                break

            clearNLines(4)

    def printMinutesAndSeconds(self, seconds: int):
        minutes = seconds // 60
        minutesStr = str(minutes) if minutes >= 10 else f'0{minutes}'

        seconds = seconds % 60
        secondsStr = str(seconds) if seconds >= 10 else f'0{seconds}'

        print(minutesStr, ':', secondsStr, sep='')

    def notify(self, message: str) -> None:
        subprocess.call(['notify-send', '-u', 'normal', '-i',
                        'tomato', 'Pomodoro CLI', message])
