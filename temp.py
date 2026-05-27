import spacy
from spacy.language import Language

# Step 1: Define your custom component
@Language.component("custom_sentiment")
def custom_sentiment_component(doc):
    """Simple rule-based sentiment: count happy/sad words"""
    happy_words = {"good", "great", "excellent", "awesome", "happy"}
    sad_words = {"bad", "terrible", "awful", "sad", "poor"}
    
    happy_count = sum(1 for token in doc if token.lower_ in happy_words)
    sad_count = sum(1 for token in doc if token.lower_ in sad_words)
    
    # Add custom attribute to the Doc
    doc._.sentiment_score = happy_count - sad_count
    doc._.sentiment_label = "Positive" if doc._.sentiment_score > 0 else "Negative" if doc._.sentiment_score < 0 else "Neutral"
    
    return doc

# Step 2: Register the component so spaCy knows it
nlp = spacy.load("en_core_web_sm")

# Step 3: Add it to the pipeline
nlp.add_pipe("custom_sentiment", last=True)   # You can use first=True, before="ner", after="parser", etc.

print("Updated pipeline:", nlp.pipe_names)
# → ['tok2vec', 'tagger', ..., 'ner', 'custom_sentiment']