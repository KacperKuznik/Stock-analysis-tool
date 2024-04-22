"""Test the AI model"""
import matplotlib.pyplot as plt

# Generate test data
test_data = generate_dummy_data(200)  # Generate 200 data points for testing
test_data = torch.tensor(test_data, dtype=torch.float32).view(-1, 1)  # Reshape to (num_samples, input_size)

# Test the model
model.eval()
with torch.no_grad():
    test_output = model(test_data)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(test_data.numpy(), label='Actual Data', color='blue')
plt.plot(test_output.numpy(), label='Predicted Data', color='red')
plt.title('Stock Prediction')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
