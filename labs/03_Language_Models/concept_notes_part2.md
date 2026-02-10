**Topic:** Lecture 04 - Smoothing (Laplace / Add-One)


#### **1. The Problem: Sparsity**

* **Scenario:** If a specific bigram (e.g., "love Zebra") never appeared in the training data, its count is 0.
* **Math Fail:** If one count is 0, the probability of the entire sentence becomes 0 (due to multiplication).
* **Impact:** The model thinks any new sequence is "impossible."

#### **2. The Solution: Laplace Smoothing (Add-One)**

We artificially inflate the counts so that no event has zero probability.

* **The Formula:**


* **Variables:**
* ****: Ensures the numerator is at least 1 (never zero).
* ** (Vocabulary Size)**: The total number of *unique* words in the training data. We add this to the denominator to balance the math (since we added a theoretical +1 for every possible word in the universe).



#### **3. Evaluating Models: Perplexity**

* **Concept:** A measurement of how "surprised" the model is by new text.
* **Goal:** Lower is better.
* **Perplexity 1:** The model knows exactly what comes next (Perfect).
* **Perplexity 100:** The model is as confused as if it had to guess from 100 options.