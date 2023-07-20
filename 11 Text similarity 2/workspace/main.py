import sys
from semantic_similarity_calculator import SemanticSimilarityCalculator
from embedding_model import EmbeddingModel

def main():
    sentences = sys.argv[1:]
    if len(sentences) != 2:
        print('Please provide exactly two sentences.')
        return

    embedding_model = EmbeddingModel()
    calculator = SemanticSimilarityCalculator(embedding_model)
    similarity = calculator.calculate_similarity(*sentences)
    print(f'The semantic similarity between the sentences is {similarity}.')

if __name__ == '__main__':
    main()
