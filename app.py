from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='build')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/drivefast')
def drive_fast():
    # Add your code here to control the robot car
    print("Driving fast!")
    return "Driving fast!", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
