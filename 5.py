class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

text = "Python is a great programming language."
analyzer = TextAnalyzer(text)

print(f"Word count: {analyzer.word_count()}")
