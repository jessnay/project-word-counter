from collections import Counter
import re

# 1. Load file 
def load_file(filename):
    """Load the content of the file and return as a string."""
    with open(filename, 'r') as file:
        return file.read()

# 2. Count words 
def count_words(text):
    """Count the frequency of each word in the text."""
    # Convert the text to lowercase and tokenize it using regular expression
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

# 3. Save report 
def save_report(counter, output_filename):
    """Save the word frequency report to a file."""
    with open(output_filename, 'w') as file:
        for word, count in counter.most_common():
            file.write(f'{word}: {count}\n')

def main():
    text = load_file("sample.txt")
    word_counts = count_words(text)
    save_report(word_counts, "word_report.txt")
    print("Word report saved to word_report.txt!")

if __name__ == "__main__":
    main()

