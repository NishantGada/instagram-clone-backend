from flask import Flask, jsonify

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

@app.route('/getLastName', methods=['GET'])
def getLastName():
    name = {
        "lastName": "Gada"
    }
    result = jsonify(name)
    return result

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
