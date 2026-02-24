# 🦚 KrishnAI  
### Ancient Wisdom. Modern Guidance.

KrishnAI is a **responsive, AI-powered student guidance web application** developed as an **MCA Minor Project**.  
The application helps students deal with academic stress, confusion, and lack of motivation using a **Krishna-inspired AI chatbot** powered by **Groq AI**, with guidance explained in simple, modern language.

---

## 📌 Problem Statement
Students often experience stress, confusion, and self-doubt during their academic journey. Most existing systems provide generic answers without emotional depth or ethical grounding. KrishnAI addresses this problem by combining **Artificial Intelligence** with **timeless philosophical wisdom** to guide students in a meaningful and practical way.

---

## 🎯 Objectives
- To provide AI-based emotional and academic guidance to students  
- To help students manage stress and confusion effectively  
- To integrate philosophical wisdom with modern AI technology  
- To build a secure, login-based personalized guidance platform  

---

## ✨ Key Features
- 🔐 Secure login and signup system  
- 🤖 Krishna-inspired AI chatbot using Groq AI  
- 📘 Daily Bhagavad Gita shloka with meaning and explanation  
- 📝 Personal reflection journal for students  
- 📊 Dashboard for easy navigation  
- 🎨 Fully responsive and modern UI design  
- 🦚 Custom logo and consistent branding  

---

## 🧩 Application Modules

### 🧭 Dashboard
Acts as the central navigation hub where users can access all features of the application after login.

### 🤖 Chat with Krishna
Allows students to interact with the AI chatbot to seek guidance related to stress, fear, confusion, motivation, and academic challenges.

### 📘 Daily Wisdom
Displays a Bhagavad Gita shloka each day along with its meaning and a student-friendly explanation to provide daily motivation and clarity.

### 📝 Reflections
Enables students to write and store personal reflections, helping them track thoughts, emotions, and personal growth over time.

### ℹ️ About
Explains the purpose of the system, technologies used, and the role of each module.

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **AI Engine:** Groq AI (LLaMA 3.1 model)  
- **Database:** SQLite  
- **Authentication:** Flask-Login  
- **Frontend:** HTML, CSS (Responsive Design)  
- **Version Control:** Git  

---

## 🗂️ Project Structure
```bash
krishnai/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── models/
│ ├── user.py
│ ├── chat.py
│ └── reflection.py
│
├── services/
│ ├── groq_service.py
│ ├── krishna_prompt.py
│ └── shloka_service.py
│
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── signup.html
│ ├── dashboard.html
│ ├── chat.html
│ ├── daily_shloka.html
│ ├── reflection.html
│ └── about.html
│
├── static/
│ ├── style.css
│ └── images/
│ └── logo.jpg
│
└── venv/


```bash
---

## ⚙️ Setup Instructions
```bash
### 1️⃣ Clone the Repository

git clone <repository-url>
cd krishnai
2️⃣ Create & Activate Virtual Environment
bash

python -m venv venv
venv\Scripts\Activate   # Windows
3️⃣ Install Dependencies
bash

pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file (not committed to Git):

env

GROQ_API_KEY=your_groq_api_key_here
5️⃣ Run the Application
bash

python app.py
Open in browser:


http://127.0.0.1:5000
🎨 UI & Responsiveness
Fully responsive layout using flexible containers and CSS media queries

Mobile, tablet, and desktop friendly

Hover effects with color transition and sky-blue shadow for better UX

Clean, academic, and professional design

🔐 Security Practices
Passwords stored using hashing (Werkzeug)

API keys stored in environment variables

Sensitive files excluded using .gitignore

Protected routes using Flask-Login

📈 Future Enhancements
Mood-based chatbot personalization

Analytics dashboard for student well-being

Multilingual support

Mobile application version

🌱 Project Slogan
🦚 Ancient Wisdom. Modern Guidance.

