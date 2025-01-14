def longest_word(sentence):
    words = sentence.split(" ")
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

sentence = input("Enter a sentence: ")
print(f"The length of the longest word is {longest_word(sentence)}")
