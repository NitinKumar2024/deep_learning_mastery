#### **1. Data Structures**

* **NumPy:** `np.array`
* **PyTorch:** `torch.tensor` (Can be moved to a GPU).

#### **2. Neural Network Layers (The `nn` module)**

Instead of writing the matrix math manually, we use `torch.nn` (Neural Network) blocks.

* **`nn.Linear(in, out)`:** The exact Perceptron math you built in Week 2 ($X \cdot W + b$).
* **`nn.Embedding(vocab, dim)`:** The matrix lookup table from Week 3 that converts One-Hot vectors into dense Word Embeddings.
* **`nn.LSTM(in, hidden)`:** The bank account/memory loop from Week 4. It handles the $W_{xh}$ and $W_{hh}$ matrices automatically over time.

#### **3. The Training Loop**

* **Forward Pass:** You just pass data through the blocks. `output = model(input)`
* **Calculate Error:** `loss = loss_function(output, target)`
* **Backward Pass (Calculus):** `loss.backward()`
* **Update Weights:** `optimizer.step()` (This is the $w_{new} = w_{old} - (\alpha \cdot \text{gradient})$ equation).

---
