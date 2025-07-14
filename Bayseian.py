import numpy as np
from collections import Counter, defaultdict


class NaiveBayesClassifier:
    def __init__(self):
        self.class_priors = {}
        self.feature_likelihoods = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        self.classes = None

    def fit(self, X, y):
        """
        Train the Naive Bayes Classifier.

        Parameters:
            X (numpy.ndarray): Feature matrix of shape (n_samples, n_features).
            y (numpy.ndarray): Target array of shape (n_samples,).
        """
        self.classes = np.unique(y)
        n_samples, n_features = X.shape

        
        class_counts = Counter(y)
        self.class_priors = {cls: count / n_samples for cls, count in class_counts.items()}

        
        for cls in self.classes:
            class_indices = np.where(y == cls)[0]
            class_samples = X[class_indices]

            for feature in range(n_features):
                feature_counts = Counter(class_samples[:, feature])
                total_feature_values = sum(feature_counts.values())

              
                for value, count in feature_counts.items():
                    self.feature_likelihoods[cls][feature][value] = (count + 1) / (total_feature_values + len(feature_counts))

    def predict(self, X):
        """
        Predict class labels for input data.

        Parameters:
            X (numpy.ndarray): Feature matrix of shape (n_samples, n_features).

        Returns:
            numpy.ndarray: Predicted class labels.
        """
        predictions = []
        for sample in X:
            class_probabilities = {}
            for cls in self.classes:
                
                posterior = self.class_priors[cls]
                for feature_index, feature_value in enumerate(sample):
                    posterior *= self.feature_likelihoods[cls][feature_index].get(feature_value, 1e-6)  
                class_probabilities[cls] = posterior

            
            predictions.append(max(class_probabilities, key=class_probabilities.get))
        return np.array(predictions)



if __name__ == "__main__":
    
    X = np.array([
        ["Sunny", "Hot", "High", "Weak"],
        ["Sunny", "Hot", "High", "Strong"],
        ["Overcast", "Hot", "High", "Weak"],
        ["Rain", "Mild", "High", "Weak"],
        ["Rain", "Cool", "Normal", "Weak"],
        ["Rain", "Cool", "Normal", "Strong"],
        ["Overcast", "Cool", "Normal", "Strong"],
        ["Sunny", "Mild", "High", "Weak"],
        ["Sunny", "Cool", "Normal", "Weak"],
        ["Rain", "Mild", "Normal", "Weak"],
        ["Sunny", "Mild", "Normal", "Strong"],
        ["Overcast", "Mild", "High", "Strong"],
        ["Overcast", "Hot", "Normal", "Weak"],
        ["Rain", "Mild", "High", "Strong"],
    ])

    y = np.array(["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"])


    from sklearn.preprocessing import LabelEncoder
    encoders = [LabelEncoder() for _ in range(X.shape[1])]
    X_encoded = np.array([encoder.fit_transform(X[:, col]) for col, encoder in enumerate(encoders)]).T
    y_encoded = LabelEncoder().fit_transform(y)

    
    nb = NaiveBayesClassifier()
    nb.fit(X_encoded, y_encoded)

    
    X_test = np.array([
        ["Sunny", "Cool", "High", "Strong"],
        ["Rain", "Mild", "Normal", "Weak"],
        ["Overcast", "Hot", "High", "Weak"],
    ])
    X_test_encoded = np.array([encoder.transform(X_test[:, col]) for col, encoder in enumerate(encoders)]).T
    y_pred = nb.predict(X_test_encoded)

    
    y_pred_decoded = LabelEncoder().fit(y).inverse_transform(y_pred)

    print("Predicted Classes:", y_pred_decoded)
