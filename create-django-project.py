import os
import virtualenv
import pip
import subprocess
from django.core import management


directoryName = input('Enter your project name: ')

dir = "K:\\Programming\\Python\\Scripts\\Eyakub\\"
venv = "venv"
djangoVersion = "2.2"
venvDir = dir + directoryName + '\\' + venv + '\\'


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(dir + directory)
            os.chdir(dir + directory)
            virtualenv.create_environment(
                os.path.join((dir + directory + '\\' + venv + '\\'))
            )
            activate_script = dir + directory + '\\' + venv + '\\' + 'Scripts' + '\\' + 'activate.bat'
            print(activate_script)
            
            exec(compile(open(activate_script, 'rb').read(),
                         activate_script, 'exec'), dict(__file__=activate_script))
            os.makedirs('src')

    except OSError:
        print('Error: Creating directory.' + directory)


createFolder(directoryName)
