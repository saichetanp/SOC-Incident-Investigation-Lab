# Security Incident Report

## Incident Title
Phishing-Led Account Compromise and Endpoint Execution

## Incident ID
SOC-INC-001

## Date Identified
2025-01-12

## Reported By
Security Operations Center (SOC)

## Severity
High

---

## Executive Summary
The Security Operations Center identified a confirmed security incident involving a phishing email that led to user interaction with a malicious link, suspicious DNS activity, endpoint execution of encoded PowerShell commands, and anomalous authentication activity from a high-risk geographic location. Correlation across email, DNS, endpoint, and authentication logs confirmed malicious activity and elevated the incident severity.

---

## Incident Timeline
- **2025-01-12 08:30** – Phishing email delivered with malicious attachment and URL  
- **2025-01-12 10:15** – DNS query observed to known malicious domain  
- **2025-01-12 10:18** – Encoded PowerShell execution detected on endpoint  
- **2025-01-10 02:18** – Successful authentication from foreign location following failed attempts  

---

## Affected Assets
- User Account: `user@company.com`  
- Endpoint: `host-01`  
- Source IP: `185.220.101.4`  

---

## Indicators of Compromise (IOCs)
- Malicious Domains:
  - malicious-site.com
  - phish-login.com
- Suspicious IP Address:
  - 185.220.101.4
- Malicious Attachment:
  - invoice.zip
- Suspicious Process:
  - powershell.exe (encoded execution)

---

## Detection & Analysis
The incident was detected through multiple SOC detections, including phishing analysis of email metadata, DNS log monitoring for suspicious domain resolution, endpoint monitoring for encoded PowerShell execution, and authentication log analysis identifying a successful login from a high-risk geographic region. The combination of these signals confirmed malicious activity and warranted escalation.

---

## Response Actions
- Phishing email removed from user mailbox  
- Malicious domains blocked at email and network gateways  
- Affected user credentials reset  
- Endpoint isolated and scanned  
- Indicators shared with detection and threat intelligence teams  

---

## MITRE ATT&CK Mapping
- **T1566.001** – Phishing: Attachment  
- **T1078** – Valid Accounts  
- **T1059.001** – Command and Scripting Interpreter: PowerShell  
- **T1105** – Ingress Tool Transfer  

---

## Lessons Learned
- Email filtering rules updated to better detect HTML and ZIP attachments  
- Enhanced alerting for foreign authentication activity  
- User phishing awareness training recommended  

---

## Incident Status
Resolved

---

## Prepared By
Sai Chetan Panathukula
