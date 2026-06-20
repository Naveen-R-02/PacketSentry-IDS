# PacketSentry IDS

PacketSentry IDS is a Python-based Intrusion Detection System (IDS) that detects SYN-based port scanning attacks in real time. The system captures network traffic using Scapy, analyzes scanning behavior, classifies attack severity, stores alerts in SQLite, and visualizes attack data through an interactive Flask dashboard.

---

## Features

- Real-time packet monitoring using Scapy
- SYN scan detection
- Severity classification (LOW, MEDIUM, HIGH, CRITICAL)
- SQLite-based alert logging
- Flask web dashboard
- Severity distribution chart
- Top attacker identification
- Attack history tracking
- Session-based scan detection

---

## Severity Levels

| Ports Scanned | Severity |
|--------------|----------|
| 1 – 9 | LOW |
| 10 – 19 | MEDIUM |
| 20 – 49 | HIGH |
| 50+ | CRITICAL |

---

## System Architecture

```text
Attacker
   │
   ▼
TCP SYN Scan
   │
   ▼
Packet Capture (Scapy)
   │
   ▼
Detection Engine
   │
   ├── Port Tracking
   ├── Severity Analysis
   └── Alert Generation
   │
   ▼
SQLite Database
   │
   ▼
Flask Dashboard
```

---

## Project Structure

```text
PacketSentry/
│
├── app.py
├── detector.py
├── packet_capture.py
├── database.py
│
├── templates/
│   └── dashboard.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── screenshots/
│   ├── dashboard.png
│   ├── terminal-alert.png
│   └── severity-chart.png
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Flask
- Scapy
- SQLite3
- HTML5
- CSS3
- JavaScript
- Chart.js

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/PacketSentry-IDS.git
cd PacketSentry-IDS
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run PacketSentry

```bash
sudo python3 app.py
```

---

## Testing

Run an Nmap SYN scan against a target machine:

```bash
nmap -sS -p 1-30 <target-ip>
```

Example:

```bash
nmap -sS -p 1-30 192.168.1.100
```

PacketSentry will:

- Capture SYN packets
- Detect scan activity
- Count scanned ports
- Assign severity
- Store alerts
- Display results on the dashboard

---

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Attack History

![Attack History](screenshots/severity-chart.png)

### Terminal Alert

![Terminal Alert](screenshots/terminal-alert.png)

---

## Example Detection Output

```text
=================================
[FINAL ALERT REPORT]

Attacker IP : 10.135.145.192
Ports Scanned : 30
Severity : HIGH
Timestamp : 2026-06-20 10:30:15

=================================
```

---

## Learning Outcomes

This project demonstrates practical knowledge of:

- Network Packet Analysis
- Intrusion Detection Systems (IDS)
- Real-Time Threat Monitoring
- Python Security Automation
- Flask Web Development
- SQLite Database Management
- Cybersecurity Event Analysis

---

## Future Enhancements

- GeoIP Mapping
- Email Alerts
- Threat Intelligence Integration
- Machine Learning-Based Detection
- Distributed IDS Architecture
- SIEM Integration

---

## Disclaimer

PacketSentry is an educational IDS prototype developed for learning and demonstration purposes. Normal network traffic may occasionally be classified as low-severity scan activity because detection is based primarily on TCP SYN packet analysis and port diversity.

---

## Author

**Naveen R**

BCA  – Cyber Security

Aspiring SOC Analyst | Python Developer | Network Security Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
