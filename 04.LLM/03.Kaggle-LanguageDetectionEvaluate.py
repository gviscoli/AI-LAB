import time 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import tensorflow as tf
from keras import layers, models
import tensorflow as tf
from scipy.sparse import csr_matrix
import pickle

import os

os.system('cls')

# Let's create a function to test the model out
def predict_language(input_text, model):
    # Preprocess input text
    input_text = [input_text]
    input_vector = vectorizer.transform(input_text)
    input_sparse = tf.convert_to_tensor(input_vector.todense(), dtype=tf.float32)

    # Make prediction using the trained model
    predictions = model.predict(input_sparse)

    # Convert predicted index back to language label
    predicted_label_index = np.argmax(predictions)
    predicted_language = label_encoder.classes_[predicted_label_index]

    return predicted_language


model = models.load_model('Assets/Models/kaggle/language-detection/LanguageDetection_model.keras')

input_text = "Checking if this works"
predicted_language = predict_language(input_text, model)

print(f"The predicted language for '{input_text}' is: {predicted_language}")

