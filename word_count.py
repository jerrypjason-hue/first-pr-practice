def count_words(text):
    """Count the number of words in a string."""
    return len(text.split())


def most_common_word(text):
    """Return the most frequently occurring word in a string."""
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return max(counts, key=counts.get)
