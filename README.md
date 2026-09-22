# 🛡️ Local Network Security Scanner

### Python • Nmap • Flask

A beginner-friendly **defensive cybersecurity tool** for network reconnaissance, open port discovery and service detection.

---

## 📌 About The Project

**Local Network Security Scanner** is a Python-based cybersecurity project developed to understand the fundamentals of network reconnaissance through practical implementation.

The application uses **Nmap** as its scanning engine and **Flask** to provide a web-based interface.

The scanner can:

* Validate target IP addresses
* Check whether a host is reachable
* Discover open TCP ports
* Detect running services
* Identify service versions using Nmap
* Parse Nmap output with Python
* Display scan results through a web interface

The project is designed for **cybersecurity learning and authorized defensive testing**.

---

## 🖥️ Application

The scanner provides a modern web interface where an authorized target IP can be entered and scanned.

### SENTINEL Dashboard

<img width="1325" height="627" alt="image" src="https://github.com/user-attachments/assets/5c71b539-1205-430f-b805-497eb670c1be" />

<img width="1321" height="620" alt="image" src="https://github.com/user-attachments/assets/7ec7931f-b58d-4971-87e1-e2a81f3424e6" />

<img width="1201" height="638" alt="image" src="https://github.com/user-attachments/assets/7a69c85d-335e-4b2b-b683-4f12463601f0" />


The interface displays:

* 🎯 Target IP
* 🟢 Host status
* 🚪 Open ports
* 🌐 Protocol
* ⚙️ Detected services
* 📡 Scan status

---

## 🔍 How It Works

```text
User
  ↓
SENTINEL Web Interface
  ↓
Flask
  ↓
Python Scanner
  ↓
Nmap
  ↓
Target System
  ↓
Scan Results
  ↓
Web Interface
```

---

## 🧠 What I Learned

While developing this project, I practiced and connected several fundamental cybersecurity concepts.

### Networking

* IP addresses
* `localhost`
* Loopback address
* TCP
* Ports
* Services
* Host availability

### Nmap

* Basic network scanning
* Host discovery
* Open port detection
* Service detection
* Nmap output interpretation

### Python

* `subprocess`
* `ipaddress`
* Input validation
* Functions
* Lists and dictionaries
* Parsing command-line output

### Flask

* Routes
* HTTP requests
* JSON
* API endpoints
* Frontend/backend communication

---

## 🛠️ Technologies

| Technology   | Purpose              |
| ------------ | -------------------- |
| 🐍 Python    | Scanner logic        |
| 🔎 Nmap      | Network scanning     |
| 🌐 Flask     | Backend and API      |
| HTML         | Web interface        |
| CSS          | Interface design     |
| JavaScript   | Frontend interaction |
| Git & GitHub | Version control      |

---

## 📁 Project Structure

```text
local-network-security-scanner/
│
├── app.py
├── scanner.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── app.js
│
└── screenshots/
    └── sentinel-dashboard.png
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ulcnzey/local-network-security-scanner.git
cd local-network-security-scanner
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows

```powershell
venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Make sure Nmap is installed

```bash
nmap --version
```

---

## ▶️ Run the Application

Start Flask:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Enter an authorized target such as:

```text
127.0.0.1
```

and click **SCAN TARGET**.

---

## 🧪 Example Result

Example scan result:

```text
Target: 127.0.0.1
Status: UP

Open Ports:

Port: 80
Protocol: TCP
State: open
Service: http

Port: 3306
Protocol: TCP
State: open
Service: mysql

Port: 5432
Protocol: TCP
State: open
Service: postgresql
```

Actual results depend on the services running on the target system.

---

## 🔐 Ethical Use

This project is intended for **defensive security learning and authorized testing**.

Only scan:

* Your own systems
* Your own laboratory environments
* Systems for which you have explicit authorization

> ⚠️ An open port does not automatically mean that a system is vulnerable. Port discovery is an initial reconnaissance step and should be followed by further security analysis.

---

## 🎯 Current Status

**Version:** `v1.0`

**Status:** 🟢 Working

The first functional version of the scanner has been completed with Python, Nmap and Flask.

Future development can build upon this foundation with deeper security analysis and reporting capabilities.

---

## 👩‍💻 Author

**Zeynep Ulucan**

Adli Bilişim Mühendisliği Student
Cybersecurity Learning & Development
