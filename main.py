from flask import Flask
import jwt

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def requestToken():
    return jwt.encode({"loggedin" : "you-decide"}, 'secret', algorithm='HS256') 

app.run(host='0.0.0.0', port=8000, debug=False)