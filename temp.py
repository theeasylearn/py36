# verify.py
import spacy, json
from spacy.tokens import DocBin

# Check JSON
with open("training_data.json") as f:
    data = json.load(f)
print(f"JSON examples: {len(data)}")   # should be 11

# Check .spacy file
nlp = spacy.blank("en")
db = DocBin().from_disk("train.spacy")
docs = list(db.get_docs(nlp.vocab))
print(f"Docs in train.spacy: {len(docs)}")   # should be 11

total_ents = sum(len(doc.ents) for doc in docs)
print(f"Total labeled entities: {total_ents}")  # should be 25+

for doc in docs:
    print(f"  '{doc.text[:45]}' → {[(e.text, e.label_) for e in doc.ents]}")