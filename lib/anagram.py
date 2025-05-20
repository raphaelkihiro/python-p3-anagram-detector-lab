# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for candidate in word_list:
            cand_lower = candidate.lower()
            if cand_lower != self.word and sorted(cand_lower) == self.sorted_word:
                matches.append(candidate)
        return matches