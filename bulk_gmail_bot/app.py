from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from werkzeug.utils import secure_filename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['LOG_FOLDER'] = 'logs/'

# Create folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['LOG_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_emails', methods=['POST'])
def send_emails():
    # Get form data
    file = request.files['file']
    file_type = request.form['file_type']
    email_column = request.form['email_column']
    subject = request.form['subject']
    body = request.form['body']
    daily_limit = int(request.form['daily_limit'])
    gmail_user = request.form['gmail_user']
    gmail_password = request.form['gmail_password']

    # Save the uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Read the file based on type
    if file_type == 'excel':
        df = pd.read_excel(file_path)
    elif file_type == 'csv':
        df = pd.read_csv(file_path)
    else:
        return "Unsupported file type", 400

    # Detect email column if not found
    if email_column not in df.columns:
        detected_column = detect_email_column(df)
        if detected_column:
            email_column = detected_column
        else:
            return f"No email column found. Specified '{email_column}' not in file.", 400

    # Extract emails and names (if available)
    emails = df[email_column].dropna().tolist()
    total_emails = len(emails)
    has_name = 'Name' in df.columns

    # Send emails
    sent_count = 0
    failed_emails = []
    for index, email in enumerate(emails):
        if sent_count >= daily_limit:
            break
        email_body = body
        if has_name and '{name}' in body:
            name = df['Name'].iloc[index]
            email_body = body.replace('{name}', str(name))
        
        success = send_email(gmail_user, gmail_password, email, subject, email_body)
        if success:
            sent_count += 1
        else:
            failed_emails.append(email)
        time.sleep(1)  # 1-second delay between emails

    # Log results
    log_file = os.path.join(app.config['LOG_FOLDER'], 'email_log.txt')
    with open(log_file, 'a') as f:
        f.write(f"Date: {time.ctime()}\n")
        f.write(f"Total emails: {total_emails}, Sent: {sent_count}, Failed: {len(failed_emails)}\n")
        if failed_emails:
            f.write("Failed emails:\n")
            for email in failed_emails:
                f.write(f"{email}\n")
        f.write("\n")

    message = f"Processed {total_emails} emails. Sent: {sent_count}. Failed: {len(failed_emails)}. Check logs at {log_file}."
    return render_template('results.html', message=message)

def detect_email_column(df):
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    for column in df.columns:
        if df[column].dropna().str.match(email_pattern).any():
            return column
    return None

def send_email(gmail_user, gmail_password, to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        return False

if __name__ == '__main__':
    app.run(debug=True)