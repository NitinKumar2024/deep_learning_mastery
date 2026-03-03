import numpy as np

# 1. Activation and its Derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(a):
    return a * (1.0 - a)

# 2. The Learning Brain
class LearningNeuron:
    def __init__(self):
        # Start completely blank (0.0)
        self.w = 0.0
        self.b = 0.0
        self.lr = 1.0 # Learning Rate
        
    def train(self, x, target_y, epochs=10):
        print(f"\n--- Training Started | Input: {x} | Target: {target_y} ---")
        
        for epoch in range(epochs):
            # --- 1. FORWARD PASS ---
            z = (x * self.w) + self.b
            a = sigmoid(z)
            loss = 0.5 * (a - target_y)**2
            
            # --- 2. BACKWARD PASS (The Chain Rule) ---
            dL_da = a - target_y
            da_dz = sigmoid_derivative(a)
            
            dz_dw = x
            dz_db = 1.0
            
            # The Magic Multiplications (Gradient)
            gradient_w = dL_da * da_dz * dz_dw
            gradient_b = dL_da * da_dz * dz_db
            
            # --- 3. GRADIENT DESCENT (The Update) ---
            self.w = self.w - (self.lr * gradient_w)
            self.b = self.b - (self.lr * gradient_b)
            
            print(f"Epoch {epoch+1:2d} | Pred: {a:.4f} | Loss: {loss:.4f} | w: {self.w:.4f} | b: {self.b:.4f}")

# --- EXECUTION ---
neuron = LearningNeuron()

# Scenario 1: The standard test
neuron.train(x=1.0, target_y=1.0, epochs=30)

# Scenario 2: The "Zero Input" edge case you figured out
neuron2 = LearningNeuron()
neuron2.train(x=0.0, target_y=1.0, epochs=30)