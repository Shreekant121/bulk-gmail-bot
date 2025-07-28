# 📧 **Bulk Gmail Bot**

**_Send bulk emails effortlessly with your Gmail account!_**

The **Bulk Gmail Bot** is a sleek, web-based tool designed to simplify sending bulk emails using a Gmail account. Built with **Python** and **Flask**, it reads email lists from **Excel** or **CSV** files and sends personalized emails while respecting Gmail's sending limits. Whether you're a user looking for a straightforward way to send bulk emails or a developer eager to extend its functionality, this tool is for you!

---

## ✨ **Features**

- 📊 **File Support**: Upload **Excel (.xlsx)** or **CSV** files containing email lists.
- 🔍 **Smart Detection**: Automatically identifies the email column in your file.
- ⚙️ **Configurable Limits**: Set a daily sending limit (up to **500 emails** per Gmail's policy).
- 📜 **Detailed Logging**: Tracks sent and failed emails for easy monitoring.
- 🛠️ **Developer-Friendly**: Simple codebase, perfect for customization.

---

## 📋 **Requirements**

To run the **Bulk Gmail Bot**, ensure you have:

- 🐍 **Python 3.x** installed on your system.
- 📧 A **Gmail account** configured with:
  - **Less Secure Apps** enabled (if 2FA is disabled), **_OR_**
  - An **App Password** (if 2FA is enabled).  
    *Generate an App Password: Google Account > Security > 2FA > App Passwords.*

---

## 🚀 **Installation**

Follow these steps to set up the **Bulk Gmail Bot** on your machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shreekant121/bulk-gmail-bot.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd bulk-gmail-bot
   ```

3. **(Optional) Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   _This keeps dependencies isolated for a cleaner setup._

4. **Install Dependencies**:
   ```bash
   pip install flask pandas
   ```
   - **Flask**: Powers the web application.
   - **Pandas**: Handles Excel/CSV file processing.

---

## 🖥️ **Usage**

Get started with the **Bulk Gmail Bot** in just a few steps:

1. **Launch the Flask Application**:
   ```bash
   python app.py
   ```
   This starts the local web server.

2. **Access the Web Interface**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Complete the Form**:
   - **Upload File**: Select an **Excel (.xlsx)** or **CSV** file with email addresses.
   - **File Type**: Choose Excel or CSV.
   - **Email Column**: Specify the column name (e.g., "Email") or leave blank for auto-detection.
   - **Email Details**: Enter the subject and body. Use `{name}` for personalization if your file includes a "Name" column.
   - **Daily Limit**: Set a limit (max **500** for Gmail).
   - **Gmail Credentials**: Provide your Gmail username and password (or App Password for 2FA).

4. **Send Emails**:
   Click **"Send Emails"** to process and send the emails.

5. **Review Results**:
   Check the results page for sent/failed email details. Logs are saved in the `logs/` folder.

---

## ⚠️ **Important Notes**

- **2FA Users**: Use an **App Password** instead of your regular Gmail password.
- **Spam Prevention**: The bot includes a **1-second delay** between emails to avoid triggering Gmail's spam filters.
- **Basic Interface**: The UI prioritizes functionality but can be enhanced with custom styling.

---

## ⚖️ **Disclaimer**

Use the **Bulk Gmail Bot** responsibly! **_Only email recipients who have given consent._** Spamming violates Gmail’s Terms of Service and may lead to account suspension.

---

## 🗂️ **Configuration**

The app uses two default folders:
- **`uploads/`**: Stores uploaded Excel/CSV files.
- **`logs/`**: Stores logs of email activity.

To modify these paths, edit the `app.py` file and update the relevant variables.

---

## 🤝 **Contributing**

We’d love your help to make the **Bulk Gmail Bot** even better! Here’s how to contribute:

1. **Fork the Repository** on GitHub.
2. **Create a Branch**:
   ```bash
   git checkout -b your-feature-name
   ```
3. **Make Changes** and commit:
   ```bash
   git commit -m "Describe your changes here"
   ```
4. **Push to Your Fork**:
   ```bash
   git push origin your-feature-name
   ```
5. **Submit a Pull Request** with a clear description of your changes.

### 💡 **Ideas for Improvements**
- 🎨 Add **CSS styling** (e.g., via `styles.css`) to enhance the UI.
- 📧 Support additional email providers (e.g., Outlook, Yahoo).
- 🔒 Implement **OAuth2** for Gmail authentication.
- 🖌️ Expand personalization with placeholders like `{company}` or `{date}`.
- 🚨 Improve error handling for invalid files or failed sends.

---

## 📬 **Contact**

Have questions or ideas?  
- Open an **issue** on the [GitHub repository](https://github.com/Shreekant121/bulk-gmail-bot).
- Message me on X at **[@Shreekantbrand](https://x.com/Shreekantbrand)**.
