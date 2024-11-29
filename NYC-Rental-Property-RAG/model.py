import pandas as pd
import torch
from transformers import DistilBertTokenizer, DistilBertModel, GPT2LMHeadModel, GPT2Tokenizer
import faiss

data_path = 'ny_rental_data.csv'
df = pd.read_csv(data_path)
df_cleaned = df[['latitude', 'longitude', 'neighbourhood', 'room_type', 'price', 'days_occupied_in_2019', 'minimum_nights', 'number_of_reviews']].copy()

df_cleaned.dropna(inplace=True)
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertModel.from_pretrained("distilbert-base-uncased")

def get_embeddings(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1) 
    return embeddings

embeddings = get_embeddings(df_cleaned['neighbourhood'].head(10).tolist())
embeddings_np = embeddings.numpy()

index = faiss.IndexFlatL2(embeddings_np.shape[1])  # L2 distance for similarity search
index.add(embeddings_np)

gpt_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
gpt_model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_response(query, context):
    input_text = f"Context: {context}\nQuestion: {query}\nAnswer:"
    inputs = gpt_tokenizer.encode(input_text, return_tensors="pt")
    outputs = gpt_model.generate(inputs, max_length=512, num_return_sequences=1, no_repeat_ngram_size=2)
    return gpt_tokenizer.decode(outputs[0], skip_special_tokens=True)


def limit_response_length(response, max_length=1500):
    truncated_response = response[:max_length]
    last_punctuation_pos = max(truncated_response.rfind(punc) for punc in ['.', '!', '?'])

    if last_punctuation_pos != -1:
        truncated_response = truncated_response[:last_punctuation_pos + 1]
    else:
        truncated_response = truncated_response.rstrip().rsplit(' ', 1)[0]
    return truncated_response.strip()
    
def get_relevant_context(query, top_k=3):
    query_embedding = get_embeddings([query]).numpy()
    distances, indices = index.search(query_embedding, top_k)
    contexts = df_cleaned['neighbourhood'].iloc[indices[0]].tolist()
    return " ".join(contexts)  # Combine relevant contexts into a single string


def answer_query(query):
    context = get_relevant_context(query)
    answer = generate_response(query, context)
    answer = limit_response_length(answer)
    
    return answer