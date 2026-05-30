import spacy

nlp = spacy.load("en_core_web_sm")

print("Pipeline components:", nlp.pipe_names)
print("\nFull pipeline with details:")
for name, component in nlp.pipeline:
    print(f"→ {name:<15} : {component}")