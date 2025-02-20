"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""

starting_letters = ["c", "t", "b"]
middle_letters = ["a", "o"]
ending_letters = ["p", "t", "n"]
def print_three_letter_words():
        for j in range (len(starting_letters)):
            for k in range (len(middle_letters)):
                for l in range (len(ending_letters)):
                    print(starting_letters[j]+middle_letters[k]+ending_letters[l])
                    print(" ")
print_three_letter_words()
