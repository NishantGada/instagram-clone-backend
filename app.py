from flask import Flask, jsonify, request
import json

from common_functions.KeyMissingErrorResponse import KeyMissingErrorResponse

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

    try:
        if request.method == 'POST':

            DATA = request.json

            if not DATA.__contains__("name"):
                return KeyMissingErrorResponse("name key Missing")
            if not DATA.__contains__("email"):
                return KeyMissingErrorResponse("email key Missing")
            if not DATA.__contains__("phone"):
                return KeyMissingErrorResponse("phone key Missing")
            if not DATA.__contains__("bio"):
                return KeyMissingErrorResponse("bio key Missing")
            if not DATA.__contains__("number_of_posts"):
                return KeyMissingErrorResponse("number_of_posts key Missing")
            if not DATA.__contains__("posts"):
                return KeyMissingErrorResponse("posts key Missing")
            if not DATA.__contains__("followers"):
                return KeyMissingErrorResponse("followers key Missing")
            if not DATA.__contains__("following"):
                return KeyMissingErrorResponse("following key Missing")
            if not DATA.__contains__("username"):
                return KeyMissingErrorResponse("username key Missing")

            response = {
                "Success": "True",
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
                    "username": request.json['username'],
                }
            }
            response = jsonify(response)

    except Exception as e:
        response = {
            "Success": "False",
            "Message": "Technical Error",
            "Description": e
        }

    return response


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
            "username": "nishantgada"
        })
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
