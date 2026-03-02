**Topic:** Lecture 08 - Deep Neural Networks (MLPs)


#### **1. The Limitation of One Neuron**

* **Linear Separability:** A single Perceptron can only draw a **straight line**.
* **The XOR Problem:** Data points arranged in a checkerboard pattern cannot be separated by a single line. This requires a non-linear boundary (curves or multiple lines).

#### **2. The Solution: Multi-Layer Perceptron (MLP)**

We stack neurons in layers.

* **Input Layer:** Receives raw data. No computation.
* **Hidden Layer(s):** The intermediate layers where computation happens. "Deep Learning" simply means having many hidden layers.
* **Output Layer:** Produces the final prediction.

**Why "Hidden"?**
Because we don't see their inputs or outputs directly. They are internal to the machine. They transform the data into a shape that the Output Layer can easily separate.

#### **3. The Secret Sauce: Non-Linearity (Activation Functions)**

If we only used linear math (), stacking layers would be useless (a stack of linear functions is still just a linear function). We need to bend the lines.

We apply an **Activation Function** () after every neuron.

**Common Functions:**

* **Sigmoid:** 
* *Shape:* S-curve. Squashes output between 0 and 1.
* *Use:* Probability outputs.


* **ReLU (Rectified Linear Unit):** 
* *Shape:* Flat for negatives, linear for positives.
* *Use:* The default for almost all modern Hidden Layers. It is fast and efficient.