import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow import keras

def ModelReadyString(text_str, pad):
    '''converts an individual unit of text into tokenized sequences'''
    text = [text_str]
    t = keras.preprocessing.text.Tokenizer()
    t.fit_on_texts(text)
    tokens = t.texts_to_sequences(text)
    tokens2 = keras.preprocessing.sequence.pad_sequences(tokens, maxlen=pad)
    return tokens2

app = Flask(__name__)
model = keras.models.load_model('BidFinal.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tokenized = ModelReadyString(request.form['Text'], 1640)
    prediction = model.predict(tokenized)
    output = round(prediction[0][1]*100, 2)
    return render_template('index.html', prediction_text='We predict a {}% probability that an AI wrote this.'.format(output))

if __name__ == "__main__":
    app.run(debug=True)