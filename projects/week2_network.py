import torch.nn as nn
import torch
import torch.optim as optim

class SimpleMLP(nn.Module):
    def __init__(self):
        super().__init__()

        self.hidden_layer = nn.Linear(in_features=3, out_features=5)
        self.relu = nn.ReLU()
        self.output_layer = nn.Linear(in_features=5, out_features=1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        hidden_nn = self.hidden_layer(x)
        relu_activation = self.relu(hidden_nn)
        output_nn = self.output_layer(relu_activation)
        prediction = self.sigmoid(output_nn)

        return prediction
    
model = SimpleMLP()
patient_data = torch.tensor([[7.5, 120.0, 30.0]])
output = model(patient_data)
print(output)

true_target = torch.tensor([[1.0]])
loss_fn = nn.BCELoss()

loss = loss_fn(output, true_target)
optimizer = optim.SGD(model.parameters(), lr=0.01)

optimizer.zero_grad()
loss.backward()
optimizer.step()

output2 = model(patient_data)
print(output2)