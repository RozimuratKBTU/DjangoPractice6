"""file2.py — коллекция функций для работы со строками"""
#"""kkfkkfkkfk"""
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]

def word_count(s):
    words = s.split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

class TextStats:
    def __init__(self, text):
        self.text = text
    def length(self):
        return len(self.text)
    def words(self):
        return len(self.text.split())
    def unique_words(self):
        return len(set(self.text.split()))

def sample_usage():
    s = "Madam Im Adam"
    print("rev:", reverse_string(s))
    print("palindrome:", is_palindrome(s))
    print("counts:", word_count("hello hello world"))
    ts = TextStats("hello world hello")
    print("length:", ts.length(), "words:", ts.words(), "unique:", ts.unique_words())

if __name__ == "__main__":
    sample_usage()
    # дополнительные строки
    for i in range(8):
        print("extra", i)
