import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# supported algorithms
algorithms = {
    'LogisticRegression': LogisticRegression
    , 'SVC': SVC
    , 'DecisionTreeClassifier': DecisionTreeClassifier
    , 'RandomForestClassifier': RandomForestClassifier
    , 'XGBClassifier': XGBClassifier
    }

class Classification:
    def __init__(self, algorithm: str, **kwargs):
        """
        Set algorithm and model.

        Parameters:
            algorithm (str): Algorithm to use.
            kwargs (dict): Hyperparams for the specified algorithm.
        """
        
        # validate the algorithm and initialize it
        self.algorithm = algorithm
        if self.algorithm in algorithms:
            self.model = algorithms[self.algorithm](**kwargs)
        else:
            raise NotImplementedError(f"{algorithm} isn't supported. Select from {list(algorithms.keys())}.")

    def fit(self, X: pd.DataFrame, y: pd.Series, sample_weight = None):
        """Feeds data, predictors & target, into the algorithm."""
        
        self.model.fit(X=X, y=y, sample_weight=sample_weight)
    
    def predict(self, X: pd.DataFrame):
        """Predicts target value for the given observations."""

        return self.model.predict(X=X)
        
    def score(self, X: pd.DataFrame):
        """Computes probability score for the given observations."""

        return self.model.predict_proba(X=X)
    