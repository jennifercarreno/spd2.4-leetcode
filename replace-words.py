# LEETCODE QUESTION 648: REPLACE WORDS

"""
input: sentence and roots
output: sentence with some words replaced by corresponding roots

EXAMPLE:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
"""

def replaceWords(self, roots, sentence):
    # Dictionary of roots
    rootset = set(roots)

    def replace(word):
        # loops through each character in word
        for i in xrange(1, len(word)):

            # if selection of word is in rootset
            if word[:i] in rootset:
            # returns shortened word in rootset
                return word[:i]
        # returns the full word if part of it is not in rootset
        return word
    # joins words together to form sentences
    return " ".join(map(replace, sentence.split()))
    # return the sentence in new array
    # appened returned word to new array
    # join words in array to form sentence