import time 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import tensorflow as tf
from keras import layers, models


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


df = pd.read_csv('Assets/Datasets/kaggle/language-detection/Language Detection.csv')
df.head(10)
df["Language"].value_counts()

language_counts = df["Language"].value_counts().reset_index()
language_counts.columns = ["Language", "Count"]

# splitting the df to test and train data
#
train_texts, test_texts, train_labels, test_labels = train_test_split(df['Text'], df['Language'], test_size=0.2, random_state=42)

# Tokenize and vectorize the text data
#
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

# Encode the language labels
#
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(train_labels)
y_test = label_encoder.transform(test_labels)

#model = models.load_model('Assets/Models/kaggle/language-detection/LanguageDetection_model.keras')
model = models.load_model('Assets/Models/kaggle/language-detection/LanguageDetection_model.h5')

input_text = "Checking if this works"
predicted_language = predict_language(input_text, model)

print(f"The predicted language for '{input_text}' is: {predicted_language}")

input_text = "Hola Kaggle"
predicted_language = predict_language(input_text, model)

print(f"The predicted language for '{input_text}' is: {predicted_language}")

input_text = "Ciao Mondo"
predicted_language = predict_language(input_text, model)

print(f"The predicted language for '{input_text}' is: {predicted_language}")