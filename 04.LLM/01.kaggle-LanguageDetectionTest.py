import time 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.python.keras import layers, models
import tensorflow as tf
from scipy.sparse import csr_matrix
import pickle

import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation

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

plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Language', data=language_counts, palette='muted')
plt.xlabel('Count')
plt.ylabel('Language')
plt.title('Language Distribution')
plt.tight_layout()
plt.show()