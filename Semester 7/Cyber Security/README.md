# 🛡️ Cyber Security (CS-452)

Welcome to the **Cyber Security** course directory! This folder houses comprehensive lecture slides, practical network and web security lab sheets, assignment reports, and coursework outline completed during Semester 7.

The course covers both theoretical security frameworks (governance, risk assessment, policies) and practical hands-on penetration testing and ethical hacking operations.

---

## 📂 Directory Contents

This directory contains the following core files and resources:

*   **📘 Course Information**:
    *   [Course Outline Cybersecurity.docx](./Course%20Outline%20Cybersecurity.docx) — Scope, grading criteria, and textbook mappings.
*   **📑 Lecture Notes & Hands-on Lab Manuals**:
    1.  [1 Intro to CS.pdf](./1%20Intro%20to%20CS.pdf) — Fundamentals of cybersecurity.
    2.  [2 Cybersecurity Frameworks.pdf](./2%20Cybersecurity%20Frameworks.pdf) — ISO 27001, NIST, COBIT.
    3.  [3 Cybersecurity governance.pdf](./3%20Cybersecurity%20governance.pdf) — Enterprise-level security policies.
    4.  [4 Information Risk Assesment.pdf](./4%20Information%20%20Risk%20Assesment.pdf) — Threat analysis and risk scoring.
    5.  [5 The Need for Security .pdf](./5%20The%20Need%20for%20Security%20.pdf) — Legal, ethical, and organizational needs.
    6.  [6 Password authentication.pdf](./6%20Password%20authentication.pdf) — Salting, hashing, multi-factor protocols.
    7.  [7 ARP SPOOFING.pdf](./7%20ARP%20SPOOFING.pdf) — Man-in-the-Middle (MitM) attacks.
    8.  [7 Phishing Spoofingsniffing DoSDDoS.pdf](./7%20Phishing%20Spoofingsniffing%20DoSDDoS.pdf) — Social engineering and flooding.
    9.  [8 DHCP Spoofing .pdf](./8%20%20%20DHCP%20Spoofing%20.pdf) — Rogue DHCP server attacks.
    10. [9 DNS Attack.pdf](./9%20DNS%20Attack.pdf) — Cache poisoning, spoofing, and hijacking.
    11. [10 Database Security.pdf](./10%20Database%20Security.pdf) — SQL authorization and DB hardening.
    12. [11 BURP SUIT.pdf](./11%20BURP%20SUIT.pdf) — Introduction to web proxies.
    13. [12 SQL injection using burp suit.pdf](./12%20SQL%20injection%20using%20burp%20suit.pdf) — Vulnerability scanning and automated exploitation.
    14. [13 HTTP HTTPS cookies.pdf](./13%20HTTP%20HTTPS%20cookies.pdf) — Session states and secure/HttpOnly cookies.
    15. [14 XSS Attack.pdf](./14%20XSS%20Attack.pdf) — Stored, Reflected, and DOM-based Cross-Site Scripting.
    16. [15 XSRF.pdf](./15%20XSRF.pdf) — Cross-Site Request Forgery and mitigation.
    17. [16 Mobile device Security.pdf](./16%20%20Mobile%20device%20Security.pdf) — OWASP mobile top-10 and sandboxing.
*   **🖊️ Academic Assignments & Lab Reports**:
    *   [Abubakar(41)_Cyber_Security_Assignment#01.pdf](./Abubakar(41)_Cyber_Security_Assignment%2301.pdf) — Initial research paper focusing on threat assessment and cybersecurity principles.
    *   [Abubakar(41)_Cyber_Security_Assignment#02.pdf](./Abubakar(41)_Cyber_Security_Assignment%2302.pdf) — Hands-on penetration testing tasks, network spoofing simulation results, and analysis.
    *   [Abubakar(41)_Assignment03_Cybersecurity.pdf](./Abubakar(41)_Assignment03_Cybersecurity.pdf) — Advanced vulnerability assessment report detailing web exploits (XSS, SQLi, and CSRF protection mechanisms).
*   **🔑 Digital Cryptography Reference Framework**:
    *   [Digital_Signature_Validator_Framework.pdf](./Digital_Signature_Validator_Framework.pdf) — Detailed design guidelines and analysis of public-key cryptographic validator engines.
    *   🔗 **[Certea GitHub Repository](https://github.com/abubakarp789/Certea)** — Official implementation repository of the digital signature validator and verification system.

---

## 🛠️ Main Tech & Tools Explored

```text
  ┌──────────────────────────────────────────────────────────┐
  │                        BURP SUITE                        │
  │  Used as an HTTP proxy to intercept, edit, and replay     │
  │  client-server requests, enabling secure analysis.       │
  └──────────────────────────┬───────────────────────────────┘
                             │
       ┌─────────────────────┼─────────────────────┐
       ▼                     ▼                     ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  SQL Map &   │      │  Wireshark   │      │     DVWA     │
│ SQL Injections│     │   Packet     │      │  (Dam Vulner-│
│ (Exploitation)│     │  Analysis    │      │  able Web Ap)│
└──────────────┘      └──────────────┘      └──────────────┘
```

---

## 🧠 Core Competencies Achieved

### 1. Network Vulnerability Exploitation
*   **ARP Spoofing**: Simulating Man-in-the-Middle (MitM) attacks inside local subnets to capture cleartext traffic.
*   **DHCP Spoofing**: Setting up rogue DHCP servers to poison client gateway entries.
*   **DNS Attacks**: Cache poisoning simulations redirecting target domains to malicious endpoints.

### 2. Web Application Security (OWASP Top 10)
*   **SQL Injection (SQLi)**: Triggering boolean, time-based, and union-based injections on database queries via custom inputs and proxy modification tools.
*   **Cross-Site Scripting (XSS)**: Injecting malicious scripts (JavaScript payloads) into database entries (stored XSS) and input parameters (reflected XSS).
*   **Cross-Site Request Forgery (CSRF)**: Forging requests from authenticated user sessions and designing secure anti-CSRF token verification filters.

### 3. Enterprise Security & Cryptography
*   **Framework Compliance**: Practical study of NIST, ISO 27001, and COBIT frameworks for corporate risk management.
*   **Digital Signatures**: Understood asymmetric cryptography (RSA, ECC), public-key validation infrastructure, and hashing (SHA-256).

---

*Note: All offensive security tools, scripts, and analyses were executed strictly in isolated sandboxes and local virtual machines for educational and research purposes.*
