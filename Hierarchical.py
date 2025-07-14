import numpy as np
from collections import Counter
class DecisionTree:
    def __init__(self, max_depth=None):
        """
        Initialize the Decision Tree.

        Parameters:
            max_depth (int): The maximum depth of the tree. If None, grows the tree fully.
        """
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        """
        Fit the Decision Tree to the training data.

        Parameters:
            X (numpy.ndarray): Features matrix of shape (n_samples, n_features).
            y (numpy.ndarray): Target array of shape (n_samples,).
        """
        self.tree = self._build_tree(X, y)

    def predict(self, X):
        """
        Predict the labels for the input data.

        Parameters:
            X (numpy.ndarray): Features matrix of shape (n_samples, n_features).

        Returns:
            numpy.ndarray: Predicted labels.
        """
        return np.array([self._predict_sample(self.tree, sample) for sample in X])

    def _gini_impurity(self, y):
        """Calculate the Gini impurity for a set of labels."""
        counts = Counter(y)
        n = len(y)
        return 1 - sum((count / n) ** 2 for count in counts.values())

    def _best_split(self, X, y):
        """
        Find the best feature and threshold to split on.

        Returns:
            best_feature (int): Index of the best feature to split on.
            best_threshold (float): Threshold value for the split.
            best_gain (float): Gini gain for the split.
        """
        n_samples, n_features = X.shape
        best_feature, best_threshold, best_gain = None, None, 0
        parent_impurity = self._gini_impurity(y)

        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_indices = X[:, feature] <= threshold
                right_indices = X[:, feature] > threshold
                if len(y[left_indices]) == 0 or len(y[right_indices]) == 0:
                    continue

                left_impurity = self._gini_impurity(y[left_indices])
                right_impurity = self._gini_impurity(y[right_indices])
                n_left, n_right = sum(left_indices), sum(right_indices)
                weighted_impurity = (n_left / n_samples) * left_impurity + (n_right / n_samples) * right_impurity

                gain = parent_impurity - weighted_impurity
                if gain > best_gain:
                    best_feature, best_threshold, best_gain = feature, threshold, gain

        return best_feature, best_threshold, best_gain

    def _build_tree(self, X, y, depth=0):
        """
        Recursively build the decision tree.

        Returns:
            dict: Nested dictionary representing the tree structure.
        """
        n_samples, n_features = X.shape
        n_classes = len(set(y))

        if n_classes == 1 or n_samples == 0 or (self.max_depth is not None and depth >= self.max_depth):
            return Counter(y).most_common(1)[0][0]  

        feature, threshold, gain = self._best_split(X, y)
        if gain == 0:
            return Counter(y).most_common(1)[0][0]  

        left_indices = X[:, feature] <= threshold
        right_indices = X[:, feature] > threshold

        return {
            "feature": feature,
            "threshold": threshold,
            "left": self._build_tree(X[left_indices], y[left_indices], depth + 1),
            "right": self._build_tree(X[right_indices], y[right_indices], depth + 1),
        }

    def _predict_sample(self, node, sample):
        """Predict the label for a single sample using the tree."""
        if isinstance(node, dict):
            feature = node["feature"]
            threshold = node["threshold"]
            if sample[feature] <= threshold:
                return self._predict_sample(node["left"], sample)
            else:
                return self._predict_sample(node["right"], sample)
        else:
            return node


# Example Usage
if __name__ == "__main__":
    # Sample dataset
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    # Load Iris dataset
    data = load_iris()
    X = data['data']
    y = data['target']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the Decision Tree
    tree = DecisionTree(max_depth=3)
    tree.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = tree.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
