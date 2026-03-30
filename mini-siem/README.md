# 🛡️ Mini SIEM - Log Analysis & Intrusion Detection

## 📌 Overview

This project is a Python-based Mini SIEM (Security Information and Event Management) tool that analyzes authentication logs to detect suspicious activities such as brute-force attacks and unusual login behavior.

---

## 🚀 Features

* 🔍 Log file analysis
* 🚨 Brute-force attack detection
* ⚠️ Suspicious login activity detection
* 📊 CSV report generation
* 🧩 Modular code structure

---

## 🛠️ Technologies Used

* Python
* Regular Expressions (Regex)
* File Handling
* CSV Module

---

## 📁 Project Structure

```
mini-siem/
│
├── main.py
├── analyzer.py
├── utils.py
├── config.py
├── auth.log
├── report.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

```bash
python main.py
```

Then enter:

```
auth.log
```

---

## 📊 Sample Output

```
🚨 Security Report:

⚠️ Brute Force Attack from 192.168.1.10 (5 attempts)

📁 Report saved as report.csv
```

---

## 🧠 Detection Logic

* ≥ 5 failed attempts → Brute Force Attack 🚨
* ≥ 3 failed attempts (no success) → Suspicious ⚠️

---

## 🚀 Future Improvements

* GUI dashboard
* Real-time monitoring
* Data visualization

---

