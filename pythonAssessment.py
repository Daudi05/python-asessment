import re
from collections import Counter



def count_specific_word(text, word):
    pattern = r'\b' + re.escape(word.lower()) + r'\b'
    return len(re.findall(pattern, text.lower()))

def identify_most_common_word(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    if not words:
        return None
    
    counter = Counter(words)
    return counter.most_common(1)[0][0]

def calculate_average_word_length(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    if not words:
        return 0
    total_length = 0
    for w in words:  
        total_length += len(w)
    avg = total_length / len(words) 
    return avg

def count_paragraphs(text):
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    if paragraphs:  
        return len(paragraphs)
    else:
        return 1

def count_sentences(text):
    sentences = re.findall(r'[.!?]', text)
    if sentences: 
        return len(sentences)
    else:
        return 1
if __name__ == "__main__":
    text = input("Enter text to analyze:\n")
    word = input("Enter word to count:\n")
    print("Occurrences:", count_specific_word(text, word))
    print("Most common word:", identify_most_common_word(text))
    print("Average word length:", calculate_average_word_length(text))
    print("Paragraphs:", count_paragraphs(text))
    print("Sentences:", count_sentences(text))
