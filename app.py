#Este será el archivo principal donde construirás tu API Flask.
from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Cargar el vectorizador y el modelo entrenado
with open(os.path.join('tfidf_vectorizer.pkl'), 'rb') as f:
    vectorizer = pickle.load(f)

with open(os.path.join('voting_classifier_model.pkl'), 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Asegúrate de que 'review' es la clave que envías en el JSON
    # Transformar el texto utilizando el vectorizador
    X_new_tfidf = vectorizer.transform([data['review']])
    
    # Hacer la predicción
    prediction = model.predict(X_new_tfidf)

    # Retornar la predicción
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

