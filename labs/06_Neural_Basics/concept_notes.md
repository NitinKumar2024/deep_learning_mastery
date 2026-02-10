**Topic:** Lecture 06 - The Artificial Neuron (Perceptron)

#### **1. The Biological Inspiration**

* **Neuron:** The brain's basic computing unit.
* **Mechanism:** Accumulates signals from neighbors; if the sum exceeds a threshold, it fires.

#### **2. The Perceptron (Mathematical Model)**

The simplest possible Neural Network (1 neuron).

* **Formula:**  $z = \sum (x_i \cdot w_i) + b$
* **Components:**
* **Inputs (x):** The features (data).
* **Weights ($w$):** The importance (strength) of each connection.
* **Bias ($b$):** An extra value that shifts the activation (allows the neuron to fire even if inputs are zero).
* **Activation Function:** The decision rule (e.g., Step Function: if $z > 0$, output 1).



#### **3. The Goal of "Learning"**

We do **not** write code to solve the problem.
We write code to **find the weights ($w$)** that solve the problem.

#### **4. The Training Cycle (Supervised Learning)**

1. **Forward Pass:** Calculate output based on current weights.
2. **Loss:** Compare output to the actual answer (Ground Truth).
3. **Update:** Adjust weights slightly to reduce the error.
4. **Repeat:** Do this until the error is low.