"""Basic stock market prediction model training loop."""
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd

class StockPredictor(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(StockPredictor, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def generate_dummy_data(num_samples):
    time = np.arange(0, num_samples)
    trend = 0.5 * time + 10  
    noise = np.random.normal(0, 1, num_samples)  
    data = trend + noise
    return data

# Hyperparameters
input_size = 1
hidden_size = 128
output_size = 1
learning_rate = 0.01
num_epochs = 200

# Initialize model, loss function, and optimizer
model = StockPredictor(input_size, hidden_size, output_size)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

num_samples = 1000
data = generate_dummy_data(num_samples)
data = torch.tensor(data, dtype=torch.float32).view(-1, 1)  # Reshape to (num_samples, input_size)

train_ratio = 0.8
train_size = int(train_ratio * num_samples)
train_data = data[:train_size]
val_data = data[train_size:]

for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    train_output = model(train_data)
    train_loss = criterion(train_output, train_data)
    train_loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Train Epoch [{epoch + 1}/{num_epochs}], Loss: {train_loss.item():.4f}')

    model.eval()
    with torch.no_grad():
        val_output = model(val_data)
        val_loss = criterion(val_output, val_data)
        if (epoch + 1) % 10 == 0:
            print(f'Validation Loss: {val_loss.item():.4f}')
