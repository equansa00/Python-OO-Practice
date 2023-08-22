"""Word Finder: finds random words from a dictionary."""
import random

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
            print(f"An error occurred: {e}")
            self.words = []

    def random(self):
        """Return a random word from the list of words."""
        if self.words:
            return random.choice(self.words)
        else:
            return "No words available"

if __name__ == "__main__":
    word_finder = WordFinder("words.txt")
    print(word_finder.random())

