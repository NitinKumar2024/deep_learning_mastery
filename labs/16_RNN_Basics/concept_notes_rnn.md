**Topic:** Lecture 16 - The Math of an RNN


#### **1. The Core Idea**

Standard neural networks process fixed-size inputs with no memory. RNNs process sequences by passing a continuous memory vector (Hidden State) from one time step to the next.

#### **2. The Three Weight Matrices**

An RNN uses the exact same weights over and over again at every time step:

* **$W_{xh}$:** The weight matrix that processes the current Input Word.
* **$W_{hh}$:** The weight matrix that processes the previous Hidden State (The Memory).
* **$W_{hy}$:** The weight matrix that calculates the final Output Prediction.

#### **3. The RNN Equations (The Forward Pass)**

At any time step $t$, the network performs two calculations:

**Step 1: Update the Memory (Hidden State)**


$$h_t=\tanh((W_{hh}\cdot h_{t-1})+(W_{xh}\cdot x_t)+b_h)$$


*(Translation: Multiply old memory by its weights, multiply new word by its weights, add them together, and squash it through a Tanh curve between -1 and 1).*

**Step 2: Make a Prediction**


$$y_t=(W_{hy}\cdot h_t)+b_y$$


*(Translation: Multiply our brand new memory by the output weights to guess the next word).*

---


**Topic:** Lecture 18 & 19 - Seq2Seq & Beam Search


#### **1. Seq2Seq (Encoder-Decoder)**

* **Purpose:** Translating sequences where input and output lengths differ (Translation, Summarization).
* **Encoder:** Reads the input and compresses the entire sequence into a single memory state called the **Context Vector**.
* **Decoder:** Unpacks the Context Vector to generate a new sequence, stopping only when it predicts an `<END>` token.

#### **2. Decoding Strategies**

* **Greedy Search:** Selects the single highest probability word at each step. Fast, but often leads to poor overall sentences because it cannot look ahead.
* **Beam Search:** Tracks the top $K$ most probable sequences at every step. It calculates the *joint probability* (multiplying probabilities together) to find the globally optimal sentence.

---


**Topic:** Lecture 20 - LSTMs & The Vanishing Gradient

#### **1. The Vanishing Gradient Problem**

* Standard RNNs suffer from short-term memory. Over long sequences, repeated matrix multiplication causes early inputs to mathematically vanish toward zero.
* They cannot connect context over long distances.

#### **2. LSTM Architecture**

* **Cell State ($C_t$):** The "Long Term Memory" highway. Information flows continuously without being constantly squashed by weights.
* **The Gates (Using Sigmoid):** Gates use a Sigmoid activation to output a number exactly between $0.0$ and $1.0$.
* `1.0` means "Let everything through" (Keep memory).
* `0.0` means "Shut the valve completely" (Erase memory).



---

