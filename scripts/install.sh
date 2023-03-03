git clone https://github.com/danjovich/pomodoro-cli
pip install readchar
if [ $? -ne 0 ]; then
  exit 1
fi
cd pomodoro-cli
ARG='\$1'
sudo sh -c "echo \"#!/usr/bin/sh\npython3 $(pwd)/src/main.py $ARG\" > /usr/local/bin/pomodoro"
sudo sh -c "chmod +x /usr/local/bin/pomodoro"
echo "Pomodoro CLI installed! You can run it in a shell with the \"pomodoro\" command"