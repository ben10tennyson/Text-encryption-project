from flask import Flask, render_template, request
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']

        # Encrypt the text
        encrypted_text = cipher_suite.encrypt(text.encode())
        
        return render_template('index.html', encrypted_text=encrypted_text.decode(), original_text=text)
    
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_text = request.form['encrypted_text']
    
    # Decrypt the text
    decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
    
    return render_template('index.html', decrypted_text=decrypted_text.decode(), original_encrypted_text=encrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
