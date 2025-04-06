from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['GET'])
def callback():
    # Handle authorization callback
    code = request.args.get('code')
    print(f'Received authorization code: {code}')
    return 'Authorization successful!'

if __name__ == '__main__':
    app.run(port=5000)
