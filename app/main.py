from flask import Flask, jsonify, request, abort


app = Flask(__name__)

@app.route('/api/email', methods=['POST'])
def get_emails():
    data = request.json
    if not data:
        abort(400, description="Missing data")
    return jsonify(), 200

if __name__ == '__main__':
    app.run(debug=True)