from flask import Flask, render_template, request, redirect, flash
from deep_translator import GoogleTranslator
import sqlite3
from datetime import datetime
import requests
from flask import session, redirect
from textblob import TextBlob

app = Flask(__name__)
app.secret_key = "translator123"

users = []


def init_db():
    conn = sqlite3.connect("translator.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_text TEXT,
            translated_text TEXT,
            source_lang TEXT,
            target_lang TEXT,
            created_at TEXT,
            type TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

def table_exists(table_name):
    conn = sqlite3.connect("translator.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name=?
    """, (table_name,))

    result = cur.fetchone()
    conn.close()

    return result is not None
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect("translator.db")
    cur = conn.cursor()

    # Total
    cur.execute("SELECT COUNT(*) FROM history")
    total = cur.fetchone()[0]

    # Languages (REAL unique)
    cur.execute("SELECT COUNT(DISTINCT source_lang || target_lang) FROM history")
    languages = cur.fetchone()[0]

    # Today
    cur.execute("SELECT COUNT(*) FROM history WHERE created_at = date('now')")
    today = cur.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        languages=languages,
        today=today
    )
    
@app.route('/translator', methods=['GET', 'POST'])
def translator():

    translated_text = ""

    if request.method == 'POST':

        text = request.form['text']
        source = request.form['source']
        target = request.form['target']

        translated_text = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        conn = sqlite3.connect("translator.db")
        cur = conn.cursor()
        cur.execute("""
    INSERT INTO history
    (source_text, translated_text, source_lang, target_lang, created_at, type)
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    text,
    translated_text,
    source,
    target,
    str(datetime.now().date()),
    "text"
))

        conn.commit()
        conn.close()

    return render_template("translator.html", translated_text=translated_text)
@app.route('/history')
def history():

    conn = sqlite3.connect("translator.db")
    cur = conn.cursor()

    # all history
    cur.execute("SELECT * FROM history ORDER BY id DESC")
    data = cur.fetchall()

    # TOTAL
    cur.execute("SELECT COUNT(*) FROM history")
    total = cur.fetchone()[0] or 0

    # LANGUAGES (unique pairs)
    cur.execute("SELECT COUNT(DISTINCT source_lang || target_lang) FROM history")
    languages = cur.fetchone()[0] or 0

    # TODAY
    cur.execute("SELECT COUNT(*) FROM history WHERE created_at = date('now')")
    today = cur.fetchone()[0] or 0

    conn.close()

    return render_template(
        'history.html',
        history=data,
        total=total,
        languages=languages,
        today=today
    )


@app.route('/view/<int:id>')
def view_translation(id):
    return f"Viewing Translation ID: {id}"


@app.route('/download/<int:id>')
def download_translation(id):
    return f"Downloading Translation ID: {id}"


@app.route("/delete/<int:id>")
def delete(id):

    conn = sqlite3.connect("translator.db")   # FIXED
    cursor = conn.cursor()

    cursor.execute("DELETE FROM history WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/history")



@app.route("/ocr", methods=["GET", "POST"])
def ocr():
    extracted_text = ""

    if request.method == "POST":
        file = request.files["image"]
        # OCR logic here (pytesseract / easyocr)
        extracted_text = result

    return render_template("ocr.html", ocr_text=extracted_text)

@app.route("/pdf", methods=["GET", "POST"])
def pdf():
    extracted_text = ""
    translated_text = ""

    if request.method == "POST":
        file = request.files["pdf"]
        target_lang = request.form["language"]

        # Step 1: Extract text from PDF (PyPDF2 / pdfminer)
        # Step 2: Translate text (googletrans / deep translator)

        extracted_text = text
        translated_text = translated

    return render_template(
        "pdf.html",
        extracted_text=extracted_text,
        translated_text=translated_text
    )
    


@app.route("/grammar", methods=["GET", "POST"])
def grammar():
    input_text = ""
    corrected_text = ""
    improved_text = ""

    if request.method == "POST":
        input_text = request.form.get("input_text")

        # REAL correction
        corrected_text = str(TextBlob(input_text).correct())

        improved_text = corrected_text + " ✨ Improved Version"

    return render_template(
        "grammar.html",
        input_text=input_text,
        corrected_text=corrected_text,
        improved_text=improved_text
    )

@app.route("/analytics")
def analytics():

    conn = sqlite3.connect("translator.db")
    cursor = conn.cursor()

    # TOTAL
    cursor.execute("SELECT COUNT(*) FROM history")
    total_translations = cursor.fetchone()[0]

    # TEXT
    cursor.execute("SELECT COUNT(*) FROM history WHERE type='text'")
    text_count = cursor.fetchone()[0]

    # OCR
    cursor.execute("SELECT COUNT(*) FROM history WHERE type='ocr'")
    ocr_count = cursor.fetchone()[0]

    # PDF
    cursor.execute("SELECT COUNT(*) FROM history WHERE type='pdf'")
    pdf_count = cursor.fetchone()[0]

    # GRAMMAR
    cursor.execute("SELECT COUNT(*) FROM history WHERE type='grammar'")
    grammar_count = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "analytics.html",
        total_translations=total_translations,
        text_count=text_count,
        ocr_count=ocr_count,
        pdf_count=pdf_count,
        grammar_count=grammar_count
    )
    
if __name__ == "__main__":
    app.run(debug=True)