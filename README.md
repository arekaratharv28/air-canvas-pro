# 🎨 Air Canvas Pro: AR Gesture Interface
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0-green)
![DevOps](https://img.shields.io/badge/DevOps-CI%2FCD-orange)
![Deployment](https://img.shields.io/badge/Deployment-Render-purple)

**A futuristic, gesture-controlled Augmented Reality drawing tool. Features real-time hand tracking, depth-based brush sizing, and a Flask backend for cloud storage. Deployed via CI/CD on Render.**

---

## 📋 Experiment Context
[cite_start]**Aim:** Develop a web application and deploy on GitHub to study DevOps: Principles, Practices, and DevOps Engineer Role and Responsibilities. 

This project fulfills the experiment requirements by implementing:
* **Version Control:** Git & GitHub for source code management.
* **Continuous Delivery (CD):** Automated deployment pipeline connected to Render.
* **Infrastructure as Code:** Dependency management via `requirements.txt`.
* **Automation:** Real-time Client-Server communication without manual intervention.

---

## 🚀 Key Features
* **👆 Gesture Control:** "Pinch" (Index + Thumb) to draw; release to hover.
* **📏 Spatial Depth Sensing:** Brush size dynamically adjusts based on your hand's distance from the camera (Z-axis emulation).
* **💾 Cloud Archiving:** Sketches are serialized and sent to a Python (Flask) backend for permanent storage.
* **🕶️ Futuristic HUD:** A "Minority Report" style interface with glassmorphism UI and neon accents.
* **📱 Responsive:** Optimized for both Desktop and Mobile (Samsung S25 Ultra / iPhone) via NPU acceleration.

---

## 🛠️ Tech Stack
* **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6)
* **AI/ML Engine:** Google MediaPipe Hands (Client-Side)
* **Backend:** Python (Flask)
* **Deployment:** Render (PaaS)
* **Version Control:** Git

---

## 📂 Project Structure
```bash
flask-air-canvas/
├── .gitignore          # Prevents user data/artifacts from being pushed
├── app.py              # Flask Backend Server
├── requirements.txt    # Dependency list for Cloud Build
└── templates/
    └── index.html      # AR Interface (Frontend)