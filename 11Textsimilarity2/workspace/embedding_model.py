from transformers import AutoTokenizer, AutoModel

class EmbeddingModel:
    def __init__(self, model_name='distilbert'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def get_embedding(self, sentences):
        inputs = self.tokenizer(sentences, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model(**inputs)
        embeddings = outputs[0].mean(1).detach().numpy()
        return embeddings