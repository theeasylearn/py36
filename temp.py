# python -m spacy download en_core_web_sm
import spacy

# Load a pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Process text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")

# Access annotations
for token in doc:
    print(token.text, token.pos_, token.dep_)

# Named entities
for ent in doc.ents:
    print(ent.text, ent.label_)