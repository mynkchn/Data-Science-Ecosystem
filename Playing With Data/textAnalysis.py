import re

class TextAnalyzer:
    def __init__(self, text):
        fmtText = re.sub(r'[!?,.]', '', text)  # Remove punctuation
        lower = fmtText.lower()  # Convert to lowercase
        self.text = lower
        self.word_count = {}  # Store word frequencies
        print(self.text)

    def feqAll(self):
        words = self.text.split()  # Split into words
        self.word_count = {word: words.count(word) for word in set(words)}  # Count frequency
        return self.word_count

    def feqOf(self, word):
        if not self.word_count:  # Ensure word_count is populated
            self.feqAll()
        return self.word_count.get(word, 0)  # Return frequency of the word

# Example usage:
givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

test = TextAnalyzer(givenstring)
print(test.feqAll())  # Get word frequency dictionary
print(test.feqOf("diam"))  # Get frequency of "diam"
print(test.feqOf("lorem"))  # Get frequency of "lorem"
