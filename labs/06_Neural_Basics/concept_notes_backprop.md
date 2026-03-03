**Topic:** Lecture 09 & 10 - Gradient Descent & Backpropagation

#### **1. The Loss Function (The Mountain)**

Before we can learn, we need to measure how badly we messed up. We use a **Loss Function** (or Cost Function).

* For regression (predicting a number), we often use **Mean Squared Error (MSE)**.
* Formula: $L = \frac{1}{2}(\text{Target} - \text{Prediction})^2$
* *Goal:* Minimize $L$ to $0$.

#### **2. Gradient Descent (The Strategy)**

The algorithm used to minimize the Loss. It calculates the slope of the error and takes a step downhill.

* **The Update Rule:** 
$$W_{\text{new}} = W_{\text{old}} - \alpha \frac{\partial L}{\partial W}$$


* **$\alpha$ (Alpha):** The Learning Rate. Controls the size of the step.
* **$\frac{\partial L}{\partial W}$ (Gradient):** The derivative of the Loss with respect to the Weight. It tells us: "If I change this weight by 1%, how much does the error change?"

#### **3. Backpropagation (The Delivery System)**

Short for "Backward Propagation of Errors."
If you have multiple layers, you can't easily see how a weight in the first layer affected the final error. We use the **Chain Rule** from calculus to pass the blame backward.

1. Calculate the error at the Output Layer.
2. Figure out how much the Output Weights contributed to that error, and update them.
3. Pass the remaining error backward to the Hidden Layer.
4. Figure out how much the Hidden Weights contributed to *that* error, and update them.