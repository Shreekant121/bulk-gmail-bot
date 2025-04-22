Bulk Gmail Bot

The Bulk Gmail Bot is a web-based application that allows users to send bulk emails using their Gmail account. It reads a list of email addresses from an Excel or CSV file, and sends emails while respecting Gmail's sending limits. The tool is built with Python and Flask, featuring a simple, functional interface. It’s perfect for users who need a straightforward way to send bulk emails and for developers who might want to extend its functionality.

Features
Supports Excel (.xlsx) and CSV files for email lists

Automatically detects the email column in the uploaded file

Configurable daily sending limit (max 500 emails per day for Gmail)

Logs sent and failed emails for tracking

Requirements
To run the Bulk Gmail Bot, you’ll need:
Python 3.x installed on your system

A Gmail account with either:
"Less Secure Apps" enabled (if 2FA is disabled), or

An App Password (if 2FA is enabled)
You can get an app password from going to manage account < security < 2FA Auth < Generate app password
Installation
Follow these steps to set up the project on your machine:
Clone the repository:
bash

git clone https://github.com/Shreekant121/bulk-gmail-bot.git


Navigate to the project directory:
bash

cd bulk-gmail-bot

(Optional) Create a virtual environment:
bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

This step is recommended to keep dependencies isolated.

Install the required packages:
bash

pip install flask pandas

These are the core dependencies: Flask for the web app and pandas for handling Excel/CSV files.

Usage
Here’s how to run and use the Bulk Gmail Bot:
Start the Flask application:
bash

python app.py

This launches the web server locally.

Open your web browser and go to:

http://127.0.0.1:5000/

Fill in the form:
Upload your file: Select an Excel (.xlsx) or CSV file with a list of email addresses.

Select file type: Choose whether it’s Excel or CSV.

Specify email column: Enter the column name containing emails (e.g., "Email"), or leave it blank for automatic detection.

Enter email details: Provide the subject and body (use {name} for personalization if your file has a "Name" column).

Set daily limit: Enter a number (max 500 for Gmail).

Provide Gmail credentials: Enter your Gmail username and password (or App Password).

Click "Send Emails": The bot will process the list and send the emails.

Check results: After completion, view the results on the next page. Logs of sent and failed emails are saved in the logs/ folder.

Important Notes
If using a Gmail account with 2FA, generate an App Password in your Google Account settings and use it instead of your regular password.

The bot adds a 1-second delay between emails to avoid triggering spam filters.

The interface is basi, focusing on functionality over appearance.

Disclaimer
Use this tool responsibly. Ensure you have permission to email your recipients. Spamming violates Gmail’s terms of service and may result in account suspension.
Configuration
The app uses two default folders:
uploads/: Stores uploaded Excel/CSV files.

logs/: Stores log files tracking email activity.

To change these paths, edit the app.py file and update the relevant variables.
Contributing
We welcome contributions to improve the Bulk Gmail Bot! Here’s how to get involved:
Fork the repository on GitHub.

Create a branch for your changes:
bash

git checkout -b your-feature-name

Make your improvements and commit them:
bash

git commit -m "Describe your changes here"

Push to your fork:
bash

git push origin your-feature-name

Submit a pull request with a clear description of your changes.

Ideas for Advancements:
Add styling: Reintroduce CSS (e.g., via a styles.css file) to improve the UI.

Support other providers: Extend functionality to work with Outlook, Yahoo, etc.

Enhance security: Implement OAuth2 for Gmail instead of "Less Secure Apps" or App Passwords.

More personalization: Add support for multiple placeholders (e.g., {company}, {date}).

Error handling: Improve feedback for invalid files or failed sends.

Contact
Have questions or suggestions? Open an issue on the GitHub repository.
or message me at @Shreekantbrand on X.com