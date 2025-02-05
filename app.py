from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST']) 
def validate_registration():  
    data = request.get_json()  

    full_name = data.get('fullName', '').strip()
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    phone_number = data.get('phoneNumber', '').strip()
    password = data.get('password', '')
    confirm_password = data.get('confirmPassword', '')
    gender = data.get('gender', '')

    
    if not full_name:
        return jsonify({'success': False, 'message': 'Full Name is required.'}), 400

    if not username:
        return jsonify({'success': False, 'message': 'Username is required.'}), 400

    if '@' not in email or '.' not in email:
        return jsonify({'success': False, 'message': 'Invalid email address.'}), 400

    if not phone_number.isdigit() or len(phone_number) != 10:
        return jsonify({'success': False, 'message': 'Phone number must be 10 digits.'}), 400

    if len(password) < 6:
        return jsonify({'success': False, 'message': 'Password must be at least 6 characters.'}), 400

    if password != confirm_password:
        return jsonify({'success': False, 'message': 'Passwords do not match.'}), 400

    if not gender:
        return jsonify({'success': False, 'message': 'Gender is required.'}), 400

    return jsonify({'success': True, 'message': 'Registration successful!'}), 200

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000,debug = True)
