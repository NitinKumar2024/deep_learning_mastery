import sys
import os

# System Setup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from preprocessing.tokenizer import rigorous_tokenize

def train_bigram_model(corpus):
    # The "Brain"
    # Format: { "current_word": { "next_word": count } }
    bigram_counts = {}
    
    print("Training Model...")
    
    for sentence in corpus:
        tokens = rigorous_tokenize(sentence)
        
        # We need to look at pairs: (Word i, Word i+1)
        # Loop from 0 to length-1
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            next_word = tokens[i+1]
            
            # --- LOGIC MISSING 1: POPULATE THE BRAIN ---
            # 1. Check if 'current_word' is already in bigram_counts.
            #    If not, add it as an empty dict {}.
            # 2. Inside that inner dict, check if 'next_word' exists.
            #    If yes, increment count (+1).
            #    If no, set count to 1.
            
            if current_word not in bigram_counts:
                bigram_counts[current_word] = {}
            
            if next_word in bigram_counts[current_word]:
                bigram_counts[current_word][next_word] += 1
            else:
                bigram_counts[current_word][next_word] = 1
            
    return bigram_counts

def predict_next_word(model, input_word):
    # Check if we know this word
    if input_word not in model:
        return None
    
    # Get the inner dictionary of possibilities
    # e.g., {'books': 2, 'code': 1}
    candidates = model[input_word]
    
    # --- LOGIC MISSING 2: FIND THE WINNER ---
    # Find the key (word) with the highest value (count).
    # Hint: You can use a loop, or the python function: max(dictionary, key=dictionary.get)
    best_word = max(candidates, key=candidates.get)
    
    return best_word

# --- TEST DATA ---
corpus = [
    "I read books.",
    "I read code.",
    "I read books.",
    "I love AI.",
    "AI is great."
]

# 1. Train
model = train_bigram_model(corpus)

# 2. Inspect "read"
print("\nStats for 'read':", model.get('read'))

# 3. Predict
test_word = "read"
prediction = predict_next_word(model, test_word)
print(f"Prediction: '{test_word}' -> '{prediction}'")

test_word_2 = "AI"
prediction_2 = predict_next_word(model, test_word_2)
print(f"Prediction: '{test_word_2}' -> '{prediction_2}'")