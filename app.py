from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        # Get user input from the form
        ses_access_key = request.form['ses_access_key']
        ses_secret_key = request.form['ses_secret_key']
        sender_email = request.form['sender_email']
        recipient_email = request.form['recipient_email']
        email_subject = request.form['email_subject']
        email_body = request.form['email_body']

        # Set up the SMTP connection to SES
        smtp_server = 'email-smtp.us-east-1.amazonaws.com'  # Replace with your SES endpoint
        smtp_port = 587  # Replace with your SMTP port
        smtp_username = ses_access_key
        smtp_password = ses_secret_key

        # Create the email message
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = email_subject
        msg.set_content(email_body)

        # Send the email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
                message = 'Email sent successfully.'
        except Exception as e:
            message = f'Error sending email: {str(e)}'

        return render_template('result.html', message=message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
