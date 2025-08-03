def word_frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    for word, count in freq.items():
        print(f"{word}: {count}")

# Example usage:
input_str = input("Enter a string: ")
word_frequency(input_str)