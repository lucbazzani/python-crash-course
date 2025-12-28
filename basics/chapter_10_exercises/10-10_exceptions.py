# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org)
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the
# number of times 'row' appears in a string:
# >>> line = "Row, row, row your boat" 
# >>> line.count('row') 
# 2 
# >>> line.lower().count('row') 
# 3
# Notice that converting the string to lowercase using lower() catches all
# appearances of the word you’re looking for, regardless of how it’s formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.
from pathlib import Path 

def count_word_occurrences(path, word): 
    """Count the number of times a word appears in a text file."""
    try: 
        contents = path.read_text(encoding='utf-8') 
    except FileNotFoundError: 
        pass
    else: 
        occurrences = contents.lower().count(word)
        print(f"The word '{word.strip()}' occurs {occurrences} times in the file '{path}'.")
 
filenames = [
        'basics/chapter_10_exercises/text_files/brazilian_tales.txt', 
        'basics/chapter_10_exercises/text_files/don_quixote.txt', 
        'basics/chapter_10_exercises/text_files/metamorphosis.txt'
        ]

for filename in filenames: 
    path = Path(filename) 
    count_word_occurrences(path, 'the ')
