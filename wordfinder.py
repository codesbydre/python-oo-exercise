import random 


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> random.seed(42) # Set seed for predictable results

    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random()
    'researchful'

    >>> wf.random()
    'calyptriform'

    >>> wf.random()
    'amellus'
    

    """
    def __init__(self, filepath):
        self.words = self.load_words(filepath)
        print(f"{len(self.words)} words read")

    def load_words(self, filepath):
        """Load words from given file and return them as list"""
        with open(filepath, "r") as file:
            return [word.strip() for word in file.readlines()]
        
    def random(self):
        """Return random word from the list of words"""
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary, ignoring blank lines and comments.
    
    >>> random.seed(42) # Set seed for predictable results

    >>> swf = SpecialWordFinder("special_words.txt")
    4 words read

    >>> swf.random()
    'kale'

    >>> swf.random()
    'parsnips'

    >>> swf.random()
    'apple'

    """
    def load_words(self, filepath):
        """Load words from given file, ignoring blank lines and comments, and return them as a list."""
        with open(filepath, "r") as file:
            return [
                word.strip()
                for word in file.readlines()
                if word.strip() and not word.startswith("#")
            ]