import spacy

from collections import defaultdict

class TextPrep:

    def _create_doc(text: str) -> list:
        """Converts text to processed ready list"""
        nlp = spacy.load("en_core_web_sm")
        return nlp(text)

    @classmethod
    def tokenize(self, text: str) -> list:
        """
        Tokenizes all the words in the text and returs as a list
        """
        doc = self._create_doc(text)
        return [token for token in doc]

    @classmethod
    def remove_stop_words(self, text: str) -> list:
        """
        Removes stop words, like “if”, “but”, “or” and so on
        """
        doc = self._create_doc(text)
        return [token for token in doc if not token.is_stop]

    @classmethod
    def lemmatize(self, text: str) -> list:
        """Normalizes words to its simplest form, or lemma.
        
        for example “watched”, “watching”, “watches”
        will all be normalized to “watch.”
        """
        tokens = TextPrep.remove_stop_words(text)
        lemmas = defaultdict(list)

        for t in tokens:
            lemmas[t.lemma_].append(t)

        return lemmas

    @classmethod
    def vertorize(self, text: str) -> list:
        """Transforms tokens into a dense vector"""
        tokens = TextPrep.remove_stop_words(text)
        return [tokens[i].vector for i in range(len(tokens))]


if __name__ == '__main__':
    t = '''
Dave watched as the forest burned up on the hill,
only a few miles from his house. The car had
been hastily packed and Marta was inside trying to round
up the last of the pets. "Where could she be?" he wondered
as he continued to wait for Marta to appear with the pets.
Watching what was going on.
'''
    print(TextPrep.lemmatize(t))