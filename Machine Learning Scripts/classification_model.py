
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Dummy data: [Enemy Type, Player Health, Weapon Type, Difficulty]
data = np.array([
    [1, 80, 2, 3],  # e.g., 1: Creeper, 80: health, 2: sword, 3: Hard difficulty
    [2, 50, 1, 2],  # 2: Skeleton, 50: health, 1: bow, 2: Medium
    [1, 20, 2, 3],  
    [2, 90, 1, 1],  
    [1, 60, 2, 3],
    # Add more training data here
])

# Labels (1 = Coachable Moment 1, 2 = Coachable Moment 2)
labels = np.array([1, 2, 1, 2, 1])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)

# Model definition
model = RandomForestClassifier()

# Training the model
model.fit(X_train, y_train)

# Predicting on test data
y_pred = model.predict(X_test)

# Print accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Save the model for later use
with open("classification_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

# To load and predict with this model:
# with open("classification_model.pkl", "rb") as model_file:
#     loaded_model = pickle.load(model_file)
#     predictions = loaded_model.predict(new_data)
