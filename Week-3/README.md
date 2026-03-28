# Advanced VAPT Lab: Exploitation, Web Testing & Security Reporting

## Overview

This repository documents a complete **Vulnerability Assessment and Penetration Testing (VAPT)** lifecycle, covering:

- Theoretical foundations  
- Practical exploitation  
- Web application testing  
- Reporting  
- Post-exploitation analysis  

The project simulates real-world attack scenarios including:

- Exploit chaining  
- Privilege escalation  
- Full system compromise  

## Key Components

### 1. Advanced Exploitation Lab
- Exploit chaining (**XSS → Session Hijacking → RCE**)  
- Payload customization (PHP reverse shell)  
- Use of Metasploit for exploitation  
- Demonstrated full system compromise  

---

### 2. Web Application Testing
Tested **DVWA** for OWASP Top 10 vulnerabilities.

**Identified:**
- SQL Injection  
- Command Injection  
- Brute Force Authentication Weakness  

**Tools Used:**
- Burp Suite  
- sqlmap  

---

### 3. Reporting Practice
Structured reports including:
- Executive Summary  
- Technical Findings  
- Remediation Plan  

Additional focus:
- Risk-based vulnerability classification  
- Stakeholder-focused communication  

---

### 4. Post-Exploitation
- Privilege escalation to root level  

**Evidence Collected:**
- `/etc/passwd`  
- `/etc/shadow`  
- Network traffic (Wireshark)  

Maintained **chain-of-custody using SHA-256 hashing**.

---

### 5. Capstone Project
- Full penetration testing cycle on target system  

**Critical Vulnerability:**
- Samba Trans2Open Buffer Overflow (**CVE-2003-0201**)  

**Achieved:**
- Remote Code Execution (RCE)  
- Root shell access  
- Complete system compromise  

---

## Tools & Technologies

- Kali Linux  
- Metasploit Framework  
- Burp Suite  
- sqlmap  
- Wireshark  
- Nessus / OpenVAS  
- DVWA / Metasploitable2  

---

## Methodology

This project follows the **Penetration Testing Execution Standard (PTES)**:

1. Reconnaissance  
2. Scanning  
3. Vulnerability Analysis  
4. Exploitation  
5. Post-Exploitation  
6. Reporting  

---

## Key Findings

| ID   | Vulnerability                          | CVE            | Severity | Impact                     |
|------|----------------------------------------|----------------|----------|----------------------------|
| F001 | Samba Remote Code Execution            | CVE-2003-0201  | Critical | Full system compromise     |
| F002 | SQL Injection                          | N/A            | Critical | Database compromise        |
| F003 | Command Injection                      | N/A            | Critical | OS command execution       |
| F004 | Cross-Site Scripting (XSS)             | N/A            | High     | Session hijacking          |
| F005 | Brute Force Authentication Weakness    | N/A            | High     | Unauthorized access        |

## Remediation Highlights

- Implement strict **input validation & output encoding**  
- Use **parameterized queries**  
- Enforce **strong authentication & rate limiting**  
- Secure file uploads and disable execution in upload directories  
- Apply **patch management** and update vulnerable services  
- Deploy **WAF, IDS/IPS monitoring**  

---

## Learning Outcomes

- Developed exploit chaining techniques  
- Customized real-world PoCs  
- Performed manual and automated web testing  
- Created professional penetration testing reports  
- Conducted post-exploitation and forensic evidence handling  

---

## Disclaimer

This project is intended for **educational purposes only**.  

All testing was conducted in controlled lab environments:
- DVWA  
- Metasploitable2  
- VulnHub  

Do not attempt these techniques on unauthorized systems.

---

## Author

**Akash Bangera**  
VAPT Analyst  
