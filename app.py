import sys
sys.dont_write_bytecode = True

from manage_poke import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
