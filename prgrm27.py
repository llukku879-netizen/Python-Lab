def longestWord(words):
    max_length = len(words[0])
    for item in words:
        length = len(item)
        if length > max_length:
            max_length = length
    return max_length
words = input("Enter a list of words separated by spaces: ").split()
result = longestWord(words)
print(f"The length of the longest word is: {result}")
