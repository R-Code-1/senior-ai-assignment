import openai, os, numpy as np
openai.api_key = os.getenv("OPENAI_API_KEY")
def get_embedding(text):
    resp = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
    return resp['data'][0]['embedding']
def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))