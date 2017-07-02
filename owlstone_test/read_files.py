"""Opens all the files in a specified directory and gathers their data to help with textual analysis."""

from os import listdir, path
from owlstone_test.article import Article
from owlstone_test.publisher import Publisher

class Text_Processor(object):
    """Opens the files and returns relevant data as a dictionary with the pubslisher name as a key and
    a publisher object as a value.
    
    The files must be saved in the text_files directory with the publisher name before an underscore, then an 
    arbitrary ID number, e.g. BBC_01.txt. 
    
    Available function: 
    - read_files: This needs to be called to read in the files and return the relevant data. 
    """
    def __init__(self, path='./owlstone_test/owlstone_test/text_files'):
        self._path = path
        self._publishers = {}

    def read_files(self):
        """Opens the files in the specified path and returns a dictionary with publisher names as keys and 
        publisher objects as values."""
        for file_name in listdir(self._path):
            try:
                publisher_name = file_name.split('_')[0]
                article_id = file_name.split('_')[1].split('.')[0]
            except IndexError as e:
                raise ValueError('File name formatted incorrectly') from e
            else:
                if publisher_name not in self._publishers:
                    self._publishers[publisher_name] = Publisher(publisher_name)
                with open(path.join(self._path, file_name), encoding="utf8") as f:
                    publisher = self._publishers[publisher_name]
                    publisher._articles.append(Article(publisher_name, article_id, f.read()))

        return self._publishers
