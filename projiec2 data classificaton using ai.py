# Step 1: Import libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score

# Step 2: Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Step 3: Create DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = y

print(df.head())
print(df["species"].value_counts())

# Step 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 6: KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Step 7: Prediction
predictions = model.predict(X_test)

# Step 8: Results
print("\nAccuracy:", accuracy_score(y_test, predictions))

print("F1 Score:", f1_score(y_test, predictions, average="macro"))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=iris.target_names
    )
)