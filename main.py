from flask import Flask, render_template, request
import qrcode


app = Flask(__name__)

#   Server
@app.route('/')
def home():
    return render_template('index.html')   #   Return HTML

if __name__ == '__main__':
    app.run(debug=True)
