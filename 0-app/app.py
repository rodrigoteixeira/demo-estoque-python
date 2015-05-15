import os
from flask import Flask, url_for, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='/ui')


@app.route("/")
def hello():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))