#! /bin/bash

if [ ! -d "py36dev" ]; then
  echo "Creating virtual environment py36dev"
  virtualenv --python=/usr/bin/python3.5 py36dev
  source py36dev/bin/activate
  pip install -r requirements_py3.txt
fi

# Enter the python virtual enviro on the current shell
echo "Entering virtual environment py36dev"
bash --rcfile <(echo '. py36dev/bin/activate')

# use echo $BASHPID to check the bash prompt process id

