from sklearn.neural_network import MLPClassifier
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
neural_net = MLPClassifier(solver="lbfgs", hidden_layer_sizes=(3, 2))

# Train Decision Tree Classifier
neural_model = neural_net.fit(X_train, y_train)

# Test the model against the test data
neural_pred = neural_model.predict(X_test)

print(f"Accuracy is {accuracy_score(y_test, neural_pred)}")
print(f"Recall is {recall_score(y_test, neural_pred)}")
print(f"Specificity is {recall_score(y_test, neural_pred, pos_label=0)}")
print(f"Precision is {precision_score(y_test, neural_pred)}")
print(f"F1-Score is {f1_score(y_test, neural_pred)}")
print(f"MCC is {matthews_corrcoef(y_test, neural_pred)}")

# See the confusion matrix
cm = confusion_matrix(y_test, neural_pred, labels=neural_model.classes_)
cm_visual = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=neural_model.classes_)
cm_visual.plot()
plt.show()