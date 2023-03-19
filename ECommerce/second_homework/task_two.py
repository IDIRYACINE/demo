input_sentence = input("Enter a sentence: ")

words = input_sentence.split()

words.reverse()

output_sentence = " ".join(words)

print("Reversed words in the sentence:", output_sentence)
