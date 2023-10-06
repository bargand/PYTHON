from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

def perform_wsd(sentence, ambiguous_word):
    tokens = word_tokenize(sentence)
    best_sense = lesk(tokens, ambiguous_word)
    if best_sense is not None:
        return best_sense.definition()
    else:
        return "Could not determine the correct sense."

# Example usage
sentence = "He went to the bank to deposit his money."
ambiguous_word = "bank"
meaning = perform_wsd(sentence, ambiguous_word)
print(f"The correct meaning of '{ambiguous_word}' in this context is: {meaning}")
