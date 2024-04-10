from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post', methods=['POST'])
def handle_post():
    # Get the JSON data from the request
    data = request.json
    print(" File Just arrived to Data lake")
    print(f"Received POST data: {data}")

    # Echo back the received data as a response
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
