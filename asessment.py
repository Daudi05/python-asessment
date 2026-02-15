

# pythonAssessment.py

def count_specific_word(text, search_word):
    """Counts occurrences of a specific word using while and if."""
    if not text or not search_word:
        return 0
    
    count = 0
    # Manual split to avoid libraries
    words = text.lower().split()
    
    i = 0
    while i < len(words):
        # Clean punctuation from the word
        word = words[i]
        cleaned = ""
        for char in word:
            if char.isalnum():
                cleaned += char
        
        if cleaned == search_word.lower():
            count += 1
        i += 1
    return count

def identify_most_common_word(text):
    """Identifies the most common word. Returns None for empty string."""
    if not text or text.strip() == "":
        return None

    words = text.lower().split()
    cleaned_words = []
    for w in words:
        cw = "".join(c for c in w if c.isalnum())
        if cw:
            cleaned_words.append(cw)
            
    if not cleaned_words:
        return None

    most_common = ""
    max_count = 0
    unique_checked = []
    
    i = 0
    while i < len(cleaned_words):
        word = cleaned_words[i]
        if word not in unique_checked:
            current_count = 0
            for item in cleaned_words:
                if item == word:
                    current_count += 1
            
            if current_count > max_count:
                max_count = current_count
                most_common = word
            unique_checked.append(word)
        i += 1
        
    return most_common

def calculate_average_word_length(text):
    """Calculates average word length. Returns 0.0 for empty string."""
    if not text or text.strip() == "":
        return 0.0

    words = text.split()
    total_chars = 0
    valid_word_count = 0
    
    i = 0
    while i < len(words):
        word = words[i]
        cleaned_len = 0
        for char in word:
            if char.isalnum():
                cleaned_len += 1
        
        if cleaned_len > 0:
            total_chars += cleaned_len
            valid_word_count += 1
        i += 1
            
    if valid_word_count == 0:
        return 0.0
    return float(total_chars / valid_word_count)

def count_paragraphs(text):
    """Counts paragraphs based on empty lines. Empty string returns 1."""
    if not text or text.strip() == "":
        return 1
    
    # Split by double newline to detect paragraph breaks
    paragraphs = text.split('\n\n')
    count = 0
    for p in paragraphs:
        if p.strip() != "":
            count += 1
            
    return count if count > 0 else 1

def count_sentences(text):
    """Counts sentences ending in . ! or ? Empty string returns 1."""
    if not text or text.strip() == "":
        return 1
    
    count = 0
    i = 0
    while i < len(text):
        char = text[i]
        if char == '.' or char == '!' or char == '?':
            count += 1
        i += 1
    
    return count if count > 0 else 1

def main():
    # User prompts for input
    article = input("Enter news article: ")
    target = input("Enter word to count: ")
    
    # Execution
    print(f"Word Count: {count_specific_word(article, target)}")
    print(f"Most Common: {identify_most_common_word(article)}")
    print(f"Average Length: {calculate_average_word_length(article)}")
    print(f"Paragraphs: {count_paragraphs(article)}")
    print(f"Sentences: {count_sentences(article)}")

if __name__ == "__main__":
    main()

