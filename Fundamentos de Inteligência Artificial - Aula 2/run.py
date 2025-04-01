import torch
import torch.nn as nn
import torch.optim as optim

# Define the learning data as a tensor
learning_data = torch.tensor(
    [[5.0], [10.0], [10.0], [5.0], [10.0],
     [5.0], [10.0], [10.0], [5.0], [10.0],
     [5.0], [10.0], [10.0], [5.0], [10.0],
     [5.0], [10.0], [10.0], [5.0], [10.0]],
    dtype=torch.float32
)

expected_output = torch.tensor(
    [[30.5], [63.0], [67.0], [29.0], [62.0],
     [30.5], [63.0], [67.0], [29.0], [62.0],
     [30.5], [63.0], [67.0], [29.0], [62.0],
     [30.5], [63.0], [67.0], [29.0], [62.0]],
    dtype=torch.float32
)

# Define the neural network model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(1, 10)  # Input layer to hidden layer
        self.fc2 = nn.Linear(10, 1)   # Hidden layer to output layer

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))  # Activation function for hidden layer
        x = self.fc2(x)                  # Output layer
        return x

# Initialize the model, loss function, and optimizer
model = SimpleNN()
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent

for epoch in range(1000):  # Training loop
    optimizer.zero_grad()  # Zero the gradients
    outputs = model(learning_data)  # Forward pass
    loss = criterion(outputs, expected_output)  # Compute loss
    loss.backward()  # Backward pass
    optimizer.step()  # Update weights

    if (epoch + 1) % 100 == 0:  # Print loss every 100 epochs
        print(f'Epoch [{epoch + 1}/1000], Loss: {loss.item():.4f}')

with torch.no_grad():  # No gradient calculation for inference
    test_data = torch.tensor([[5.0], [10.0]], dtype=torch.float32)  # Test data
    predicted_output = model(test_data)  # Get predictions
    print(f'Predicted output: {predicted_output.numpy()}')  # Print predictions