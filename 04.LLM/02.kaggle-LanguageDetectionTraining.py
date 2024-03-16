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


# STEP BY STEP
#
# https://www.kaggle.com/code/chayandatta/language-detection-model-using-tensorflow



import os

os.system('cls')

df = pd.read_csv('Assets/Datasets/kaggle/language-detection/Language Detection.csv')
df.head(10)
df["Language"].value_counts()

language_counts = df["Language"].value_counts().reset_index()
language_counts.columns = ["Language", "Count"]

print(language_counts)


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

# Let's Build the model
#
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(len(label_encoder.classes_), activation='softmax')
])
#rectified linear unit (ReLU)

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# manually splitting the data
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Convert sparse matrices to TensorFlow Sparse Tensors

X_train_sparse = tf.convert_to_tensor(csr_matrix(X_train).todense(), dtype=tf.float32)
X_val_sparse = tf.convert_to_tensor(csr_matrix(X_val).todense(), dtype=tf.float32)
X_test_sparse = tf.convert_to_tensor(csr_matrix(X_test).todense(), dtype=tf.float32)

# Addestra il modello 
history = model.fit(X_train_sparse, y_train, epochs=10, batch_size=32, validation_data=(X_val_sparse, y_val))

# Salva il modello sul disco
model.save('Assets/Models/kaggle/language-detection/LanguageDetection_model.keras')
