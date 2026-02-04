import sys
import os

# --- SYSTEM SETUP to find your 'src' folder ---
# This tells Python: "Look for modules in the folder one level up"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from preprocessing.tokenizer import rigorous_tokenize

# --- THE LOGIC ---
def generate_bow(corpus):
    # Step 1: Tokenization (Using YOUR custom module)
    print("Step 1: Tokenizing...")
    tokenized_sentences = []
    
    # We define some terms we want to protect in this specific corpus
    my_tech_terms = ["AI", "Python"] 
    
    for sentence in corpus:
        # CALLING YOUR FUNCTION HERE
        tokens = rigorous_tokenize(sentence, my_tech_terms)
      
        
        # Lowercase everything? 
        # CAREFUL: If we lowercase "AI", it becomes "ai". 
        # But our tokenizer protected "AI". 
        # Decision: Let's keep case for now to respect the tokenizer.
        tokenized_sentences.append(tokens)
    
    # Step 2: Build Vocabulary (Unique Words)
    vocab_set = set()
    
    for tokens in tokenized_sentences:
        # --- YOUR CODE HERE ---
        # Add all tokens to the set
        for vocab in tokens:

            vocab_set.add(vocab)
      
        
    vocab = sorted(list(vocab_set))
    print(f"Vocabulary ({len(vocab)} words): {vocab}")
    print(vocab_set)
    
    
    # Step 3: Create Vectors
    vectors = []
    for tokens in tokenized_sentences:
        # Create a vector of Zeros
        vector = [0] * len(vocab)
        
        # --- YOUR CODE HERE ---
        # 1. Loop through the *Vocabulary* (to maintain order).
        # 2. Count how many times that vocab word appears in the current 'tokens'.
        # 3. Store that count in the vector.
        # Hint: You can use tokens.count(word) 

        for i, word in enumerate(vocab):
            count = tokens.count(word) 
            vector[i] = count
        
        vectors.append(vector)
        
    return vectors

# --- TEST DATA ---
corpus = [
    "I love AI and I love code.",
    "I code with Python.",
    "AI is the future!"
]

# Execute
vectors = generate_bow(corpus)

print("\n--- Final Matrix ---")
for v in vectors:
    print(v)