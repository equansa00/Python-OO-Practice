import random

class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, start=0):
        """Initialize a serial generator with a starting number."""
        self.start = start
        self.next = start

    def generate(self):
        """Return the next sequential serial number."""
        result = self.next
        self.next += 1
        return result

    def reset(self):
        """Reset the serial number back to the original start number."""
        self.next = self.start

    def __repr__(self):
        """Return a string representation of the SerialGenerator."""
        return "<SerialGenerator start={} next={}>".format(self.start, self.next)

class WordFinder:
    """Read words from a file and provide random word retrieval."""
    
    def __init__(self, path):
        """Initialize WordFinder with a file path and read words."""
        try:
            with open(path, 'r') as file:
                self.words = [line.strip() for line in file.readlines()]
            self.num_words = len(self.words)
            print("{} words read".format(self.num_words))
        except FileNotFoundError:
            print("Error: The specified file was not found.")
            self.words = []
        except Exception as e:
            print("An error occurred: {}".format(e))
            self.words = []

    def random(self):
        """Return a random word from the list of words."""
        if self.words:
            return random.choice(self.words)
        else:
            return "No words available"

class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder that handles comments and blank lines."""
    
    def __init__(self, path):
        """Initialize SpecialWordFinder by calling superclass init."""
        super().__init__(path)
        self.words = [word for word in self.words if word and not word.startswith('#')]

# Example usage
if __name__ == "__main__":
    WORDS_FILE = "words.txt"

    wf = WordFinder(WORDS_FILE)
    print(wf.random())
    print(wf.random())
    print(wf.random())
    
    serial = SerialGenerator(start=100)
    print(serial.generate())
    print(serial.generate())
