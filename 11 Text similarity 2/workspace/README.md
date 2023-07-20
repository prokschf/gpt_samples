Given the requirements, we will need the following core classes, functions, and methods:

1. `EmbeddingModel`: This class will be responsible for loading the pre-trained embedding model and providing a method to get the embeddings for a given sentence.

2. `SemanticSimilarityCalculator`: This class will be responsible for calculating the semantic similarity between two sentences. It will use an instance of `EmbeddingModel` to get the embeddings for the sentences and then calculate the cosine similarity between them.

3. `main`: This function will be the entry point of the program. It will take two sentences as input, use an instance of `SemanticSimilarityCalculator` to calculate the semantic similarity between them, and then print the result.

Now, let's write the code for each of these components.

requirements.txt
