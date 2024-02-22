from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/uppercase', methods=['POST'])
def return_uppercase():

    result = {
        'data': None,
        'error': None,
        'status_code': 200
    }

    try:
        body = request.data.decode('utf-8')

        json_object = json.loads(body)

        if not json_object:
            result['error'] = 'Missing body in request.'
            result['status_code'] = 400
    
    except Exception as e:
        print("Error while decoding body: {}".format(e))
        
        result['error'] = e
        result['status_code'] = 500
    
    if json_object and json_object.get('message'):
        result['data'] = json_object.get('message').upper()
    
    elif (not json_object.get('message')):
        result['error'] = "Body must contain dictionary key 'message' with corresponding value."
        result['status_code'] = 400
    
    return result, result['status_code']

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')