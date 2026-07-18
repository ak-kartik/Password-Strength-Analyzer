# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:35:17 2026

@author: karti
"""# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:35:17 2026

@author: karti
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample Dataset
data = {
    "Email": [
        "Congratulations! You won a lottery. Click here now.",
        "Your bank account is blocked. Verify immediately.",
        "Meeting is scheduled for tomorrow.",
        "Project submission deadline is Friday.",
        "Claim your free gift now.",
        "Please review the attached report.",
        "Update your password immediately.",
        "Let's have lunch tomorrow."
    ],
    "Label": [
        "Phishing",
        "Phishing",
        "Safe",
        "Safe",
        "Phishing",
        "Safe",
        "Phishing",
        "Safe"
    ]
}

df = pd.DataFrame(data)

# Feature Extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["Email"])

y = df["Label"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, prediction))

# Confusion Matrix
print("\nConfusion Matrix")
print(confusion_matrix(y_test, prediction))

# Test New Email
email = input("\nEnter Email: ")

email_vector = vectorizer.transform([email])

result = model.predict(email_vector)

print("Prediction:", result[0])