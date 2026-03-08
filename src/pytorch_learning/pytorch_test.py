import torch
import torch.nn as nn

# 1. Create a fake input (like 3 features for a patient)
patient_data = torch.tensor([[1.5, 2.0, 0.5]]) 

# 2. Create a Perceptron (3 inputs -> 1 output)
# This automatically creates a 3x1 Weight Matrix and a Bias
layer = nn.Linear(in_features=3, out_features=1)

# 3. Push the data through!
prediction = layer(patient_data)

print("Patient Data:", patient_data)
print("Untrained Prediction:", prediction)