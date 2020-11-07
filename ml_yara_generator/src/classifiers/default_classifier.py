from sklearn.base import BaseEstimator
from ml_yara_generator.src.transformers.improved_tfidf import ImprovedTfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline


class Classifier(BaseEstimator):
    """
    This class is a pipeline including linear models to generate the yara rule.
    """

    def __init__(self):
        self.pipe = Pipeline([
            ('vect', ImprovedTfidfVectorizer(
                ngram_range=(4, 4),
                encoding='ISO-8859-1',
                analyzer='char',
                max_features=None
            ),
        ),
            ('clf', RandomForestClassifier(

            )),
        ])

    def fit(self, X, y):
        self.pipe.fit(X, y)

        return self.pipe

    def predict(self, X, **predict_params):
        return self.pipe.predict(X)
