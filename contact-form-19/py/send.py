from flask import Flask, render_template, request
from flask_mail import Mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_mail import Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use the appropriate port for your email server
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'karkala95@gmail.com'
app.config['MAIL_PASSWORD'] = 'oehpistdamrihzja'
app.config['MAIL_DEFAULT_SENDER'] = 'karkala95@gmail.com'  # Default sender for emails

mail = Mail(app)

# end

@app.route('/')
def index():
    return render_template('form.html')

# @app.route('/send_email', methods=['POST'])
# def send_email():
#     if request.method == 'POST':
#         # Get form data
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         message = request.form['message']
#         city = request.form['city']

#         # Email configuration
#         sender_email = "your_email@example.com"
#         receiver_email = "karkala95@gmail.com"

#         # SMTP configuration (example for Gmail)
#         smtp_server = "smtp.gmail.com"
#         smtp_port = 587
#         smtp_username = "karkala95@gmail.com"
#         smtp_password = "oehp istd amri hzja"

#         # Create message
#         msg = MIMEMultipart()
#         msg["From"] = sender_email
#         msg["To"] = receiver_email
#         msg["Subject"] = subject
#         msg.attach(MIMEText(f"Name: {name}\nEmail: {email}\n\n{message}", "plain"))

#         # Connect to SMTP server and send email
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.starttls()
#             server.login(smtp_username, smtp_password)
#             server.sendmail(sender_email, receiver_email, msg.as_string())

#         return "Email sent successfully"
    
#     # send email
    

@app.route('/send_email', methods=['POST'])
def send_email():
    # Create a message
    if request.method == 'POST':
        subject = request.form['name']
        name = request.form['name']
        email = request.form['email']
        recipients = ['mh525694@gmail.com']  # Replace with the recipient's email address
        phone = request.form['phone']
        message = request.form['message']
        city = request.form['city']
        degree = request.form['degree']
        gpa = request.form['gpa']
        country = request.form['country']
        course = request.form['course']
        print(name,email,phone,message,city,degree,gpa,country,course)
        message_body = render_template('email.html', name=name, message=message, email=email, phone=phone, city=city, degree=degree, gpa=gpa, country=country, course=course)  # You can use templates

        message = Message(subject=subject, recipients=recipients, body=message_body)

        # Send the message
        try:
            mail.send(message)
            return 'Email sent successfully!'
        
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(debug=True)
