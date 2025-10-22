
# Import necessary libraries
from sklearn import datasets  # To load a sample dataset
from sklearn.model_selection import train_test_split  # To split the dataset into training and test sets
from sklearn.preprocessing import StandardScaler  # To standardize features by removing the mean and scaling to unit variance
from sklearn.svm import SVC  # To import the Support Vector Classifier

# Load a sample dataset. Here, we use the famous Iris dataset.
iris = datasets.load_iris()
X = iris.data  # The features (measurements) of the iris flowers
y = iris.target  # The labels (species) of the iris flowers

# Split the dataset into a training set and a test set (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create a Support Vector Classifier
svm = SVC(kernel='linear', C=1.0, random_state=42)  # kernel='linear' uses a linear hyperplane. C is the regularization parameter.

# Train the classifier with the training set
svm.fit(X_train, y_train)

# Use the trained classifier to make predictions on the test set
predictions = svm.predict(X_test)

# Evaluate the classifier
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy*100:.2f}%")
