
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, matthews_corrcoef, \
    confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import matplotlib.pyplot as plt

# Load in the dataset from CSV using Pandas
data = pd.read_csv("titanic_new.csv")

X = data.drop(["Survived"], axis=1)
y = data["Survived"]

# Split data into training samples and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create a decision tree classifier
knn = KNeighborsClassifier(n_neighbors=7)

# Train Decision Tree Classifier
knn_model = knn.fit(X_train, y_train)

# Test the model against the test data
knn_pred = knn_model.predict(X_test)

print(f"Accuracy is {accuracy_score(y_test, knn_pred)}")
print(f"Recall is {recall_score(y_test, knn_pred)}")
print(f"Specificity is {recall_score(y_test, knn_pred, pos_label=0)}")
print(f"Precision is {precision_score(y_test, knn_pred)}")
print(f"F1-Score is {f1_score(y_test, knn_pred)}")
print(f"MCC is {matthews_corrcoef(y_test, knn_pred)}")

# See the confusion matrix
cm = confusion_matrix(y_test, knn_pred, labels=knn_model.classes_)
cm_visual = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=knn_model.classes_)
cm_visual.plot()
plt.show()