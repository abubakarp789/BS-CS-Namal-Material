# 🎓 BS-CS-Namal-Material

[![Namal University](https://img.shields.io/badge/University-Namal%20University-blue?style=for-the-badge&logo=education)](https://www.namal.edu.pk/)
[![Degree](https://img.shields.io/badge/Degree-BS%20Computer%20Science-darkgreen?style=for-the-badge)](https://www.namal.edu.pk/)
[![Semesters](https://img.shields.io/badge/Semesters-Semester%207%20%26%208-orange?style=for-the-badge)](./Semester%208/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Welcome to my academic repository! This repository serves as a comprehensive, structured archive of all labs, programming assignments, projects, exam study guides, and research materials that I have completed during my **Bachelor of Science in Computer Science (BS CS)** degree at **Namal University Mianwali**. 

The goal of this repository is to track my academic progression, showcase from-scratch implementations of complex computer science concepts (ranging from Machine Learning algorithms to distributed container orchestrations and Transformer models), and act as a detailed reference for junior students, recruiters, and peers.

---

## 📂 Repository Architecture

Below is the directory map of the repository, categorized by semester and coursework. You can click on any folder or course to view its dedicated documentation and code implementations.

```mermaid
graph TD
    Root[BS-CS-Namal-Material] --> Sem7["📅 Semester 7"]
    Root[BS-CS-Namal-Material] --> Sem8["📅 Semester 8"]
    
    Sem7 --> CS["🛡️ Cyber Security"]
    Sem7 --> EN["💼 Entrepreneurship"]
    Sem7 --> IQ["📖 Iqbaliyat"]
    Sem7 --> ML["🤖 Machine Learning"]
    Sem7 --> PDC["💻 Parallel & Distributed Computing"]
    
    EN --> FYP["💡 Project: SudhaarAI Business Plan"]
    IQ --> IQP["🕌 Project: Tariq ki Dua Study"]
    ML --> MLA["✍️ 5 From-Scratch Assignments"]
    PDC --> PDCA["🔧 2 Code Optimizations"]
    PDC --> PDCT["🐳 Docker Scaling & Nginx Lab"]
    PDC --> PDCP["📚 Exam & Quiz Guides"]

    Sem8 --> NLP["🔤 Natural Language Processing"]
    Sem8 --> PPE["⚖️ Professional Practice & Ethics"]
    Sem8 --> WAD["🌐 Web Application Development"]

    NLP --> NLPA["🤖 BERT, ELMo, RoBERTa, XLNet & Blueprints"]
    PPE --> PPEA["📚 HBR Business Writing & SudhaarAI Presentation"]
    WAD --> WADA["💻 MERN Stack, MongoDB, & Student Portal Vite App"]
```

---

## 🗂️ Semester Directory Directory

### 📅 [Semester 7](./Semester%207/README.md)
*Focus: Security, AI/ML, Parallel Architectures, Iqbal's Philosophy, and Business Planning.*

| Course | Code / Type | Key Deliverables & Projects | Documentation |
| :--- | :---: | :--- | :---: |
| **🤖 Machine Learning** | CS-341 | KNN, K-Means, DBSCAN, Linear Regression, LDA, PCA, and LSTM *from scratch* (no sklearn/keras!). | [Explore](./Semester%207/Machine%20Learning/) |
| **💻 Parallel & Distributed Computing** | CS-440 | **[Multi-User Remote Access System](https://github.com/abubakarp789/Multi-User-Remote-Access-System)**, Docker Compose Scaling, Load Balancing (Nginx), and Algorithm Optimizations. | [Explore](./Semester%207/Parallel%20and%20Distributed%20Computing/) |
| **🛡️ Cyber Security** | CS-452 | **[Certea Signature Validator](https://github.com/abubakarp789/Certea)**, Burp Suite Labs, SQL Injections, XSS & XSRF Attacks, and Network Spoofing. | [Explore](./Semester%207/Cyber%20Security/) |
| **💼 Entrepreneurship** | CS-363 | **SudhaarAI**: A complete Software Requirements Specification (SRS) and comprehensive business venture plan. | [Explore](./Semester%207/Entrepreneurship/) |
| **📖 Iqbaliyat** | SS-102 | Poetic and philosophical exploration of Allama Iqbal's "Tariq ki Dua", containing research reports and certificate work. | [Explore](./Semester%207/Iqbaliyat/) |

### 📅 [Semester 8](./Semester%208/README.md)
*Focus: Natural Language Processing (Transformers), Professional Ethics & Leadership, and Full-Stack Web Application Development (MERN Stack).*

| Course | Code / Type | Key Deliverables & Projects | Documentation |
| :--- | :---: | :--- | :---: |
| **🔤 Natural Language Processing** | CS-442 | Vector Semantics, Word Embeddings, Attention, Transformers (**BERT, RoBERTa, XLNet**), & **[Urdu Tweets Classifier Repo](https://github.com/abubakarp789/Robust-Sentiment-and-Emotion-Classification-on-Noisy-Urdu-Tweets)**. | [Explore](./Semester%208/NLP/) |
| **⚖️ Professional Practice & Ethics** | CS-490 | IEEE/ACM Ethics, HBR Business Writing Manuals, Personal Branding, CV Portfolio, and **SudhaarAI Product Ethics**. | [Explore](./Semester%208/PPE/) |
| **🌐 Web Application Development** | CS-450 | MERN Stack, **[Rumi House Hub](https://github.com/abubakarp789/Rumi-House-Hub)**, **[WAD-Assignments](https://github.com/abubakarp789/WAD-Assignments)**, **[WAD-Tasks](https://github.com/abubakarp789/WAD-Tasks)**, and Express APIs. | [Explore](./Semester%208/WAD/) |

---

## 🚀 Key Highlights & Major Projects

### 🌟 [SudhaarAI — Generative AI Code Assistant](./Semester%207/Entrepreneurship/FYP%20Business%20Plan/)
A comprehensive business plan and SRS for an advanced AI-powered software assistant that optimizes legacy code and provides real-time contextual enhancements. 
* *Technologies/Methods: Business Strategy, Venture Finance, SRS, System Design.*

### 💻 [Multi-User Remote Access System (PDC Project)](https://github.com/abubakarp789/Multi-User-Remote-Access-System)
A high-performance concurrent client-server framework enabling remote command execution and access coordination across multiple concurrent users over TCP/UDP channels.
* *Technologies: Python, Concurrency, Socket Programming, Multiprocessing, TCP/UDP.*

### 🛡️ [Certea — Digital Signature Validator (Cyber Security Project)](https://github.com/abubakarp789/Certea)
Official implementation of a cryptographic digital signature validator and verification system designed to validate file authenticity using public-key infrastructure.
* *Technologies: Cryptography, Digital Signatures, PKI, Security Verification.*

### 🔤 [Noisy Urdu Tweet Sentiment & Emotion Classifier (NLP Project)](https://github.com/abubakarp789/Robust-Sentiment-and-Emotion-Classification-on-Noisy-Urdu-Tweets)
Fine-tuning and benchmarking Transformer architectures (BERT, RoBERTa, XLNet, ELMo) and vector embeddings for sentiment and emotion classification on noisy Roman/Urdu tweet corpora.
* *Technologies: PyTorch, Transformers, BERT, RoBERTa, XLNet, Word Embeddings, NLP.*

### 🌐 [Rumi House Hub — Student Operations Portal (WAD Project)](https://github.com/abubakarp789/Rumi-House-Hub)
A full-stack MERN portal unifying student engagement, society enrollments, event proposal workflows, dynamic seat RSVPs, and digital QR gate attendance verification.
* *Technologies: React, Vite, Node.js, Express.js, MongoDB, JWT, Tailwind CSS, REST APIs.*

### 🐳 [Docker Compose Load Balancing & Scaling Lab](./Semester%207/Parallel%20and%20Distributed%20Computing/Task/)
A highly efficient, scalable system demonstrating Flask application load-balancing behind an Nginx reverse proxy. It scales dynamically and computes task speedups, evaluating the efficiency gains through Amdahl's Law.
* *Technologies: Docker, Docker Compose, Nginx, Python, Flask.*

### 🧠 [Machine Learning Algorithms From Scratch](./Semester%207/Machine%20Learning/)
Five massive homework assignments where core machine learning components were coded strictly using base Python and Numpy:
1. **Clustering & Classification**: K-Means, DBSCAN (density-based clustering), and KNN (k-Nearest Neighbors).
2. **Regression Analysis**: Outlier analysis and loss metrics (MSE vs. MAE) in custom Linear Regression models.
3. **Linear Discriminant Analysis (LDA)**: High-dimensional class projection and classification from scratch.
4. **Principal Component Analysis (PCA)**: Eigenvector breakdown, covariance computations, and 3D data projection.
5. **LSTM RNN**: Deep Recurrent Neural Network built with gated cell states, custom learning rates, and gate-state visualizations.

---

## 🛠️ Tech Stack & Skills Acquired

* **Languages**: Python, JavaScript (ES6+), C++, SQL, HTML5/CSS3, Bash, Markdown, LaTeX
* **AI/ML & NLP**: Transformers, BERT, RoBERTa, XLNet, Word Embeddings (Word2Vec/GloVe), LSTM, Neural Networks, PCA, LDA, Clustering, Regression
* **Web Development & MERN Stack**: React.js, Vite, Node.js, Express.js, MongoDB, RESTful APIs, Bootstrap 5
* **DevOps & Distributed Systems**: Docker, Docker Compose, Nginx, Load Balancing, Parallel Multiprocessing
* **Cybersecurity**: Burp Suite, Network Spoofing (ARP/DHCP), Cryptography, SQLi, Cross-Site Scripting (XSS), CSRF
* **Soft Skills & Governance**: Professional Practice & Computing Ethics (IEEE/ACM), HBR Business Writing, Startup Modeling, Pitch Presentations, Technical Writing (SRS)

---

## Author

**Abu Bakar Panhwar**<br>
BS Computer Science, Namal University Mianwali<br>
Registration number: `NUM-BSCS-2022-41`<br>
Email: [abubakarp789@gmail.com](mailto:abubakarp890@gmail.com)<br>
GitHub: [@abubakarp789](https://github.com/abubakarp789)

---

## 🤝 How to Use This Repo

Feel free to browse through the folders to inspect course materials, scripts, and reports:
1. Every major directory contains a README detail outlining its contents.
2. Code files are ready to run (ensure dependencies are installed using `uv pip install` or `pip install` as listed in individual READMEs).
3. Review sheets and course outlines are structured inside each directory for easy reference.

---

*Made with 🎓 and 💻 by Abubakar — Namal University.*
