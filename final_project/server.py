<<<<<<< HEAD
from machinetranslation import translator
from flask import Flask, render_template, request
import json
=======
from .machinetranslation import translator
from flask import Flask, render_template, request
>>>>>>> First global commit.

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
<<<<<<< HEAD
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
=======
    text_to_translate = request.args.get('textToTranslate')
    return translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    return translator.french_to_english(text_to_translate)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
>>>>>>> First global commit.

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
