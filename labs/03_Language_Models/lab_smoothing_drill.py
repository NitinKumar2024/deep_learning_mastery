import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from preprocessing.tokenizer import rigorous_tokenize

# --- REUSING YOUR PREVIOUS LOGIC ---
def train_model(corpus):
    bigram_counts = {}
    vocab = set()
    
    for sentence in corpus:
        tokens = rigorous_tokenize(sentence)
        for token in tokens:
            vocab.add(token)
            
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            next_word = tokens[i+1]
            
            if current_word not in bigram_counts:
                bigram_counts[current_word] = {}
            
            if next_word in bigram_counts[current_word]:
                bigram_counts[current_word][next_word] += 1
            else:
                bigram_counts[current_word][next_word] = 1
                
    return bigram_counts, len(vocab)

# --- THE CHALLENGE: CALCULATE PROBABILITY ---
def calculate_sentence_probability(sentence, model, vocab_size, smoothing=False):
    tokens = rigorous_tokenize(sentence)
    total_probability = 1.0  # Start at 1 (multiplication identity)
    
    print(f"\nAnalyzing: '{sentence}' (Smoothing={smoothing})")
    
    for i in range(len(tokens) - 1):
        prev_word = tokens[i]
        curr_word = tokens[i+1]
        
        # 1. Get Counts
        # How many times did 'prev_word' appear as a start? (Sum of its drawer)
        prev_count = 0
        if prev_word in model:
            prev_count = sum(model[prev_word].values())
            
        # How many times did 'prev_word -> curr_word' happen?
        pair_count = 0
        if prev_word in model and curr_word in model[prev_word]:
            pair_count = model[prev_word][curr_word]
            
        # 2. Calculate Probability (THE MISSING LOGIC)
        if smoothing:
            # --- FORMULA 2: LAPLACE SMOOTHING ---
            # prob = (pair_count + 1) / (prev_count + vocab_size)
            # WRITE CODE HERE
            prob = (pair_count + 1) / (prev_count + vocab_size)
        else:
            # --- FORMULA 1: RAW PROBABILITY ---
            # prob = pair_count / prev_count
            # Handle ZeroDivisionError if prev_count is 0!
            # WRITE CODE HERE
            if prev_count == 0:
                prob = 0
            else:
                prob = pair_count / prev_count
            
        print(f"  P({curr_word} | {prev_word}) = {prob:.4f}")
        total_probability *= prob
        
    return total_probability

# --- TEST ---
corpus = ["I love AI", "I love code"]
model, vocab_size = train_model(corpus)
print(f"Vocabulary Size: {vocab_size}")

# Test 1: Known Sentence (Should work)
p1 = calculate_sentence_probability("I love AI", model, vocab_size, smoothing=False)
print(f"Final Probability: {p1:.4f}")

# Test 2: Unknown Sentence (Should crash to 0 without smoothing)
p2 = calculate_sentence_probability("I love Zebra", model, vocab_size, smoothing=False)
print(f"Final Probability: {p2:.4f}")

# Test 3: Unknown Sentence WITH Smoothing (Should survive)
p3 = calculate_sentence_probability("I love Zebra", model, vocab_size, smoothing=True)
print(f"Final Probability: {p3:.4f}")