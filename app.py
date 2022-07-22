from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def homepage():
    return "Test"

@app.route('/getFirstName', methods=['GET'])
def getFirstName():
    name = {
        "firstName": "Nishant"
    }
    result = jsonify(name)
    return result

@app.route('/saveUserDetails', methods=['POST'])
def saveUserDetails():

    if request.method == 'POST':
        return({
            "status": "Success",
            "description": "User details saved successfully",
            "data": {
                "name": request.json['name'],
                "email": request.json['email'],
                "phone": request.json['phone'],
                "bio": request.json['bio'],
                "number_of_posts": request.json['number_of_posts'],
                "posts": request.json['posts'],
                "followers": request.json['followers'],
                "following": request.json['following'],
            }
        })


@app.route('/getUserDetails', methods=['GET'])
def getUserDetails():
        return({
            "name": "Nishant Gada",
            "email": "test@gmail.com",
            "phone": "9022379777",
            "bio": "Namaste",
            "number_of_posts": "10",
            "posts": [],
            "followers": "10,000",
            "following": "250",
        })
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
