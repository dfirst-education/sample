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


# how to display env_name in Jupyter Notebook on VSCode
# after activating the virtual environment
env_name\Scripts\activate
pip install ipykernel
python -m ipykernel install --user --name env_name --display-name "env_name"
# restart VSCode
jupyter kernelspec list
# if you want to remove the env_name from Jupyter Notebook
jupyter kernelspec uninstall env_name
