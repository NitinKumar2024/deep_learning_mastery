import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        # 1. Initialize Weights and Bias
        # We use small random numbers (or zeros)
        self.weights = np.zeros(input_size)
        self.bias = 0.0
        self.lr = learning_rate
        
    def predict(self, inputs):
        # inputs is a numpy array e.g., [0, 1]
        
        # --- LOGIC MISSING 1: THE FORWARD PASS ---
        # 1. Calculate the weighted sum (Dot Product)
        #    z = (x1 * w1) + (x2 * w2) ... + bias
        #    Hint: use np.dot(inputs, self.weights) + self.bias
        
        # 2. Apply Step Function (Activation)
        #    if z > 0 return 1, else return 0
        
        linear_output = np.dot(inputs, self.weights) + self.bias
        activation = 1 if linear_output > 0 else 0
        
        return activation
    
    def train(self, training_inputs, labels, epochs=10):
        print(f"Starting Training for {epochs} epochs...")
        
        for epoch in range(epochs):
            print(f"\nEpoch {epoch+1}")
            
            for inputs, target in zip(training_inputs, labels):
                # 1. Make a prediction
                prediction = self.predict(inputs)
                
                # 2. Calculate Error
                # error = target - prediction
                error = target - prediction
                
                # --- LOGIC MISSING 2: THE UPDATE RULE ---
                # We only update if there is an error!
                # Weight_new = Weight_old + (learning_rate * error * input)
                # Bias_new   = Bias_old   + (learning_rate * error)
                
                # Update self.weights and self.bias here
                self.weights = self.weights + (self.lr * error * inputs)
                self.bias = self.bias + (self.lr * error)

                print(f"  Input: {inputs} | Target: {target} | Pred: {prediction} | Error: {error}")

# --- TEST DATA (AND Gate) ---
training_inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

labels = np.array([0, 0, 0, 1]) # AND logic

# 1. Create Neuron
neuron = Perceptron(input_size=2)

# 2. Train
neuron.train(training_inputs, labels)

# 3. Verify
print("\n--- Final Verification ---")
print(f"Weights: {neuron.weights}")
print(f"Bias: {neuron.bias}")

for inputs in training_inputs:
    print(f"Input: {inputs} -> Prediction: {neuron.predict(inputs)}")