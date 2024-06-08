# clones the repo and enters it
git clone https://github.com/danjovich/pomodoro-cli
cd pomodoro-cli

# handles python venv to install the proper packages
python3 -m venv .venv                                                                                      
.venv/bin/python3 -m pip install -r requirements.txt

# checks for errors in the previous commands and exits if it finds any
if [ $? -ne 0 ]; then
  exit 1
fi

# adds a bash file to /usr/local/bin to make it available as a terminal command
ARG='\$@'
sudo sh -c "echo \"#!/usr/bin/sh
$(pwd)/.venv/bin/python3 $(pwd)/src/main.py $ARG\" > /usr/local/bin/pomodoro"
sudo chmod +x /usr/local/bin/pomodoro

# success message
echo "Pomodoro CLI installed! You can run it in a shell with the \"pomodoro\" command"