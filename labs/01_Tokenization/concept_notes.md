**Topic:** Lecture 02 - Text Processing & Tokenization

---

#### **1. Core Definitions**

* **Corpus:** The entire collection of text data you are using (e.g., "All resumes in the database").
* **Token:** The atomic unit of text processing. Can be a word, a character, or a sub-word chunk.
* **Vocabulary:** The list of *unique* tokens the model understands.
* **`<UNK>` (Unknown Token):** A placeholder for any word *not* in the vocabulary.
* *Critical Risk:* If key technical terms (e.g., "Kubernetes") become `<UNK>`, the model loses the ability to identify that skill.



#### **2. The 3 Levels of Tokenization**

| Level | Method | Example: "smart-ai" | Pros | Cons |
| --- | --- | --- | --- | --- |
| **Word-Level** | Split by space/symbol | `['smart', '-', 'ai']` | Human readable. | Huge vocabulary. Fails on "smart-ai" (compounds). |
| **Char-Level** | Split every char | `['s','m','a','r','t'...]` | Small vocabulary. No `<UNK>`. | Loss of meaning. Computationally expensive (long sequences). |
| **Sub-Word** | **(Modern Std)** Split chunks | `['smart', '##ai']` | Best balance. Handles unseen words. | Complex to implement from scratch. |

#### **3. The "Engineering Gap" (Standard vs. Domain)**

Standard libraries (NLTK, default split) fail on technical text.

* **The Failure Case:** `C++`  `['C', '+', '+']`.
* *Result:* "C++" (Skill) becomes indistinguishable from "C" (Letter) + Math.


* **The Solution:** **Priority Tokenization**.
* *Logic:* Check for "Protected Terms" (Gold List) *first*. If no match, *then* split by standard rules.



#### **4. Modern Pre-processing Rules (CTO Guidelines)**

* **Lowercasing:**
* *General Rule:* Use for Search/IR (Information Retrieval).
* *Exception:* **DO NOT** use for Code/Technical Domains. (Distinguishes "Go" the language vs. "go" the verb).


* **Stop Words (is, the, at):**
* *General Rule:* In the Transformer/LLM era, **KEEP THEM**.
* *Reason:* Attention mechanisms use stop words to understand sentence structure and intent.



#### **5. Architectural Decision Matrix**

* **If building a Resume Parser (Smart Edu AI):** Use **Dictionary-Based Tokenization** (Regex with a Golden List of skills). precision is paramount.
* **If building a Chatbot (Sutra):** Use **Sub-Word Tokenization** (BPE/WordPiece). Generalization is paramount.