from scipy.spatial.distance import cosine
from embedding_model import EmbeddingModel

class SemanticSimilarityCalculator:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def calculate_similarity(self, sentence1, sentence2):
        embedding1 = self.embedding_model.get_embedding(sentence1)
        embedding2 = self.embedding_model.get_embedding(sentence2)
        return 1 - cosine(embedding1, embedding2)
