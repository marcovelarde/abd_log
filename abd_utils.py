# Imports
import pickle

# Loading the vocabularys from disk

class ABDUtils:
    def __init__(self, word_index=None, reverse_word_index=None):
        self.loaded_word_index = word_index
        self.loaded_reverse_word_index = reverse_word_index
        if word_index is None and reverse_word_index is None:
            with open('model/abd_variables.pkl', 'rb') as f:
                self.loaded_word_index, self.loaded_reverse_word_index = pickle.load(f)
        else:
            if word_index is None:
                self.loaded_reverse_word_index = reverse_word_index
                with open('model/abd_w_index.pkl', 'rb') as f:
                    self.loaded_word_index = pickle.load(f)
            elif reverse_word_index is None:
                self.loaded_word_index = word_index
                with open('model/abd_rw_index.pkl', 'rb') as f:
                    self.loaded_reverse_word_index = pickle.load(f)

    # Defining functions for handling (encoding and decoding) the urls based on the vocabulary

    # Encode a String and return an Array of integers
    def encode(self, text, word_index=None):
        if word_index is None: word_index=self.loaded_word_index
        text_ls = []
        for i in text.split():
            try:
                text_ls.append(word_index[i])
            except KeyError:
                print('Unhandled word \'' + i + '\'')
        return text_ls
    # Decode an Array of integers and return a String
    def decode(self, ls, reverse_word_index=None):
        if reverse_word_index is None: reverse_word_index=self.loaded_reverse_word_index
        return ' '.join([reverse_word_index.get(i, '?') for i in ls])

    # Encode a single word and return its vocabulary-indexed integer
    def encode_single(self, text, word_index=None):
        if word_index is None: word_index=self.loaded_word_index
        return word_index.get(text)
    # Decode a single integer and return its (reversed) vocabulary-indexed String
    def decode_single(self, index, reverse_word_index=None):
        if reverse_word_index is None: reverse_word_index=self.loaded_reverse_word_index
        return reverse_word_index.get(index)

# Helper function: append a '<PAD>' encoded String before a url
def insert_start(ls):
    ls.insert(0, 1)
    return ls
