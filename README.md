## SES Test Email

This is a Flask app that allows you to send a test email using the Amazon SES service. The app takes in the SES Access Key, SES Secret Key, sender email address, recipient email address, email subject, and email body as input and sends the email using the specified SMTP server.

### Prerequisites

To run this app, you will need:

- Python 3.x
- Flask
- smtplib
- An Amazon Web Services (AWS) account with access to the SES service

### Installation

1. Clone this repository to your local machine using Git.
2. Install the required dependencies by running the following command in the project directory:

```bash
pip install -r requirements.txt
```


4. Start the Flask app by running the following command:

```
python app.py
```


5. Access the app by navigating to `http://localhost:5000` in your web browser.

### Usage

1. Enter the SES Access Key, SES Secret Key, sender email address, recipient email address, email subject, and email body in the input fields on the app's home page.
2. Enter the SMTP server and port in the input fields on the app's home page.
3. Click the "Send Email" button to send the test email.
4. Wait for the app to display the result page indicating whether the email was successfully sent or not.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

This project was created with the help of the following resources:

- [Flask documentation](https://flask.palletsprojects.com/en/2.1.x/)
- [Amazon SES developer guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)
