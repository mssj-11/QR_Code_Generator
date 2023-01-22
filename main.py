from flask import Flask, render_template, request
import qrcode   #   pip install qrcode
from io import BytesIO  #   pip install bytesbufio
from base64 import b64encode


app = Flask(__name__)


#   Server
@app.route('/')
def home():
    return render_template('index.html')   #   Return HTML

#   Method generateQR - POST
@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()  #   Memory save
    data = request.form.get('link')
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)
    base64_img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')
    
    return render_template('index.html', data=base64_img)


if __name__ == '__main__':
    app.run(debug=True)