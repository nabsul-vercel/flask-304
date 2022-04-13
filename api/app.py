from flask import Flask
import os
app = Flask(__name__)

@app.route('/files')
def show_files():
    return os.popen('ls -la').read()

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

