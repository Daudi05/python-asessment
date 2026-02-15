# pythonAssessment.py

def count_specific_word(text, search_word):
    """Counts occurrences of a specific word (case-insensitive)."""
    if not text or not search_word:
        return 0
    
    words = text.split()
    count = 0
    i = 0
    while i < len(words):
        # Remove non-alphanumeric characters for comparison
        cleaned = ""
        for char in words[i]:
            if char.isalnum():
                cleaned += char
        
        if cleaned.lower() == search_word.lower():
            count += 1
        i += 1
    return count

def identify_most_common_word(text):
    """Identifies the most common word. Returns None for empty string."""
    if not text or text.strip() == "":
        return None

    raw_words = text.split()
    words = []
    for w in raw_words:
        cw = ""
        for char in w:
            if char.isalnum():
                cw += char
        if cw:
            words.append(cw.lower())
            
    if not words:
        return None

    most_common = None
    max_count = 0
    checked = []
    
    i = 0
    while i < len(words):
        word = words[i]
        # Manual check if word was already processed
        already_seen = False
        for seen in checked:
            if seen == word:
                already_seen = True
        
        if not already_seen:
            current_count = 0
            for item in words:
                if item == word:
                    current_count += 1
            
            # Tie-breaker: keep the first one found that hits max_count
            if current_count > max_count:
                max_count = current_count
                most_common = word
            checked.append(word)
        i += 1
    return most_common

def calculate_average_word_length(text):
    """Calculates average word length. Excludes punctuation."""
    if not text or text.strip() == "":
        return 0
    
    words = text.split()
    total_chars = 0
    word_count = 0
    
    i = 0
    while i < len(words):
        cleaned_word = ""
        for char in words[i]:
            if char.isalnum():
                cleaned_word += char
        
        if len(cleaned_word) > 0:
            total_chars += len(cleaned_word)
            word_count += 1
        i += 1
            
    if word_count == 0:
        return 0
    return total_chars / word_count

def count_paragraphs(text):
    """Counts paragraphs based on empty lines. Returns 1 for empty strings."""
    if not text or text.strip() == "":
        return 1
    
    # Define paragraphs based on empty lines (double newline)
    parts = text.split('\n\n')
    valid_paragraphs = 0
    for p in parts:
        if p.strip() != "":
            valid_paragraphs += 1
            
    return valid_paragraphs if valid_paragraphs > 0 else 1

def count_sentences(text):
    """Counts sentences ending in . ! or ? Returns 1 for empty strings."""
    if not text or text.strip() == "":
        return 1
    
    count = 0
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            count += 1
        i += 1
    
    return count if count > 0 else 1

def main():
    # User prompts
    article = input("Paste news article: ")
    search = input("Word to count: ")
    
    # Display results as requested by IO tests
    print(f"Word count: {count_specific_word(article, search)}")
    print(f"Most common: {identify_most_common_word(article)}")
    print(f"Average Length: {calculate_average_word_length(article)}")
    print(f"Paragraphs: {count_paragraphs(article)}")
    print(f"Sentences: {count_sentences(article)}")

if __name__ == "__main__":
    main()
