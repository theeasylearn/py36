# pip install gensim
from gensim.models import Word2Vec

# Step 1: Prepare sentences (list of words)
sentences = [
    ["natural", "language", "processing", "is", "great"],
    ["deep", "learning", "changed", "nlp"],
    ["word", "embeddings", "are", "very", "useful"],
    ["transformers", "are", "powerful", "for", "nlp"],
]

# Step 2: Train the model
model = Word2Vec(
    sentences=sentences, 
    vector_size=100,   # Size of each word vector
    window=3,          # How many words before/after to look at
    min_count=1,       # Ignore words that appear less than this
    sg=1,              # 1 = Skip-gram (better for small data)
    epochs=10          # How many times to read the data
)

# Step 3: Use the model
print("Words similar to 'nlp':")
print(model.wv.most_similar("nlp", topn=5))
