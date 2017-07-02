from statistics import mean, stdev

class Publisher(object):
    """Represents a publisher of articles in the project's data.
    
    Relies on the Article class to derive aggregate statistics about the articles by each publisher. 
    
    Available functions: 
    - get_average_word_count_by_article: Returns the arithmetic mean word count of the publisher's sample articles
    - get_stdev_of_word_count_by_article: Returns the sample standard deviation word count of the publisher's articles
    - get_average_word_length: Calculates a weighted arithmetic mean of the average article word lengths
    - get_proportion_words_in_quotes: Calculates the average proportion of words in quotes by publisher
    """
    def __init__(self, publisher_name):
        self._name = publisher_name
        self._articles = []

    def get_average_word_count_by_article(self):
        return mean((article.word_count for article in self._articles))

    def get_stdev_of_word_count_by_article(self):
        return stdev((article.word_count for article in self._articles))

    def get_average_word_length(self):
        numerator = 0.0
        total_words = 0.0
        for article in self._articles:
            numerator += article.word_count * article.average_word_length
            total_words += article.word_count
        return numerator / total_words

    def get_proportion_words_in_quotes(self):
        words_in_quotes = 0.0
        total_words = 0.0
        for article in self._articles:
            words_in_quotes += article.number_words_in_quotes
            total_words += article.word_count
        return words_in_quotes / total_words

    def __repr__(self):
        return 'Publisher(\'{}\')'.format(self._name)