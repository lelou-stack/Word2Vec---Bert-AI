import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel
import torch

# Load your data
df = pd.read_csv("C:\\Users\\hhafs\\OneDrive\\Bureau\\New folder (2)\\Scraping_Api\\server\\datajumia.csv", header=None, names=['Category', 'Transaction_Id'])

# Function to preprocess text
def preprocess_text(text):
    return text.lower()

# Apply preprocessing
df['Processed_Category'] = df['Category'].apply(preprocess_text)

# Tokenize sentences using BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

# Function to get BERT embeddings
def get_bert_embeddings(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()
    return embeddings

# Split data into train and test
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Load BERT model
model = BertModel.from_pretrained('bert-base-uncased')

# Get embeddings for train and test sentences
train_embeddings = train_df['Processed_Category'].apply(get_bert_embeddings)
test_embeddings = test_df['Processed_Category'].apply(get_bert_embeddings)

# Convert embeddings to NumPy arrays
train_embeddings = torch.stack(train_embeddings).numpy()
test_embeddings = torch.stack(test_embeddings).numpy()

# Calculate cosine similarity between train and test embeddings
similarity_matrix = cosine_similarity(test_embeddings, train_embeddings)

# Display the similarity matrix
print("Similarity Matrix:")
print(similarity_matrix)
