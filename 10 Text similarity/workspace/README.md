The architecture of the program will consist of the following core classes, functions, and methods:

1. `SentenceEmbedder`: This class will be responsible for loading the pre-trained model and generating embeddings for the input sentences. It will have the following methods:
    - `__init__`: This method will load the pre-trained model.
    - `get_embedding`: This method will take a sentence as input and return its embedding.

2. `SimilarityCalculator`: This class will be responsible for calculating the cosine similarity between two sentence embeddings. It will have the following methods:
    - `calculate`: This method will take two sentence embeddings as input and return their cosine similarity.

3. `main`: This function will be the entry point of the program. It will take two sentences as input, generate their embeddings using `SentenceEmbedder`, calculate their similarity using `SimilarityCalculator`, and return the similarity.

Now, let's write the code for each file.

**requirements.txt**
