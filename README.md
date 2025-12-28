DISCLAIMER: This is a proof-of-concept keylogger developed strictly for educational and defensive cybersecurity purposes. It is intended for authorized security testing, academic study, and understanding attacker techniques to build better defenses.

    It is illegal to use this software on any system you do not own or have explicit written permission to test.

    Misuse of this tool for unauthorized surveillance, stealing credentials, or any malicious activity is a serious crime.

    This code is published for my cybersecurity portfolio to demonstrate technical understanding, not for malicious use.


Project Purpose:

This is my first public GitHub project, created to deepen my understanding of:

    Operating System Hooks: How applications can intercept low-level system events (keystrokes).

    Persistent Processes: Techniques for creating background processes and persistence mechanisms.

    Data Exfiltration: Basic methods of capturing and logging data (local file output in this POC).

    Anti-Virus Evasion Fundamentals: Understanding how security software detects such artifacts (for defensive purposes).


Technical Overview:

    Keystroke Capture: Logs all keyboard input to a specified file.

    Stealth Execution: Runs as a background process (demonstration of basic persistence).

    Timestamping: Each logged entry includes a timestamp for analysis.

    Local Logging: Outputs data to a local file (for simplicity and safety in this POC).
    Language used: Python

Note: This is a basic implementation for learning. Real-world malicious keyloggers are far more complex and use advanced obfuscation, encryption, and C2 (Command & Control) communication.

Authorized Use Case Examples:

    Testing on your own computer or in an isolated lab environment (e.g., VirtualBox/VMware VM with no network access).

    Academic research with proper oversight.

    As part of a controlled penetration test with a signed scope of work.

   
 ### **Critical Pre-Requirements & Ethical Guidelines**

**BEFORE YOU BEGIN:**
1. **LEGAL COMPLIANCE:** Only run this software on systems you **own** or have **explicit written authorization** to test.
2. **ISOLATED ENVIRONMENT:** Use a **virtual machine (VM)** with no network access. Recommended: VirtualBox/VMware with network set to "Host-Only" or "NAT Network" (no internet).
3. **INFORMED CONSENT:** If demonstrating to others, ensure they understand what data will be captured and that it's for educational purposes only.
4. **DATA HANDLING:** All captured data must be immediately deleted after testing. Never capture real credentials or sensitive information.

**Lab Setup Instructions**

```bash
# Step 1: Create a Secure Testing Environment
# -------------------------------------------
# 1. Download and install VirtualBox (https://www.virtualbox.org/)
# 2. Create a new VM with a clean Windows 10/11 or Linux installation
# 3. Configure VM network settings to "Host-Only Adapter"
# 4. Take a VM snapshot before running any tests (for easy rollback)

# Step 2: Download the Source Code
# ---------------------------------
# Method A: Clone repository (if VM has limited network access)
git clone https://github.com/yourusername/educational-keylogger.git
cd educational-keylogger

# Method B: Download and transfer via USB (more secure isolation)
# 1. On host machine: Download ZIP from GitHub
# 2. Disable VM network completely
# 3. Transfer ZIP via shared folder or USB

# Step 3: Installation & Dependencies
# ------------------------------------
# Python Version (example):
pip install -r requirements.txt  # or install specific dependencies
# If no dependencies: python keylogger.py

# Compiled Language (C/C++ example):
gcc -o keylogger keylogger.c  # Compile for analysis only
# Note: Some AV may flag the compiled binary even in VM
```

### **Usage Examples (Controlled Testing)**

```python
# Example 1: Basic Testing - Monitor your own input
# --------------------------------------------------
# Run with: python keylogger.py --output test.log --duration 30
# Type: "test123" followed by [ENTER], [TAB], [BACKSPACE]
# Expected output in test.log:
# [2024-01-15 10:30:00] t
# [2024-01-15 10:30:01] e
# [2024-01-15 10:30:01] s
# [2024-01-15 10:30:02] t
# [2024-01-15 10:30:02] 1
# [2024-01-15 10:30:03] 2
# [2024-01-15 10:30:03] 3
# [2024-01-15 10:30:04] [ENTER]
# [2024-01-15 10:30:05] [TAB]
# [2024-01-15 10:30:06] [BACKSPACE]

# Example 2: Persistence Testing (Admin Rights Required)
# -------------------------------------------------------
# Run with: python keylogger.py --install --startup
# Reboot VM and verify persistence mechanism
# Immediately uninstall: python keylogger.py --uninstall

# Example 3: Defensive Detection Testing
# ---------------------------------------
# 1. Run keylogger in background
# 2. Use defensive tools (see next section) to detect it
# 3. Document detection methods and effectiveness
```

### **Safety Controls**

1. **Automatic Shutdown:**
```python
# Code should include safety mechanisms like:
if __name__ != "__main__":
    sys.exit(0)  # Prevent import/execution as module
if not is_authorized_environment():
    self_destruct()  # Check for VM markers, test environment flags
```

2. **Environment Validation:**
   - Check for VM artifacts (VirtualBox, VMware indicators)
   - Validate test flags or configuration
   - Limit runtime duration (auto-terminate after 5 minutes)

3. **Data Sanitization:**
```bash
# Post-test cleanup script
rm -f *.log
rm -f /tmp/keystrokes.*
# Use secure deletion tools for sensitive data
```

---

## **Defensive Mitigations & Detection Techniques**

This section demonstrates understanding of **Blue Team/defensive cybersecurity** by explaining how to detect, prevent, and respond to such threats.

### ** Prevention **

