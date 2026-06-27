# 🌍 AI Language Translation Tool

An AI-powered Flask web application that supports text translation, OCR text extraction, PDF translation, and grammar correction using intelligent NLP libraries.

# 📌 Project Overview

The AI Language Translation Tool is a full-stack web application built using Flask that allows users to translate text between multiple languages along with advanced features like OCR (image-to-text extraction), PDF translation, and grammar correction.

The system stores all translation history in a SQLite database and provides an analytics dashboard to track usage patterns such as total translations, OCR usage, PDF translations, and grammar checks.

This project demonstrates how AI and NLP libraries can be integrated into a web application to build a smart multilingual communication system.

# 🎯 Objective

The main objective of this project is:
```text
🌐 To break language barriers by providing instant translation between multiple languages
🖼 To extract text from images using OCR technology
📄 To translate PDF documents efficiently
🤖 To improve writing quality using AI-based grammar correction
📊 To track and analyze user activity using a dashboard
💾 To store translation history for future reference
🧠 To integrate AI/NLP tools into a real-world web application
```
# 🚀 Features
```text
✨ Text Translation (Multi-language support)
🖼 OCR Image Text Extraction
📄 PDF Text Translation
🤖 AI Grammar Correction (TextBlob)
📜 Translation History with SQLite Database
📊 Analytics Dashboard (usage tracking)
🎨 Modern responsive UI (Bootstrap + Custom CSS)
```
# 🧠 Tech Stack
```text
Backend
Python 🐍
Flask
SQLite3
AI / NLP
deep-translator (GoogleTranslator)
TextBlob
Frontend
HTML5
CSS3
Bootstrap 5
JavaScript
```
# 📂 Project Structure

```text
Language_Translation_Tool_Project/
│
├── app.py
├── translator.db
├── requirement.txt
──  database.db
│
├── templates/
│   ├── home.html
│   ├── dashboard.html
│   ├── translator.html
│   ├── history.html
│   ├── ocr.html
│   ├── pdf.html
│   ├── grammar.html
│   └── analytics.html
│
├── static/
│   └── style.css
│
└── README.md
```

# ⚙️ Installation & Setup

1️⃣ Clone Repository

git clone https://github.com/gayatrichandgude/Language_Translation_Tool_Project.git

cd Language_Translation_Tool_Project

2️⃣ Create Virtual Environment (Optional)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirement.txt

4️⃣ Run Flask App
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/

# 📊 Database (SQLite)
```text
history table
id
source_text
translated_text
source_lang
target_lang
created_at
type
```
# 🧪 Modules Explained

🌍 Translator
Uses GoogleTranslator
Supports multiple languages

🖼 OCR Module
Extracts text from images using OCR

📄 PDF Translator
Extracts and translates PDF content

🤖 Grammar Checker
Uses TextBlob for grammar correction

📊 Analytics
Tracks:
Total translations
OCR usage
PDF usage
Grammar usage

# 📈 Future Improvements

🔐 User authentication system
🎤 Voice translation feature
☁ Cloud database integration
📱 Mobile responsive PWA
🌐 Better AI translation APIs

👩‍💻 Author

Gayatri Chandgude

📧 Email: chandgudegayatri@gmail.com

GitHub: https://github.com/gayatrichandgude

📌 License

This project is for educational purposes.
