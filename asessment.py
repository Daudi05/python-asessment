

def is_letter_or_digit(char):
    if char >= 'a' and char <= 'z':
        return True
    if char >= 'A' and char <= 'Z':
        return True
    if char >= '0' and char <= '9':
        return True
    return False


def to_lower(text):
    result = ""
    i = 0
    while i < len(text):
        c = text[i]
        if c >= 'A' and c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c
        i += 1
    return result


def extract_words(text):
    words = []
    current = ""
    i = 0

    while i < len(text):
        c = text[i]
        if is_letter_or_digit(c):
            current += c
        else:
            if current != "":
                words.append(current)
                current = ""
        i += 1

    if current != "":
        words.append(current)

    return words


def is_blank(text):
    i = 0
    while i < len(text):
        if text[i] != ' ' and text[i] != '\n' and text[i] != '\t':
            return False
        i += 1
    return True



def count_specific_word(text: str, search_word: str) -> int:
    if text == "" or search_word == "":
        return 0

    words = extract_words(to_lower(text))
    search_word = to_lower(search_word)

    count = 0
    for word in words:
        if word == search_word:
            count += 1

    return count


def identify_most_common_word(text: str):
    if is_blank(text):
        return None

    words = extract_words(to_lower(text))

    if len(words) == 0:
        return None

    counts = {}

    i = 0
    while i < len(words):
        word = words[i]
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        i += 1

    most_common = None
    highest = 0

    for word in counts:
        if counts[word] > highest:
            highest = counts[word]
            most_common = word

    return most_common


def calculate_average_word_length(text: str) -> float:
    if is_blank(text):
        return 0.0

    words = extract_words(text)

    if len(words) == 0:
        return 0.0

    total = 0
    i = 0

    while i < len(words):
        total += len(words[i])
        i += 1

    return total / len(words)


def count_paragraphs(text: str) -> int:
    if is_blank(text):
        return 1

    count = 0
    in_paragraph = False
    i = 0

    while i < len(text):
        c = text[i]

        if c != '\n':
            if not in_paragraph:
                count += 1
                in_paragraph = True
        else:
            in_paragraph = False

        i += 1

    return count


def count_sentences(text: str) -> int:
    if is_blank(text):
        return 1

    count = 0

    for c in text:
        if c == '.' or c == '!' or c == '?':
            count += 1

    return count




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
    print("Occurrences of '" + search_word + "': " + str(word_count))
    print("Most common word: " + str(most_common))
    print("Average word length: " + str(round(avg_length, 2)))
    print("Number of paragraphs: " + str(paragraph_count))
    print("Number of sentences: " + str(sentence_count))
    print("\n===== End of Analysis =====\n")


if __name__ == "__main__":
    main()
