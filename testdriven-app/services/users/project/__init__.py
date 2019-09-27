# /services/users/project/__init__.py

from flask import Flask, jsonify

# initiate the app
app = Flask(__name__)

# set config
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    }) 