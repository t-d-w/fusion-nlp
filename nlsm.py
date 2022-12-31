# Assuming you have not changed the general structure of the template no modification is needed in this file.
import adsk.core
from . import commands
from .lib import fusion360utils as futil


def run(context):
    try:
        # This will run the start function in each of your commands as defined in commands/__init__.py
        commands.start()
        import sys
        #import pip
        """
        try:
            import openai
            openaiinstallworked=1
            #continue
        except ModuleNotFoundError:
            pip.main(['install', 'openai'])
            openaiinstallworked=0
        print(f'did it? {openaiinstallworked}\n')
        """
        #sys.path.remove('C:\\Users\\Thomas D Wilkinson\\anaconda3\\lib\\site-packages\\openai')
        msg1=f"Add in created. Heres some info: \n\nsys path: {sys.path}\n\n sys version: {sys.version}\n\n executable location: {sys.executable}"
        app = adsk.core.Application.get()
        ui = app.userInterface
        ui.messageBox(msg1)
        
    except:
        futil.handle_error('run')


def stop(context):
    try:
        # Remove all of the event handlers your app has created
        futil.clear_handlers()

        # This will run the start function in each of your commands as defined in commands/__init__.py
        commands.stop()

    except:
        futil.handle_error('stop')