1. **Application Whitelisting:**
   - **Implementation:** Use tools like AppLocker (Windows) or SELinux/AppArmor (Linux)
   - **Effect:** Prevents unauthorized executables from running
   - **Example:** `Allow only signed applications from C:\Program Files\`

2. **Principle of Least Privilege:**
   - Users operate with minimal necessary permissions
   - Keyloggers often require admin rights for persistence - limit admin accounts
   - Use User Account Control (UAC) at highest setting

3. **System Hardening:**
   - Disable unnecessary services (especially remote access)
   - Remove/local admin privileges where not needed
   - Implement Windows Defender Application Control (WDAC)

### ** Detection (Indicators of Compromise)**

4. **Process Monitoring:**
   ```powershell
   # PowerShell detection commands:
   Get-Process | Where-Object {$_.Path -like "*temp*"}  # Suspicious locations
   Get-WmiObject Win32_Process | Select Name, ProcessId, CommandLine
   # Look for: Unusual parent processes, hidden windows, mismatched process names
   ```

5. **File System Monitoring:**
   - Monitor creation of `.log`, `.txt` files in unusual locations (`%AppData%`, `%Temp%`)
   - Watch for files with system/archive attributes: `attrib +s +h malicious.exe`
   - Use File Integrity Monitoring (FIM) for critical directories

6. **Registry & Persistence Monitoring:**
   ```bash
   # Common persistence locations to monitor:
   Windows: HKLM\Software\Microsoft\Windows\CurrentVersion\Run
   Windows: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
   Linux: /etc/rc.local, ~/.bashrc, cron jobs (@reboot)
   macOS: LaunchAgents, LaunchDaemons
   ```

7. **Network Indicators:**
   - Unexpected outbound connections (even for local logging tools)
   - DNS requests to suspicious domains
   - Unusual protocol usage on localhost

### ** Technical Detection Tools**

8. **Endpoint Detection & Response (EDR):**
   - Commercial: CrowdStrike, SentinelOne, Microsoft Defender for Endpoint
   - Open Source: Wazuh, Osquery, Elastic Security
   - Key Capabilities: Behavioral analysis, memory scanning, hook detection

9. **Anti-Virus & Anti-Malware:**
   - **Signature-based:** Detects known patterns (this keylogger's hash)
   - **Heuristic/Behavioral:** Detects keylogging behavior (hook installation, keystroke monitoring)
   - **Examples:** Windows Defender, ClamAV, Malwarebytes

10. **Memory Analysis:**
    ```bash
    # Tools for memory forensics:
    Volatility Framework: python vol.py -f memory.dump windows.pslist
    Rekall: rekall pslist
    # Look for: Injected threads, API hooks, suspicious DLLs
    ```

11. **Sysinternals Suite (Specific Detection):**
    - **Process Explorer:** Verify digital signatures, view handles/DLLs
    - **Process Monitor:** Real-time file/registry/process monitoring
    - **Autoruns:** Startup persistence detection
    - **Sigcheck:** Verify file hashes against VirusTotal

### ** Hands-On Detection Exercise**

```bash
# Exercise: Detect this keylogger in your VM
# ------------------------------------------
# 1. Run the keylogger with default settings
# 2. Open Process Explorer (Windows) or 'htop' (Linux)
# 3. Identify the suspicious process:
#    - Unknown publisher
#    - Unusual parent process
#    - Multiple threads
#    - Hooks to win32k.sys or similar

# 4. Check for open handles to log files:
handle.exe | findstr /i ".log .txt"

# 5. Examine network connections (even if local):
netstat -ano | findstr LISTENING
netstat -bano  # Windows with binaries

# 6. Scan with built-in AV:
# Windows: "Start > Windows Security > Quick Scan"
# Linux: clamscan -r /home/user/

# 7. Check registry persistence:
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

### ** Defensive Metrics & Monitoring**

12. **SIEM Alerting Rules (Splunk, Elastic SIEM examples):**
    ```sql
    # Detect keylogger installation attempts
    source="*.log" process_name="*keylogger*" OR command_line="*hook*" 
    | stats count by host, user
    
    # Detect persistence mechanism creation
    registry_path="*Run*" AND process_name NOT IN ("explorer.exe","System")
    
    # File creation in suspicious locations
    file_path="*/AppData/Local/Temp/*.log" AND file_size>100KB
    ```

13. **YARA Rules for Detection:**
    ```yara
    rule Keylogger_Behavior {
        meta:
            description = "Detects keylogging behavior"
            author = "Your Name"
        
        strings:
            $hook1 = "SetWindowsHookEx"
            $hook2 = "WH_KEYBOARD_LL"
            $hook3 = "GetAsyncKeyState"
            $persistence = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        
        condition:
            any of them and filesize < 500KB
    }
    ```

### ** Incident Response Checklist**

If a keylogger is detected:

1. **Containment:**
   - Isolate affected system from network
   - Disable compromised accounts
   - Preserve evidence (memory dump, disk image)

2. **Eradication:**
   - Remove persistence mechanisms (registry, startup folders)
   - Delete malicious files
   - Reset credentials that may have been captured

3. **Recovery:**
   - Restore from clean backup
   - Rebuild system if necessary
   - Implement stronger controls

4. **Post-Incident:**
   - Root cause analysis
   - Update detection rules
   - Employee training on phishing/social engineering

### ** Educational Takeaways for Defenders**

- **Understand Attackers:** By building offensive tools, defenders better understand TTPs (Tactics, Techniques, Procedures)
- **Defense in Depth:** No single control is sufficient; layer preventive, detective, and responsive controls
- **Assume Breach:** Design systems assuming some attacks will succeed; focus on detection and response
- **Continuous Monitoring:** Security is not a one-time setup but continuous process
