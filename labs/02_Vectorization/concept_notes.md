**Topic:** Lecture 03 - Vectorization (BoW & One-Hot)

#### **1. The Goal: Text  Math**

Neural networks require numerical input. Vectorization turns strings into arrays of numbers.

#### **2. Method A: One-Hot Encoding**

* **Concept:** Each word gets a unique index. A vector is all zeros except for a single `1` at that index.
* **Visual:**
* `Apple`  `[1, 0, 0]`
* `Banana`  `[0, 1, 0]`


* **Flaw:** No relationship. The mathematical distance between "Apple" and "Banana" is the same as "Apple" and "Car".

#### **3. Method B: Bag of Words (BoW)**

* **Concept:** Represents a sentence by counting word frequencies. Ignores grammar and order.
* **Algorithm:**
1. Build Vocabulary (Unique words).
2. Count occurrences of each vocab word in the sentence.


* **The Matrix:**
* Rows = Sentences (Documents).
* Columns = Words (Vocabulary).
* Values = Frequency Counts.



#### **4. Critical Engineering Flaws (The "Why we moved to Deep Learning")**

1. **Sparsity (Memory Issue):**
* Vocab size = 50,000. Sentence length = 10.
* Vector contains 49,990 zeros. This wastes huge amounts of RAM.


2. **Loss of Context (Meaning Issue):**
* "Dog bites Man" vs "Man bites Dog".
* Both produce the **exact same vector**. The model cannot distinguish subject vs. object.