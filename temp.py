from nltk.corpus import wordnet as wn

word = "happy"

print(f"All meanings and synonyms for '{word}':\n")

for syn in wn.synsets(word):
    print(f"Meaning: {syn.definition()}")
    print(f"Synonyms: {syn.lemma_names()}")
    
    # Get Antonyms
    for lemma in syn.lemmas():
        antonyms = lemma.antonyms()
        if antonyms:
            print(f"Antonyms: {[ant.name() for ant in antonyms]}")
    print("-" * 50)

    