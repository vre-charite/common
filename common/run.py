from app import create_app
from config import ConfigClass

flaskapp = create_app()

# add to https
if __name__ == '__main__':
    flaskapp.run(debug=True, port=ConfigClass.settings.port)