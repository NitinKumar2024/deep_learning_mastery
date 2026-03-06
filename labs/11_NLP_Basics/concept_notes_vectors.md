**Topic:** Lecture 11 - Word Representation (NLP)

#### **1. The Problem with Text**

Neural Networks only process numbers (Matrix Multiplication). They cannot read strings like `"Doctor"`.

#### **2. The Old Solution: One-Hot Encoding**

* **Mechanism:** Create a giant array the size of your entire dictionary (e.g., 10,000 words). Put a `1` at the word's alphabetical index, and `0` everywhere else.
* **Flaw:** It is extremely inefficient (Sparse) and **contains no semantic meaning**. In One-Hot, the mathematical distance between "Fever" and "Cough" is the exact same as "Fever" and "Car".

#### **3. The Modern Solution: Word Embeddings (Vectors)**

* **Mechanism:** Represent every word as a dense array of decimal numbers (usually 100 to 300 dimensions).
* **The Magic:** These numbers act as coordinates in geometric space.
* **Semantic Similarity:** Words with similar meanings have similar coordinates and cluster together.
* **Vector Arithmetic:** We can do math on meanings. $V_{\text{King}} - V_{\text{Man}} + V_{\text{Woman}} \approx V_{\text{Queen}}$


---


**Topic:** Lecture 12 - Skip-Gram Architecture

#### **1. The Dimensions (The Setup)**

* **$V$ (Vocabulary Size):** The total number of unique words in our dictionary (e.g., 10,000).
* **$N$ (Embedding Size):** The number of dimensions we want our vectors to have (e.g., 300).

#### **2. The Network Architecture**

Skip-Gram is a shallow neural network with only one hidden layer and no activation function in the hidden layer (it is purely linear).

* **Input Layer (Size $1 \times V$):** The target word, represented as a One-Hot Encoded vector. (Mostly zeros, with a single `1`).
* **Hidden Layer Weight Matrix $W_1$ (Size $V \times N$):** This is the magic matrix. Each row in this matrix represents the $N$-dimensional vector for a specific word.
* **Output Layer Weight Matrix $W_2$ (Size $N \times V$):**
Maps the hidden vector back to the vocabulary size.
* **Final Output (Size $1 \times V$):**
Uses a **Softmax** function to output the probability of every word in the dictionary being a context word for the input.

---


**Topic:** Lecture 14 - FastText & The OOV Problem


#### **1. The Out of Vocabulary (OOV) Problem**

* Standard Word2Vec assigns one vector per word.
* If a word was not in the training data (a typo, a rare word, or a new slang term), the network cannot process it and fails.

#### **2. The FastText Solution (Sub-word Information)**

* **Mechanism:** Represent words as a "bag of character n-grams" alongside the word itself.
* **Boundary Markers:** Add `<` and `>` to distinguish prefixes and suffixes (e.g., `<her` is different from `her`).
* **Vector Calculation:** The embedding for a word is the **sum** of its n-gram embeddings.
* **Advantage:** It can construct highly accurate vectors for words it has never seen before by combining the vectors of familiar sub-words. It is highly robust against typos and morphological variations (e.g., learn, learning, learned).

---

**Topic:** Lecture 15 - Cross-Lingual Embeddings


#### **1. The Multilingual Disconnect**

Models trained on different languages create independent vector spaces. The coordinates do not match, even for exact translations.

#### **2. Mapping / Alignment (The Procrustes Method)**

* **The Goal:** Learn a transformation matrix ($W$) that rotates and scales the Source Language space to align with the Target Language space.
* **Anchor Words:** We use a small, bilingual dictionary (e.g., 500 common words) as anchor points.
* **The Math:** We multiply the source word vector ($X$) by the transformation matrix ($W$) to get it as close as possible to the target word vector ($Y$).
* **Formula:** Minimize the distance between $(X \cdot W)$ and $Y$.

---