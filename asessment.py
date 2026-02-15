"""
pythonAssessment.py

A text analysis tool for analyzing news articles.
Performs the following tasks:
- Count specific word occurrences
- Identify most common word
- Calculate average word length
- Count number of paragraphs
- Count number of sentences
"""

import re
from collections import Counter


def count_specific_word(text: str, search_word: str) -> int:
    """
    Counts the number of occurrences of a specific word in the text.
    Case-insensitive.
    """
    if not text or not search_word:
        return 0

    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(search_word.lower())


def identify_most_common_word(text: str):
    """
    Identifies the most common word in the text.
    Returns None if text is empty.
    """
    if not text.strip():
        return None

    words = re.findall(r'\b\w+\b', text.lower())

    if not words:
        return None

    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]

    return most_common_word


def calculate_average_word_length(text: str) -> float:
    """
    Calculates the average length of words in the text.
    Excludes punctuation and special characters.
    Returns 0 for empty string.
    """
    if not text.strip():
        return 0.0

    words = re.findall(r'\b\w+\b', text)

    if not words:
        return 0.0

    total_characters = sum(len(word) for word in words)
    return total_characters / len(words)


def count_paragraphs(text: str) -> int:
    """
    Counts the number of paragraphs in the text.
    Paragraphs are separated by empty lines.
    Returns 1 if text is empty.
    """
    if not text.strip():
        return 1

    paragraphs = [p for p in text.split('\n') if p.strip()]
    return len(paragraphs)


def count_sentences(text: str) -> int:
    """
    Counts the number of sentences in the text.
    Sentences end with '.', '!' or '?'.
    Returns 1 if text is empty.
    """
    if not text.strip():
        return 1

    sentences = re.findall(r'[.!?]+', text)
    return len(sentences)


def main():
    print("\n===== News Article Text Analysis Tool =====\n")

    article = input("Paste your news article text below:\n\n")

    search_word = input("\nEnter a word to count its occurrences: ")

    
    word_count = count_specific_word(article, search_word)
    most_common = identify_most_common_word(article)
    avg_length = calculate_average_word_length(article)
    paragraph_count = count_paragraphs(article)
    sentence_count = count_sentences(article)

    
    print("\n===== Analysis Results =====")
    print(f"Occurrences of '{search_word}': {word_count}")
    print(f"Most common word: {most_common}")
    print(f"Average word length: {avg_length:.2f}")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")
    print("\n===== End of Analysis =====\n")


if __name__ == "__main__":
    main()