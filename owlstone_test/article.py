import re
quote_capturer = re.compile('[“\"][^”\"\n]*')

class Article(object):
    """Represents an article in the data. 
    
    Stores a number of different statistics about the article in each instance of the object, including: 
    - word count
    - average words per paragraph
    - average length of each word
    - the number of words in quotes
    """
    def __init__(self, publisher, article_id, text):
        self.publisher = publisher
        self.article_id = article_id
        self.text = text
        self.word_count = self.get_word_count(text)
        self.average_words_per_par = self.get_average_words_per_par()
        self.average_word_length = self.get_average_word_length()
        self.number_words_in_quotes = self.get_number_words_in_quotes()

    def get_word_count(self, words):
        """Find the word count and store it in the article object instance."""
        return len(words.split())

    def get_average_words_per_par(self):
        """Find the average word count per paragraph and store it in the article object instance."""
        pars = self.text.split('\n')
        non_empty_pars = [par for par in pars if len(par) > 0] # Drop pars that have no words, e.g. due to double line breaks
        return float(sum((self.get_word_count(par) for par in non_empty_pars))) / len(non_empty_pars)

    def get_average_word_length(self):
        """Find the average length of words and store it in the article object instance."""
        return float(sum((len(word) for word in self.text.split()))) / self.word_count

    def get_number_words_in_quotes(self):
        """Find the number of words in quotes and store it in the article object instance."""
        return float(sum((self.get_word_count(quote) for quote in re.findall(quote_capturer, self.text))))

    def __repr__(self):
        return 'Article by {} with id_number {}'.format(self.publisher, self.id_number)