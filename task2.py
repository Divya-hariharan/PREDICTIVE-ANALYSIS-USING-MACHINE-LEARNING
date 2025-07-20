# TASK - 2: PREDICTIVE ANALYSIS USING MACHINE LEARNING

# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 2: Load and View the Dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print(" Sample Data:")
print(df.head(5))

# Step 3: Data Visualization
sns.countplot(x='target', data=df)
plt.title("Flower Type Count")
plt.xlabel("Target Class")
plt.ylabel("Count")
plt.show()

# Step 4: Prepare Features and Labels
X = df.drop('target', axis=1)
y = df['target']

# Step 5: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

print(" Training data shape:", X_train.shape)
print(" Testing data shape:", X_test.shape)

# Step 6: Train the Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 7: Make Predictions
y_pred = model.predict(X_test)
print(" Accuracy:", accuracy_score(y_test, y_pred))

# Step 8: Evaluate the Model
print(" Accuracy Score:", accuracy_score(y_test, y_pred))
print("\n Classification Report:\n", classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Step 9: Feature Importance
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance.sort_values().plot(kind='barh')
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.show()
