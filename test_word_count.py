from word_count import count_words, most_common_word


def test_count_words_basic():
    assert count_words("hello world") == 2


def test_count_words_single():
    assert count_words("hello") == 1


def test_most_common_word():
    assert most_common_word("the cat sat on the mat") == "the"
