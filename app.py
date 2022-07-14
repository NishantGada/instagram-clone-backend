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
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
