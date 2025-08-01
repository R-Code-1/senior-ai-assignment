from utils.embeddings import get_embedding, cosine_similarity
class TopicManager:
    def __init__(self):
        self.known = {}
    def load_seed_topics(self, seed_list):
        for t in seed_list:
            self.known[t] = get_embedding(t)
    def map_topic(self, new_topic):
        emb = get_embedding(new_topic)
        for existing, e_emb in self.known.items():
            if cosine_similarity(e_emb, emb) > 0.9:
                return existing
        self.known[new_topic] = emb
        return new_topic