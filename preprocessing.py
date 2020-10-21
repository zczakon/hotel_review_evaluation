import nltk
from nltk.corpus import stopwords
import inflect

nltk.download('stopwords')


class Preprocessing:
    @staticmethod
    def stopwords():
        return stopwords.words('english')

    def remove_stopwords(self, words: list):
        stop_words = self.stopwords()
        for w in stop_words:
            if w in words:
                words.remove(w)
        return words

    @staticmethod
    def replace_weird_symbol(words: list):
        return [word.replace('\t', '') for word in words]

    @staticmethod
    def replace_numbers(words):
        """Replace all interger occurrences in list of tokenized words with textual representation"""
        p = inflect.engine()
        new_words = []
        for word in words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words

    def normalize(self, doc):
        words = nltk.word_tokenize(doc)
        words = self.replace_weird_symbol(words)
        words = self.replace_numbers(words)
        words = [word.lower() for word in words if word.isalpha()]
        words = self.remove_stopwords(words)
        return words
