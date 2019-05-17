from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation


class Analyser:
    """
    Class for the analysis of politician's phrase based on
    the Latent Dirichlet allocation and Non-negative matrix factorization
    methods.
    """
    def __init__(self, phrase):
        """
        (Analyser, str) -> None
        Initial function fot the Analyser object.
        """
        self.__phrase = phrase

        self.max_features = 1000
        self.num_components = 3

        self.__tf_idf_vectorizer = None
        self.__tf_idf_nmf = None
        self.__nmf = None

        self.__tf_vectorizer = None
        self.__tf_lda = None
        self.__lda = None

        self.__topics = None

    @property
    def topics(self):
        """
        (Analyser) -> set()
        Returns set of topics created by the analyser.
        """
        return self.__topics

    @topics.setter
    def topics(self, value):
        """
        (Analyser) -> None
        Raises an AttribureError exception if tried to assign a value to
        hidden __topics field.
        """
        raise AttributeError('you cannot set any value to this field')

    def __format(self):
        """
        (Analyser) -> None
        Shapes the phrase into a list of sentences.
        """
        self.__phrase = self.__phrase.split('.')

    def __tf_ifd_for_nmf(self):
        """
        (Analyser) -> None
        Creates tf-idf vectorizer and creates term-document matrix.
        """
        self.__tf_idf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                                  max_features=self.max_features,
                                           stop_words='english')
        self.__tf_idf_nmf = self.__tf_idf_vectorizer.fit_transform(self.__phrase)

    def __nmf_learn(self):
        """
        (Analyser) -> None
        Trains a NMF model for the self.__phrase data.
        """
        self.__tf_ifd_for_nmf()
        self.__nmf = NMF(n_components=self.num_components, random_state=1,
                         alpha=.1, l1_ratio=.5).fit(self.__tf_idf_nmf)

    def __tf_for_lda(self):
        """
        (Analyser) -> None
        Creates tf vectorizer and creates term-document matrix.
        """
        self.__tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                               max_features=self.max_features,
                                               stop_words='english')
        self.__tf_lda = self.__tf_vectorizer.fit_transform(self.__phrase)

    def __lda_learn(self):
        """
        (Analyser) -> None
        Trains a LDA model for the self.__phrase data.
        """
        self.__tf_for_lda()
        self.__lda = LatentDirichletAllocation(n_components=self.num_components, max_iter=5,
                                               learning_method='online',
                                               learning_offset=50.,
                                               random_state=0)
        self.__lda.fit(self.__tf_lda)

    def analyse(self):
        """
        (Analyse) -> None
        The analysis of the phrase with the two methods and post-processing of the results.
        """
        self.__format()
        self.__nmf_learn()
        self.__lda_learn()

        tfidf_features = self.__tf_idf_vectorizer.get_feature_names()
        nmf_topics = set()
        for topic in self.__nmf.components_:
            nmf_topics.add(tfidf_features[topic.argsort()[-1]])
        tf_features = self.__tf_vectorizer.get_feature_names()
        lda_topics = set()
        for topic in self.__lda.components_:
            lda_topics.add(tf_features[topic.argsort()[-1]])

        self.__topics = nmf_topics.intersection(lda_topics)
