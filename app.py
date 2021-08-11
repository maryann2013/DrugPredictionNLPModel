import spacy
from spacy import displacy
import pickle
import warnings
from flask import Flask, request, render_template,redirect
import en_core_med7_lg


warnings.warn("first example of warning!", DeprecationWarning)

import os

#nlp = pickle.load(open('nlp.pkl', 'rb'))

app = Flask(__name__)
med7 = en_core_med7_lg.load()

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/',methods=['GET', 'POST'])
def extract():
    if request.method=='POST':
        txt = request.form['ner_text']
        doc=med7(txt)
        result = [(ent.text, ent.label_) for ent in doc.ents]

    return render_template('result.html',result=result)






if __name__ == "__main__":
    app.run(debug=True)
