from sklearn.base import BaseEstimator
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline


class Classifier(BaseEstimator):
    """
    This class is a pipeline including linear models to generate the yara rule.
    """

    def __init__(self):
        self.pipe = Pipeline([
            ('vect', TfidfVectorizer(
                ngram_range=(5, 5),
                decode_error='ignore'),
             ),
            ('clf', RandomForestClassifier(

            )),
        ])

    def fit(self, X, y):
        self.pipe.fit(X, y)

        return self.pipe

    def predict(self, X, **predict_params):
        return self.pipe.predict(X)
