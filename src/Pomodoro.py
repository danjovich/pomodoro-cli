from time import sleep
from clearNLines import clearNLines
from typing import Literal
import subprocess
from threading import Thread
import os
import platform
from readchar import readchar


class Pomodoro:
    currentState: Literal['concentration',
                          'short-rest', 'long-rest'] = 'concentration'
    quit = False
    pause = False
    error: Exception | KeyboardInterrupt | None = None
    threadShouldAcceptAnything = False

    def __init__(self, concentrationTimeLength: int = 25, shortIntervalLength: int = 5, longIntervalLength: int = 15, cycles: int = 0, mode: Literal['r', 'c'] = 'c'):
        self.concentrationTimeLength = concentrationTimeLength
        self.shortIntervalLength = shortIntervalLength
        self.longIntervalLength = longIntervalLength
        self.cycles = cycles
        self.determineState(mode)

    def determineState(self, mode: Literal['r', 'c']):
        if mode == 'r':
            self.currentState = 'short-rest' if self.cycles == 0 or self.cycles % 4 != 0 else 'long-rest'


    def startCycle(self):
        while True:
            thread = Thread(target=self.captureInput)
            thread.start()

            match self.currentState:
                case 'concentration':
                    totalMinutes = self.concentrationTimeLength
                case 'short-rest':
                    totalMinutes = self.shortIntervalLength
                case 'long-rest':
                    totalMinutes = self.longIntervalLength

            remainingSeconds = totalMinutes * 60

            print(f'\r{self.currentState.capitalize()} timer started!')
            print('Time remaining:')

            while remainingSeconds >= 0:
                while self.pause:
                    self.waitForKeyPress()
                    self.pause = False
                    clearNLines(1)
                if self.quit:
                    clearNLines(3)
                    return
                if self.error:
                    raise self.error
                self.printMinutesAndSeconds(remainingSeconds)
                sleep(1)
                remainingSeconds -= 1
                if remainingSeconds >= 0:
                    clearNLines(2)
            

            if self.currentState.endswith('rest'):
                self.cycles += 1

            cyclesUntilLongRest = f'({(4 - (self.cycles % 4)) if (self.cycles % 4) != 0 else 0} cycles until long rest)'
            self.notify(
                f'{self.currentState.capitalize()} timer ended {cyclesUntilLongRest}')

            if self.currentState == 'short-rest' or self.currentState == 'long-rest':
                self.currentState = 'concentration'
            else:
                self.currentState = 'short-rest' if self.cycles == 0 or self.cycles % 4 != 0 else 'long-rest'

            self.threadShouldAcceptAnything = True
            print('Press any key to continue...', end='\r')
            while thread.is_alive():
                sleep(0.1) # avoids excessive CPU usage
                continue

            ans = input(
                f'The timer is over! Go to a {self.currentState} timer {cyclesUntilLongRest} [y|n]? ')

            if ans.lower() != 'y' and ans.lower() != 'yes':
                break

            clearNLines(5)

    def printMinutesAndSeconds(self, seconds: int) -> None:
        minutes = seconds // 60
        minutesStr = str(minutes) if minutes >= 10 else f'0{minutes}'

        seconds = seconds % 60
        secondsStr = str(seconds) if seconds >= 10 else f'0{seconds}'

        print(minutesStr, ':', secondsStr, sep='')

    def notify(self, message: str) -> None:
        subprocess.call(['notify-send', '-u', 'normal', '-i',
                        'tomato', 'Pomodoro CLI', message])

    def captureInput(self):
        while True:
            char = repr(readchar())

            if self.threadShouldAcceptAnything:
                self.threadShouldAcceptAnything = False
                return

            if char == "'q'":
                self.quit = True
                return

            if char == "'p'":
                self.pause = True

            if char == "'\\x03'":
                self.error = KeyboardInterrupt()
                return

    def waitForKeyPress(self):
        if platform.system() == "Windows":
            os.system("pause")
        else:
            os.system(
                "/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
