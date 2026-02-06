**Topic:** Lecture 03 - Language Modeling & N-Grams


#### **1. Core Concept: Language Modeling**

* **Goal:** Calculate the probability of the *next word* in a sequence.
* **Mathematical Form:** 
* **Application:** Auto-complete, Search Suggestions, Speech Recognition (deciding if you said "write" or "right").

#### **2. The N-Gram Model**

An N-gram is a sequence of  words. We use them to approximate probability by looking at a limited history.

| Model | N | Context (Previous Words) | Example Input  Prediction |
| --- | --- | --- | --- |
| **Unigram** | 1 | 0 (No context) | (Blind Guess)  "the" |
| **Bigram** | 2 | 1 word | "New"  "York" |
| **Trigram** | 3 | 2 words | "Machine Learning"  "Model" |

#### **3. The Markov Assumption (The "Goldfish Memory")**

To make math possible, we assume the future depends **only** on the recent past (last  words), not the whole history.

* *Formula:*  (for Bigram).

#### **4. The Math: Maximum Likelihood Estimation (MLE)**

How we calculate the probability from data:

#### **5. Architectural Pros & Cons**

* **Pros:** Ultra-fast. No GPU required. Great for simple tasks (Spell check).
* **Cons:** **Zero Long-Term Memory.** If the subject of the sentence was 5 words ago, an N-gram model forgets it. (This is why we moved to RNNs and Transformers).