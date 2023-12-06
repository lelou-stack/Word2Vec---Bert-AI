import pandas as pd
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('data.csv', header=None, names=['Category', 'Transaction_Id'])

# Preprocess data
sentences = df.groupby('Transaction_Id')['Category'].apply(list).tolist()

# Train Word2Vec model on the training data
model = Word2Vec(sentences=sentences, vector_size=100, window=10, min_count=1, workers=4, epochs=100)

# Save the model
model.save("word2vec.model")

# Load the Word2Vec model
model = Word2Vec.load("word2vec.model")

# Example: Get similar words for a given keyword
target_keyword = "Grooming Brushes"


# Check if the target keyword is in the vocabulary
if target_keyword in model.wv:
    # Get similar words based on the target keyword
    similar_words = model.wv.most_similar(target_keyword, topn=5)

    # Print the results
    print(f"Words related to '{target_keyword}':")
    for word, similarity in similar_words:
        if model.wv.similarity(target_keyword, word) >= 0.5:
            print(f"{word}: {similarity}")
else:
    print(f"'{target_keyword}' is not present in the vocabulary.")
