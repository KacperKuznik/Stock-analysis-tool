"""Basic inference loop"""
def predict_next_value(model, last_n_values):
    """
    Predicts the next value given the last n values using the trained model.

    Parameters:
        model (nn.Module): The trained PyTorch model.
        last_n_values (list or numpy array): The last n observed values.

    Returns:
        float: The predicted next value.
    """
    model.eval()
    with torch.no_grad():
        input_tensor = torch.tensor(last_n_values, dtype=torch.float32).view(1, -1)  # Reshape to (1, input_size)
        output = model(input_tensor)
    return output.item()
