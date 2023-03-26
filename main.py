from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/download/style.css')
def download_style():
    return send_file('static/css/style.css', as_attachment=True)

@app.route('/download/js.js')
def download_javascript():
    return send_file('static/js/script.js', as_attachment=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pick_excuse')
def pick_excuse():
    return "Sorry, I'm all out of excuses!"

@app.route('/generate_random_excuse')
def generate_random_excuse():
    return "I couldn't make it because I had to attend a virtual meeting."

@app.route('/feeling_lucky')
def feeling_lucky():
    return "Congratulations, you're feeling lucky!"

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    number = request.form['number']
    purpose = request.form['purpose']
    appointment_type = request.form['appointment-type']
    name = request.form['name']
    date = request.form['date']
    convenience = request.form['convenience']
    return f"Appointment submitted for {name} on {date} at {convenience} convenience. We will contact you at {number} regarding your {appointment_type} appointment to schedule a {purpose}."

if __name__ == '__main__':
    app.run(debug=True)
