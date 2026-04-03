📌 Comprehensive Penetration Testing & VAPT Labs
📖 Overview

This repository contains practical labs and a full-scale Vulnerability Assessment and Penetration Testing (VAPT) engagement performed as part of a cybersecurity internship. It demonstrates hands-on experience in exploitation, API security testing, privilege escalation, network attacks, and mobile application security.

🎯 Objectives
Perform real-world penetration testing scenarios
Identify and exploit vulnerabilities across multiple domains
Demonstrate post-exploitation techniques and persistence
Document findings with remediation strategies
Align testing with industry standards such as PTES and OWASP
🧪 Labs Covered
1. Advanced Exploitation Lab
Remote Code Execution (RCE) exploitation (WordPress)
Custom exploit modification (Python PoC)
Reverse shell deployment
Binary analysis basics

Key Outcome:

Successful reverse shell access via PHP payload
2. API Security Testing Lab
Manual API testing using Burp Suite
OWASP API Top 10 vulnerabilities identification

Vulnerabilities Identified:

Broken Object Level Authorization
Broken Function Level Authorization
Security Misconfiguration
Unrestricted Resource Consumption
3. Privilege Escalation & Persistence Lab
Enumeration using LinPEAS
Exploitation of SUID binaries via GTFOBins
Root privilege escalation
Persistence using cron jobs

Key Outcome:

Root shell obtained
Persistence established via scheduled tasks
4. Network Protocol Attacks Lab
SMB Relay Attack (NTLM Relay)
ARP Spoofing (Man-in-the-Middle)
Traffic interception using Wireshark

Tools Used:

Responder
ntlmrelayx
Ettercap
Wireshark
5. Mobile Application Security Testing
Static analysis using MobSF
Android security assessment

Vulnerabilities Identified:

Insecure External Storage Usage
Debug Enabled Application
Debug Certificate Usage
Support for Vulnerable Android Versions
🛠️ Tools & Technologies
Kali Linux
Metasploit Framework
Burp Suite
LinPEAS
GTFOBins
Responder & ntlmrelayx
Ettercap & Wireshark
MobSF, Frida, Drozer
Nmap
📊 Capstone VAPT Project
Target
HackTheBox Machine: Lame
Key Vulnerability
VSFTPD 2.3.4 Backdoor Command Execution (CVE-2011-2523)
Methodology
Reconnaissance
Scanning
Vulnerability Analysis
Exploitation
Post-Exploitation
Reporting
Result
Full system compromise
Root-level access achieved
Demonstrated lateral movement potential
⚠️ Impact Highlights
Remote Code Execution (RCE)
Full System Takeover
Data Exfiltration
Persistent Backdoor Access
Network-wide compromise risk
🔐 Remediation Strategies
Regular patching and updates
Secure coding practices
Principle of Least Privilege (PoLP)
Input validation and sanitization
Disable unnecessary services
Enforce secure configurations

📌 Key Learnings
Practical exploitation techniques across multiple attack surfaces
Importance of misconfiguration and outdated services
Real-world attack chaining and post-exploitation strategies
Defensive recommendations for enterprise environments
⚖️ Disclaimer

This project is intended for educational purposes only. All testing was conducted in controlled lab environments such as HackTheBox and authorized setups. Unauthorized use of these techniques is strictly prohibited.
