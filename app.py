from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/Myhobbies.html')
def serve_hobbies():
    return send_from_directory('.', 'Myhobbies.html')

@app.route('/ContactMe.html')
def serve_contact():
    return send_from_directory('.', 'ContactMe.html')

@app.route('/GitNotes.html')
def serve_git():
    return send_from_directory('.', 'GitNotes.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
