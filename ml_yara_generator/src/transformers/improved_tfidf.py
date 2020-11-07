from sklearn.feature_extraction.text import TfidfVectorizer

class ImprovedTfidfVectorizer(TfidfVectorizer):
    """
    This class is an update of the TFIDF that will only learn string patterns from the set of malicious files
    """
    def __init__(self, **kwargs):
        self.args = kwargs
        self.__tfidf_interal = TfidfVectorizer(**kwargs)


    def fit(self, raw_documents, y=None):
        voc = {}

        indexes = [index for index, t in enumerate(y) if t == 1]
        raw_documents_malicious = [raw_documents[index] for index in indexes]
        for document_malicious in raw_documents_malicious:
            self.__tfidf_interal.fit(document_malicious)
            voc = voc.intersection(self.__tfidf_interal.vocabulary_)
        super().__init__(**self.args, vocabulary=voc)
        return super().fit(raw_documents)

    def fit_transform(self, raw_documents, y=None):
        voc = {}

        indexes = [index for index, t in enumerate(y) if t == 1]
        raw_documents_malicious = [raw_documents[index] for index in indexes]

        self.__tfidf_interal.fit([raw_documents_malicious[0]])
        voc = set(self.__tfidf_interal.vocabulary_.keys())

        for document_malicious in raw_documents_malicious[1:]:
            self.__tfidf_interal.fit([document_malicious])
            voc = voc.intersection(set(self.__tfidf_interal.vocabulary_.keys()))

        super().__init__(**self.args, vocabulary=voc)
        return super().fit_transform(raw_documents)

