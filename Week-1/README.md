# 🔐 VAPT Security Assessment – Metasploitable 3

## 📌 Overview

This project presents a comprehensive **Vulnerability Assessment and Penetration Testing (VAPT)** conducted on the Metasploitable 3 environment. The assessment includes vulnerability identification, exploitation, risk evaluation, and remediation strategies based on industry-standard methodologies.

---

## 🎯 Objectives

* Identify security vulnerabilities in the target system
* Exploit identified weaknesses to validate risks
* Assess impact using CVSS scoring
* Provide actionable remediation recommendations
* Document findings in a structured report

---

## 🧠 Scope of Assessment

* **Target System:** Metasploitable 3 VM
* **IP Address:** 192.168.0.127
* **Testing Type:** Black Box Testing
* **Environment:** Controlled Lab Setup

---

## 🛠️ Tools & Technologies

* **Scanning & Enumeration:** Nmap
* **Vulnerability Scanning:** Nessus, Nikto
* **Exploitation:** Metasploit Framework
* **Environment:** Kali Linux, VirtualBox

---

## 🧪 Methodology

The assessment followed a structured VAPT methodology:

1. **Planning**

   * Defined scope, objectives, and rules of engagement

2. **Discovery**

   * Port scanning and service enumeration

3. **Scanning**

   * Identification of vulnerabilities using automated tools

4. **Exploitation**

   * Manual validation of vulnerabilities

5. **Reporting**

   * Documentation of findings, risk, and remediation

---

## 🔍 Findings Summary

| Severity      | Count |
| ------------- | ----- |
| Critical      | 12    |
| High          | 13    |
| Medium        | 20    |
| Low           | 7     |
| Informational | 101   |

---

## 🚨 Key Vulnerabilities

### 🔴 ProFTPD mod_copy Information Disclosure

* **Description:** Allows unauthorized file read/write via mod_copy module
* **CVSS Score:** 9.8 (Critical)
* **Impact:** Sensitive data exposure and system compromise
* **Remediation:** Upgrade to ProFTPD 1.3.5a or later

---

### 🔴 Drupal Coder Module RCE

* **Description:** Deserialization vulnerability enabling remote code execution
* **CVSS Score:** 10.0 (Critical)
* **Impact:** Full system compromise
* **Remediation:** Update/remove vulnerable module

---

### 🟠 SQL Injection (Drupal API)

* **Description:** Improper input validation in database abstraction layer
* **CVSS Score:** 7.5 (High)
* **Impact:** Database manipulation and privilege escalation
* **Remediation:** Upgrade Drupal version

---

### 🟡 SSL Weak Cipher (SWEET32)

* **Description:** Use of weak encryption (3DES)
* **CVSS Score:** 7.5 (High)
* **Impact:** Data interception risk
* **Remediation:** Disable weak cipher suites

---

## 📊 Risk Assessment

* Critical vulnerabilities pose immediate risk and require urgent remediation
* High vulnerabilities may lead to significant compromise
* Medium vulnerabilities assist in attack chaining
* Low and informational findings provide additional attack surface insights

---

## 🛡️ Recommendations

* Upgrade outdated systems (Ubuntu, PHP, ProFTPD)
* Patch all critical and high vulnerabilities immediately
* Disable unnecessary services and open ports
* Enforce secure configurations (firewall, SSL/TLS)
* Implement strong access control and input validation
* Disable IP forwarding if not required
* Apply secure HTTP headers (CSP, X-Frame-Options)

---

## 📚 Standards & Frameworks

* NIST Cybersecurity Framework (CSF)
* ISO/IEC 27001
* PCI-DSS
* GDPR
* HIPAA

---

## 📄 Documentation Tools

* Dradis CE
* CherryTree

---

## 📎 References

* https://www.nist.gov/cyberframework
* https://owasp.org
* https://www.first.org/cvss/
* https://www.kali.org/tools/

---

## 📌 Conclusion

The assessment successfully identified multiple critical and high-risk vulnerabilities within the target system. By applying structured methodologies and industry standards, the project demonstrates practical expertise in vulnerability assessment, exploitation, and risk management.

---

## 👤 Author

**Akash Bangera**
VAPT Intern – CyArt
