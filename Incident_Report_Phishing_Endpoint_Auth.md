# Security Incident Report

## Incident Title
Phishing-Led Account Compromise and Suspicious Endpoint Activity

## Incident ID
SOC-INC-001

## Date Identified
2025-01-12

## Reported By
Security Operations Center (SOC)

## Severity
High

## Incident Status
Resolved

---

## Executive Summary
The Security Operations Center identified a confirmed security incident involving a phishing email that resulted in user interaction with a malicious link. Subsequent investigation revealed malicious DNS activity, suspicious endpoint execution using encoded PowerShell commands, and anomalous authentication activity originating from a high-risk geographic location. Correlation of multiple telemetry sources confirmed malicious behavior and elevated the incident to high severity.

---

## Incident Description
The incident began with the delivery of a phishing email containing a malicious attachment and embedded URL. The affected user interacted with the email, resulting in DNS resolution to a known malicious domain. Shortly after, encoded PowerShell execution was observed on the user endpoint, indicating possible post-phishing exploitation. Authentication logs further revealed a successful login attempt from a foreign location following multiple failed attempts, suggesting potential credential compromise.

---

## Incident Timeline
2025-01-12 08:30 – Phishing email delivered to user mailbox  
2025-01-12 10:15 – DNS query observed to malicious domain  
2025-01-12 10:18 – Encoded PowerShell execution detected on endpoint  
2025-01-10 02:18 – Successful authentication from high-risk geographic location  

---

## Affected Assets
User Account: user@company.com  
Endpoint Hostname: host-01  
Source IP Address: 185.220.101.4  

---

## Indicators of Compromise (IOCs)
Malicious Domains:
- malicious-site.com
- phish-login.com

Suspicious IP Address:
- 185.220.101.4

Malicious Attachment:
- invoice.zip

Suspicious Process:
- powershell.exe with encoded command execution

---

## Detection and Analysis
The incident was detected through multiple SOC detections, including phishing analysis of email metadata, DNS monitoring for suspicious domain resolution, endpoint monitoring identifying encoded PowerShell execution, and authentication log analysis highlighting anomalous login behavior from a high-risk geographic region. The correlation of these events across email, network, endpoint, and authentication logs confirmed malicious activity and warranted escalation to a high-severity incident.

---

## Response Actions Taken
The phishing email was removed from the affected user mailbox and malicious domains were blocked at email and network gateways. The affected user credentials were reset, and the endpoint was isolated for further investigation and malware scanning. Indicators of compromise were documented and shared with security teams to enhance detection coverage.

---

## MITRE ATT&CK Mapping
T1566.001 – Phishing: Attachment  
T1078 – Valid Accounts  
T1059.001 – Command and Scripting Interpreter: PowerShell  
T1105 – Ingress Tool Transfer  

---

## Lessons Learned and Recommendations
Email filtering rules should be enhanced to improve detection of HTML and ZIP-based phishing attachments. Authentication monitoring should continue to focus on foreign login attempts and impossible travel scenarios. Additional user security awareness training is recommended to reduce phishing risk.

---

## Prepared By
Sai Chetan Panathukula
Security Analyst | SOC (L1 - L2) | Blue Team Analyst
