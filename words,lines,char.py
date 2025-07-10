#write a program to count the number of words, lines, and characters in a user-provided sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()    
num_words = len(words)
num_lines = sentence.count('\n') + 1 if sentence else 0
num_chars = len(sentence)
print("Number of words:", num_words)
print("Number of lines:", num_lines)
print("Number of characters:", num_chars)