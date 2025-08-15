from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
# Example data for demonstration
data = {
    "Description": [
        "KFC Lunch", "Train Ticket", "Gas Cylinder", "Movie Ticket", "Grocery Shopping",
        "Uber Ride", "Electricity Bill", "Dinner at Restaurant", "Flight Booking", "Mobile Recharge"
    ],
    "Category": [
        "Food", "Travel", "Utilities", "Entertainment", "Groceries",
        "Travel", "Utilities", "Food", "Travel", "Utilities"
    ],
    "Amount": [
        250, 120, 900, 300, 1500,
        200, 1800, 700, 5000, 399
    ]
}

df = pd.DataFrame(data)
X_train, X_test, y_train, y_test = train_test_split(df["Description"], df["Category"], test_size=0.3, random_state=42)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))

new_expenses = ["KFC Lunch", "Train Ticket", "Gas Cylinder"]
print(model.predict(new_expenses))


import matplotlib.pyplot as plt
import seaborn as sns

# Count categories
plt.figure(figsize=(6,4))
sns.countplot(x="Category", data=df)
plt.title("Number of Expenses per Category")
plt.show()

# Spending distribution
plt.figure(figsize=(6,6))
df.groupby("Category")["Amount"].sum().plot.pie(autopct="%.1f%%")
plt.title("Spending Breakdown")
plt.ylabel("")
plt.show()


import numpy as np
import pandas as pd

threshold = df["Amount"].mean() + 2*df["Amount"].std()
unusual = df[df["Amount"] > threshold]
print("Unusual expenses:\n", unusual)
