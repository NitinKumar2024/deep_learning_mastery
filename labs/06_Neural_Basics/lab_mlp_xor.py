import numpy as np

# 1. The Activation Function
def sigmoid(x):
    output = 1 / (1 + np.exp(-x))
    return output

class XORNetwork:
    def __init__(self):
        self.W1 = np.array([[20, 20], [-20, -20]])
        self.b1 = np.array([[-10, 30]])

        self.W2 = np.array([[20], [20]])
        self.b2 = np.array([[-30]])

    # The Forward Pass
    def forward(self, X):
        # 1. Hidden Layer
        z1 = np.dot(X, self.W1.T) + self.b1
        a1 = sigmoid(z1) 
        
        # 2. Output Layer Calculation
        z2 = np.dot(a1, self.W2) + self.b2
        output = sigmoid(z2)
        
        return output


model = XORNetwork()

for i in model.W1:
    print(model.forward([1, 1]))