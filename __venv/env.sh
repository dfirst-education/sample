# Description: Virtual environment setup script
python -m venv env_name
# python3.10 -m venv myenv

# activate the virtual environment
env_name\Scripts\activate
# linux
source env_name/bin/activate

# deactivate the virtual environment
deactivate

# list the virtual environments
dir /b
ls