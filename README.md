# Pomodoro CLI 🍅

Pomodoro CLI is a simple CLI written in Python thats serves as a minimal interface for the [pomodoro concentration technique](https://en.wikipedia.org/wiki/Pomodoro_Technique). 

It shows a timer in the terminal, and sends notifications when each timer/cycle has ended, using the Linux command `notify-send` (this will obviously only work on Linux). 

### Installation
To install, inside a terminal, enter the directory where you want the source code to be and simply run:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/danjovich/pomodoro-cli/main/scripts/install.sh)"
```

### Usage
Once installed, you can run the program by simply running the following command in a terminal:

```bash
pomodoro
```

To make it easier to update the app to possible changes on this repository, run:

```bash
pomodoro -u
# or
pomodoro --update
```

