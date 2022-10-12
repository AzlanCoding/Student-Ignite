from flask import Flask
#import socket
#socket.getaddrinfo('student.ignite', 8080)

app = Flask(__name__)

#app.secret_key = 'supersecretkey'
#app.config['SERVER_NAME'] = 'localhost'
#app.run(host=app.config['SERVER_NAME'], port=4343, debug=True)

@app.route('/Ignition/v1/signin')
def hello():
    return 'Hello, World!'
@app.route('/')
def hellao():
    return 'Home'
if __name__ == "__main__":
    app.run(host='0.0.0.0')
else:
    print(__name__)
