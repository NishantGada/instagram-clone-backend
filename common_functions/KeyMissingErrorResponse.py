from flask import jsonify

def KeyMissingErrorResponse(message):
	print("Key Error: " + str(message))
	response = jsonify(Success=False, Message=message)
	response.status_code = 400
	return response