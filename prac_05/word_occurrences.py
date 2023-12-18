text = input("Enter a string: ")

words = text.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

longest_word = max(word_counts.keys(), key=len)

for word in sorted(word_counts):
    print(f"{word:>{len(longest_word)}} : {word_counts[word]}")

