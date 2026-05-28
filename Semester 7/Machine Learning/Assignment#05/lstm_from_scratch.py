"""
LSTM Implementation from Scratch
Complex Computing Problem - Namal University Mianwali
Department of Computer Science

This module implements a complete Long Short-Term Memory (LSTM) network
from scratch using only NumPy, following the exact mathematical equations.
NO pre-built LSTM libraries are used.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Set random seed for reproducibility
np.random.seed(42)


class LSTMCell:
    """
    Single-layer LSTM cell implemented from scratch using mathematical equations.
    NO pre-built LSTM functions allowed.
    
    The LSTM cell implements the following equations:
    - Forget Gate: f_t = σ(W_f[h_(t-1), x_t] + b_f)
    - Input Gate: i_t = σ(W_i[h_(t-1), x_t] + b_i)
    - Candidate Cell State: c̃_t = tanh(W_c[h_(t-1), x_t] + b_c)
    - Cell State Update: c_t = f_t ⊙ c_(t-1) + i_t ⊙ c̃_t
    - Output Gate: o_t = σ(W_o[h_(t-1), x_t] + b_o)
    - Hidden State: h_t = o_t ⊙ tanh(c_t)
    
    Where:
    - σ = sigmoid activation function
    - ⊙ = element-wise multiplication (Hadamard product)
    - [h_(t-1), x_t] = concatenation of previous hidden state and current input
    """
    
    def __init__(self, input_size, hidden_size, learning_rate=0.01):
        """
        Initialize LSTM cell with weights and biases.
        
        Args:
            input_size: Dimension of input vector x_t
            hidden_size: Dimension of hidden state h_t and cell state c_t
            learning_rate: Learning rate for gradient descent
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.learning_rate = learning_rate
        
        # Combined input size (hidden + input)
        combined_size = hidden_size + input_size
        
        # Initialize weights using Xavier initialization for sigmoid gates
        # and He initialization for tanh gates
        xavier_scale = np.sqrt(2.0 / (combined_size + hidden_size))
        he_scale = np.sqrt(2.0 / combined_size)
        
        # Forget gate weights: W_f shape (hidden_size, combined_size)
        self.W_f = np.random.randn(hidden_size, combined_size) * xavier_scale
        self.b_f = np.zeros((hidden_size, 1))
        
        # Input gate weights: W_i shape (hidden_size, combined_size)
        self.W_i = np.random.randn(hidden_size, combined_size) * xavier_scale
        self.b_i = np.zeros((hidden_size, 1))
        
        # Candidate cell state weights: W_c shape (hidden_size, combined_size)
        self.W_c = np.random.randn(hidden_size, combined_size) * he_scale
        self.b_c = np.zeros((hidden_size, 1))
        
        # Output gate weights: W_o shape (hidden_size, combined_size)
        self.W_o = np.random.randn(hidden_size, combined_size) * xavier_scale
        self.b_o = np.zeros((hidden_size, 1))
        
        # Store gradients for backpropagation
        self.dW_f = np.zeros_like(self.W_f)
        self.db_f = np.zeros_like(self.b_f)
        self.dW_i = np.zeros_like(self.W_i)
        self.db_i = np.zeros_like(self.b_i)
        self.dW_c = np.zeros_like(self.W_c)
        self.db_c = np.zeros_like(self.b_c)
        self.dW_o = np.zeros_like(self.W_o)
        self.db_o = np.zeros_like(self.b_o)
    
    def sigmoid(self, x):
        """
        Implement sigmoid activation function: σ(x) = 1 / (1 + exp(-x))
        
        Args:
            x: Input array
            
        Returns:
            Sigmoid activation of x, clipped to prevent overflow
        """
        # Clip x to prevent overflow
        x_clipped = np.clip(x, -500, 500)
        return 1.0 / (1.0 + np.exp(-x_clipped))
    
    def tanh(self, x):
        """
        Implement tanh activation function: tanh(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
        
        Args:
            x: Input array
            
        Returns:
            Tanh activation of x
        """
        return np.tanh(x)
    
    def forward(self, x_t, h_prev, c_prev):
        """
        Forward pass through LSTM cell for one timestep.
        Must explicitly show all gate computations.
        
        Args:
            x_t: Current input vector, shape (input_size, 1) or (input_size,)
            h_prev: Previous hidden state, shape (hidden_size, 1) or (hidden_size,)
            c_prev: Previous cell state, shape (hidden_size, 1) or (hidden_size,)
        
        Returns:
            h_t: Current hidden state, shape (hidden_size, 1)
            c_t: Current cell state, shape (hidden_size, 1)
            gates: Dictionary containing intermediate gate values for visualization
                - f_t: Forget gate activation
                - i_t: Input gate activation
                - c_tilde: Candidate cell state
                - o_t: Output gate activation
        """
        # Ensure inputs are column vectors
        if x_t.ndim == 1:
            x_t = x_t.reshape(-1, 1)
        if h_prev.ndim == 1:
            h_prev = h_prev.reshape(-1, 1)
        if c_prev.ndim == 1:
            c_prev = c_prev.reshape(-1, 1)
        
        # Step 1: Concatenate previous hidden state and current input
        # [h_(t-1), x_t] shape: (hidden_size + input_size, 1)
        concat = np.vstack([h_prev, x_t])
        
        # Step 2: Compute forget gate
        # f_t = σ(W_f[h_(t-1), x_t] + b_f)
        f_t = self.sigmoid(self.W_f @ concat + self.b_f)
        
        # Step 3: Compute input gate
        # i_t = σ(W_i[h_(t-1), x_t] + b_i)
        i_t = self.sigmoid(self.W_i @ concat + self.b_i)
        
        # Step 4: Compute candidate cell state
        # c̃_t = tanh(W_c[h_(t-1), x_t] + b_c)
        c_tilde = self.tanh(self.W_c @ concat + self.b_c)
        
        # Step 5: Update cell state
        # c_t = f_t ⊙ c_(t-1) + i_t ⊙ c̃_t
        # ⊙ denotes element-wise multiplication (Hadamard product)
        c_t = f_t * c_prev + i_t * c_tilde
        
        # Step 6: Compute output gate
        # o_t = σ(W_o[h_(t-1), x_t] + b_o)
        o_t = self.sigmoid(self.W_o @ concat + self.b_o)
        
        # Step 7: Compute hidden state
        # h_t = o_t ⊙ tanh(c_t)
        h_t = o_t * self.tanh(c_t)
        
        # Store intermediate values for backpropagation and visualization
        gates = {
            'f_t': f_t,
            'i_t': i_t,
            'c_tilde': c_tilde,
            'o_t': o_t,
            'concat': concat
        }
        
        return h_t, c_t, gates
    
    def forward_sequence(self, X):
        """
        Process entire sequence and return all hidden states and cell states.
        
        Args:
            X: Input sequence, shape (sequence_length, input_size) or (sequence_length, input_size, 1)
        
        Returns:
            h_states: All hidden states, shape (sequence_length, hidden_size)
            c_states: All cell states, shape (sequence_length, hidden_size)
            all_gates: List of gate dictionaries for each timestep
        """
        sequence_length = X.shape[0]
        h_states = np.zeros((sequence_length, self.hidden_size))
        c_states = np.zeros((sequence_length, self.hidden_size))
        all_gates = []
        
        # Initialize hidden and cell states to zeros
        h_prev = np.zeros((self.hidden_size, 1))
        c_prev = np.zeros((self.hidden_size, 1))
        
        # Process each timestep
        for t in range(sequence_length):
            x_t = X[t]
            h_t, c_t, gates = self.forward(x_t, h_prev, c_prev)
            
            # Store states (flatten to 1D for storage)
            h_states[t] = h_t.flatten()
            c_states[t] = c_t.flatten()
            all_gates.append(gates)
            
            # Update previous states for next iteration
            h_prev = h_t
            c_prev = c_t
        
        return h_states, c_states, all_gates


class LSTMNetwork:
    """
    Complete LSTM network for sequence processing.
    Consists of an LSTM cell and an output layer for predictions.
    """
    
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        """
        Initialize LSTM network.
        
        Args:
            input_size: Dimension of input vector
            hidden_size: Dimension of hidden state
            output_size: Dimension of output (for regression: 1, for classification: num_classes)
            learning_rate: Learning rate for gradient descent
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        
        # Initialize LSTM cell
        self.lstm_cell = LSTMCell(input_size, hidden_size, learning_rate)
        
        # Initialize output layer weights
        # Output layer: y = W_out * h_t + b_out
        xavier_scale = np.sqrt(2.0 / (hidden_size + output_size))
        self.W_out = np.random.randn(output_size, hidden_size) * xavier_scale
        self.b_out = np.zeros((output_size, 1))
        
        # Store gradients
        self.dW_out = np.zeros_like(self.W_out)
        self.db_out = np.zeros_like(self.b_out)
        
        # Store training history
        self.loss_history = []
    
    def forward(self, X):
        """
        Forward pass through the network.
        
        Args:
            X: Input sequence, shape (sequence_length, input_size)
        
        Returns:
            predictions: Output predictions, shape (sequence_length, output_size)
            h_states: All hidden states
            c_states: All cell states
            all_gates: All gate activations
        """
        # Forward pass through LSTM cell
        h_states, c_states, all_gates = self.lstm_cell.forward_sequence(X)
        
        # Forward pass through output layer
        # Reshape h_states for matrix multiplication
        h_states_reshaped = h_states.reshape(-1, self.hidden_size, 1)
        predictions = np.zeros((h_states.shape[0], self.output_size))
        
        for t in range(h_states.shape[0]):
            predictions[t] = (self.W_out @ h_states_reshaped[t] + self.b_out).flatten()
        
        return predictions, h_states, c_states, all_gates
    
    def compute_loss(self, predictions, targets):
        """
        Compute Mean Squared Error loss.
        
        Args:
            predictions: Predicted values, shape (sequence_length, output_size)
            targets: Target values, shape (sequence_length, output_size)
        
        Returns:
            loss: Mean squared error
        """
        return np.mean((predictions - targets) ** 2)
    
    def backward(self, X, y, predictions, h_states, c_states, all_gates):
        """
        Backpropagation Through Time (BPTT).
        
        Args:
            X: Input sequence, shape (sequence_length, input_size)
            y: Target sequence, shape (sequence_length, output_size)
            predictions: Predicted sequence from forward pass
            h_states: All hidden states from forward pass
            c_states: All cell states from forward pass
            all_gates: All gate activations from forward pass
        """
        sequence_length = X.shape[0]
        
        # Initialize gradients
        dh_next = np.zeros((self.hidden_size, 1))
        dc_next = np.zeros((self.hidden_size, 1))
        
        # Reset gradients
        self.lstm_cell.dW_f.fill(0)
        self.lstm_cell.db_f.fill(0)
        self.lstm_cell.dW_i.fill(0)
        self.lstm_cell.db_i.fill(0)
        self.lstm_cell.dW_c.fill(0)
        self.lstm_cell.db_c.fill(0)
        self.lstm_cell.dW_o.fill(0)
        self.lstm_cell.db_o.fill(0)
        self.dW_out.fill(0)
        self.db_out.fill(0)
        
        # Backward pass through time
        for t in reversed(range(sequence_length)):
            # Output layer gradients
            dy = 2 * (predictions[t] - y[t]) / sequence_length
            dy = dy.reshape(-1, 1)
            
            self.dW_out += dy @ h_states[t].reshape(1, -1)
            self.db_out += dy
            
            # Gradient from output layer to hidden state
            dh = self.W_out.T @ dy + dh_next
            
            # Get gate values
            gates = all_gates[t]
            f_t = gates['f_t']
            i_t = gates['i_t']
            c_tilde = gates['c_tilde']
            o_t = gates['o_t']
            concat = gates['concat']
            
            # Current cell state
            c_t = c_states[t].reshape(-1, 1)
            c_prev = c_states[t-1].reshape(-1, 1) if t > 0 else np.zeros((self.hidden_size, 1))
            
            # Gradient through output gate
            tanh_c_t = self.lstm_cell.tanh(c_t)
            do_t = dh * tanh_c_t
            do_t = do_t * o_t * (1 - o_t)  # sigmoid derivative
            
            # Gradient through cell state
            dc = dh * o_t * (1 - tanh_c_t ** 2) + dc_next
            
            # Gradient through forget gate
            df_t = dc * c_prev
            df_t = df_t * f_t * (1 - f_t)  # sigmoid derivative
            
            # Gradient through input gate
            di_t = dc * c_tilde
            di_t = di_t * i_t * (1 - i_t)  # sigmoid derivative
            
            # Gradient through candidate cell state
            dc_tilde = dc * i_t
            dc_tilde = dc_tilde * (1 - c_tilde ** 2)  # tanh derivative
            
            # Accumulate gradients
            self.lstm_cell.dW_f += df_t @ concat.T
            self.lstm_cell.db_f += df_t
            self.lstm_cell.dW_i += di_t @ concat.T
            self.lstm_cell.db_i += di_t
            self.lstm_cell.dW_c += dc_tilde @ concat.T
            self.lstm_cell.db_c += dc_tilde
            self.lstm_cell.dW_o += do_t @ concat.T
            self.lstm_cell.db_o += do_t
            
            # Gradient for previous timestep
            dconcat = (self.lstm_cell.W_f.T @ df_t +
                      self.lstm_cell.W_i.T @ di_t +
                      self.lstm_cell.W_c.T @ dc_tilde +
                      self.lstm_cell.W_o.T @ do_t)
            
            dh_next = dconcat[:self.hidden_size]
            dc_next = dc * f_t
        
        # Clip gradients to prevent exploding gradients
        max_grad_norm = 5.0
        for grad in [self.lstm_cell.dW_f, self.lstm_cell.dW_i, self.lstm_cell.dW_c, 
                     self.lstm_cell.dW_o, self.dW_out]:
            grad_norm = np.linalg.norm(grad)
            if grad_norm > max_grad_norm:
                grad *= max_grad_norm / grad_norm
    
    def update_weights(self):
        """Update weights using computed gradients."""
        # Update LSTM cell weights
        self.lstm_cell.W_f -= self.learning_rate * self.lstm_cell.dW_f
        self.lstm_cell.b_f -= self.learning_rate * self.lstm_cell.db_f
        self.lstm_cell.W_i -= self.learning_rate * self.lstm_cell.dW_i
        self.lstm_cell.b_i -= self.learning_rate * self.lstm_cell.db_i
        self.lstm_cell.W_c -= self.learning_rate * self.lstm_cell.dW_c
        self.lstm_cell.b_c -= self.learning_rate * self.lstm_cell.db_c
        self.lstm_cell.W_o -= self.learning_rate * self.lstm_cell.dW_o
        self.lstm_cell.b_o -= self.learning_rate * self.lstm_cell.db_o
        
        # Update output layer weights
        self.W_out -= self.learning_rate * self.dW_out
        self.b_out -= self.learning_rate * self.db_out
    
    def train(self, X_train, y_train, epochs=100, verbose=True):
        """
        Training loop with backpropagation through time (BPTT).
        Track loss for visualization.
        
        Args:
            X_train: Training input sequences, shape (num_samples, sequence_length, input_size)
            y_train: Training targets, shape (num_samples, sequence_length, output_size)
            epochs: Number of training epochs
            verbose: Whether to print training progress
        
        Returns:
            loss_history: List of loss values per epoch
        """
        self.loss_history = []
        
        for epoch in range(epochs):
            epoch_loss = 0
            
            # Process each training sample
            for i in range(len(X_train)):
                X = X_train[i]
                y = y_train[i]
                
                # Forward pass
                predictions, h_states, c_states, all_gates = self.forward(X)
                
                # Compute loss
                loss = self.compute_loss(predictions, y)
                epoch_loss += loss
                
                # Backward pass
                self.backward(X, y, predictions, h_states, c_states, all_gates)
                
                # Update weights
                self.update_weights()
            
            avg_loss = epoch_loss / len(X_train)
            self.loss_history.append(avg_loss)
            
            if verbose and (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {avg_loss:.6f}")
        
        return self.loss_history
    
    def predict(self, X):
        """
        Make predictions on new sequences.
        
        Args:
            X: Input sequence(s), shape (sequence_length, input_size) or (num_samples, sequence_length, input_size)
        
        Returns:
            predictions: Predicted values
        """
        if X.ndim == 2:
            # Single sequence
            predictions, _, _, _ = self.forward(X)
            return predictions
        else:
            # Multiple sequences
            all_predictions = []
            for i in range(X.shape[0]):
                pred, _, _, _ = self.forward(X[i])
                all_predictions.append(pred)
            return np.array(all_predictions)


def demonstrate_long_term_dependencies():
    """
    Create experiment showing how LSTM preserves long-term dependencies
    compared to issues in vanilla RNNs.
    
    Task: Remember a value from the beginning of a sequence and output it at the end.
    """
    print("\n=== Long-Term Dependency Demonstration ===")
    
    # Create a task where we need to remember information from early in the sequence
    # Sequence: [random values..., important_value, zeros..., important_value]
    sequence_length = 50
    delay = 40  # Gap between storing and retrieving the value
    
    # Generate training data
    num_samples = 100
    X_train = []
    y_train = []
    
    for _ in range(num_samples):
        # Create sequence with important value at position 5
        sequence = np.random.randn(sequence_length, 1) * 0.1
        important_value = np.random.randn(1) * 2.0
        sequence[5] = important_value
        
        # Target: output the important value at the end
        target = np.zeros((sequence_length, 1))
        target[-1] = important_value
        
        X_train.append(sequence)
        y_train.append(target)
    
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    
    # Create and train LSTM
    lstm = LSTMNetwork(input_size=1, hidden_size=32, output_size=1, learning_rate=0.01)
    print("Training LSTM on long-term dependency task...")
    loss_history = lstm.train(X_train, y_train, epochs=200, verbose=True)
    
    # Test on new sequence
    test_sequence = np.random.randn(sequence_length, 1) * 0.1
    test_value = 1.5
    test_sequence[5] = test_value
    test_target = np.zeros((sequence_length, 1))
    test_target[-1] = test_value
    
    predictions = lstm.predict(test_sequence)
    
    print(f"\nTest: Important value at position 5: {test_value:.3f}")
    print(f"Predicted value at end: {predictions[-1, 0]:.3f}")
    print(f"Target value: {test_target[-1, 0]:.3f}")
    print(f"Error: {abs(predictions[-1, 0] - test_target[-1, 0]):.6f}")
    
    # Visualize
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(loss_history)
    plt.title('Training Loss - Long-Term Dependency Task')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(test_sequence, label='Input Sequence', alpha=0.7)
    plt.axvline(x=5, color='r', linestyle='--', label='Important Value Position')
    plt.plot(range(sequence_length), predictions, label='Predictions', linewidth=2)
    plt.axhline(y=test_value, color='g', linestyle='--', label='Target Value')
    plt.title('Long-Term Dependency: Remembering Early Information')
    plt.xlabel('Time Step')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('plots/long_term_dependency.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved to plots/long_term_dependency.png")
    plt.close()
    
    return lstm, loss_history


def visualize_gate_behavior(lstm_cell, sequence):
    """
    Visualize the behavior of each gate over a sequence:
    - Forget gate values
    - Input gate values
    - Output gate values
    - Cell state evolution
    
    Args:
        lstm_cell: Trained LSTMCell instance
        sequence: Input sequence, shape (sequence_length, input_size)
    """
    print("\n=== Gate Behavior Visualization ===")
    
    # Forward pass to get gate activations
    h_states, c_states, all_gates = lstm_cell.forward_sequence(sequence)
    
    sequence_length = sequence.shape[0]
    timesteps = np.arange(sequence_length)
    
    # Extract gate values
    forget_gates = np.array([gates['f_t'].flatten() for gates in all_gates])
    input_gates = np.array([gates['i_t'].flatten() for gates in all_gates])
    output_gates = np.array([gates['o_t'].flatten() for gates in all_gates])
    
    # Plot gate behavior
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Input sequence
    axes[0, 0].plot(timesteps, sequence.flatten(), 'b-', linewidth=2)
    axes[0, 0].set_title('Input Sequence')
    axes[0, 0].set_xlabel('Time Step')
    axes[0, 0].set_ylabel('Input Value')
    axes[0, 0].grid(True)
    
    # Forget gate (show first few dimensions)
    num_dims_to_show = min(5, forget_gates.shape[1])
    for i in range(num_dims_to_show):
        axes[0, 1].plot(timesteps, forget_gates[:, i], label=f'Dim {i}', alpha=0.7)
    axes[0, 1].set_title('Forget Gate Activations')
    axes[0, 1].set_xlabel('Time Step')
    axes[0, 1].set_ylabel('Forget Gate Value')
    axes[0, 1].legend()
    axes[0, 1].grid(True)
    axes[0, 1].axhline(y=0.5, color='r', linestyle='--', alpha=0.5, label='Threshold')
    
    # Input gate
    for i in range(num_dims_to_show):
        axes[1, 0].plot(timesteps, input_gates[:, i], label=f'Dim {i}', alpha=0.7)
    axes[1, 0].set_title('Input Gate Activations')
    axes[1, 0].set_xlabel('Time Step')
    axes[1, 0].set_ylabel('Input Gate Value')
    axes[1, 0].legend()
    axes[1, 0].grid(True)
    axes[1, 0].axhline(y=0.5, color='r', linestyle='--', alpha=0.5, label='Threshold')
    
    # Output gate
    for i in range(num_dims_to_show):
        axes[1, 1].plot(timesteps, output_gates[:, i], label=f'Dim {i}', alpha=0.7)
    axes[1, 1].set_title('Output Gate Activations')
    axes[1, 1].set_xlabel('Time Step')
    axes[1, 1].set_ylabel('Output Gate Value')
    axes[1, 1].legend()
    axes[1, 1].grid(True)
    axes[1, 1].axhline(y=0.5, color='r', linestyle='--', alpha=0.5, label='Threshold')
    
    plt.tight_layout()
    plt.savefig('plots/gate_behavior.png', dpi=300, bbox_inches='tight')
    print("Plot saved to plots/gate_behavior.png")
    plt.close()
    
    # Cell state evolution
    plt.figure(figsize=(12, 6))
    num_dims_to_show = min(5, c_states.shape[1])
    for i in range(num_dims_to_show):
        plt.plot(timesteps, c_states[:, i], label=f'Cell State Dim {i}', linewidth=2, alpha=0.8)
    plt.title('Cell State Evolution Over Time')
    plt.xlabel('Time Step')
    plt.ylabel('Cell State Value')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/cell_state_evolution.png', dpi=300, bbox_inches='tight')
    print("Plot saved to plots/cell_state_evolution.png")
    plt.close()


def parameter_sensitivity_analysis():
    """
    Demonstrate effects of different learning parameters on gate outputs:
    - Different weight initializations
    - Different learning rates
    - Different hidden sizes
    """
    print("\n=== Parameter Sensitivity Analysis ===")
    
    # Generate simple sine wave data
    sequence_length = 30
    t = np.linspace(0, 4 * np.pi, sequence_length)
    X_simple = np.sin(t).reshape(-1, 1)
    y_simple = np.sin(t + 0.1).reshape(-1, 1)  # Shifted sine wave
    
    X_train = np.array([X_simple])
    y_train = np.array([y_simple])
    
    # 1. Learning Rate Analysis
    print("\n1. Learning Rate Analysis...")
    learning_rates = [0.001, 0.01, 0.1]
    lr_losses = {}
    
    for lr in learning_rates:
        lstm = LSTMNetwork(input_size=1, hidden_size=16, output_size=1, learning_rate=lr)
        loss_history = lstm.train(X_train, y_train, epochs=100, verbose=False)
        lr_losses[lr] = loss_history
        print(f"  Learning Rate {lr}: Final Loss = {loss_history[-1]:.6f}")
    
    # Plot learning rate comparison
    plt.figure(figsize=(10, 6))
    for lr, losses in lr_losses.items():
        plt.plot(losses, label=f'LR = {lr}', linewidth=2)
    plt.title('Effect of Learning Rate on Training')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/learning_rate_comparison.png', dpi=300, bbox_inches='tight')
    print("Plot saved to plots/learning_rate_comparison.png")
    plt.close()
    
    # 2. Hidden Size Analysis
    print("\n2. Hidden Size Analysis...")
    hidden_sizes = [8, 16, 32, 64]
    hidden_losses = {}
    
    for hidden_size in hidden_sizes:
        lstm = LSTMNetwork(input_size=1, hidden_size=hidden_size, output_size=1, learning_rate=0.01)
        loss_history = lstm.train(X_train, y_train, epochs=100, verbose=False)
        hidden_losses[hidden_size] = loss_history
        print(f"  Hidden Size {hidden_size}: Final Loss = {loss_history[-1]:.6f}")
    
    # Plot hidden size comparison
    plt.figure(figsize=(10, 6))
    for hidden_size, losses in hidden_losses.items():
        plt.plot(losses, label=f'Hidden Size = {hidden_size}', linewidth=2)
    plt.title('Effect of Hidden Size on Training')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/hidden_size_comparison.png', dpi=300, bbox_inches='tight')
    print("Plot saved to plots/hidden_size_comparison.png")
    plt.close()
    
    # 3. Weight Initialization Analysis
    print("\n3. Weight Initialization Analysis...")
    # This would require modifying the initialization in LSTMCell
    # For demonstration, we'll show that different random seeds produce different results
    init_losses = {}
    seeds = [42, 123, 456]
    
    for seed in seeds:
        np.random.seed(seed)
        lstm = LSTMNetwork(input_size=1, hidden_size=16, output_size=1, learning_rate=0.01)
        loss_history = lstm.train(X_train, y_train, epochs=100, verbose=False)
        init_losses[f'Seed {seed}'] = loss_history
        print(f"  Initialization Seed {seed}: Final Loss = {loss_history[-1]:.6f}")
    
    # Plot initialization comparison
    plt.figure(figsize=(10, 6))
    for init_name, losses in init_losses.items():
        plt.plot(losses, label=init_name, linewidth=2)
    plt.title('Effect of Weight Initialization on Training')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/initialization_comparison.png', dpi=300, bbox_inches='tight')
    print("Plot saved to plots/initialization_comparison.png")
    plt.close()
    
    # Reset seed
    np.random.seed(42)


# Main execution
if __name__ == "__main__":
    # Ensure plots directory exists
    os.makedirs('plots', exist_ok=True)
    
    print("=" * 60)
    print("LSTM Implementation from Scratch")
    print("Complex Computing Problem - Namal University")
    print("=" * 60)
    
    # Example 1: Simple sequence prediction (sine wave)
    print("\n" + "=" * 60)
    print("Example 1: Sine Wave Prediction")
    print("=" * 60)
    
    # Generate sine wave data
    sequence_length = 50
    t = np.linspace(0, 4 * np.pi, sequence_length)
    X_sine = np.sin(t).reshape(-1, 1)
    y_sine = np.sin(t + 0.1).reshape(-1, 1)  # Predict next value
    
    X_train_sine = np.array([X_sine])
    y_train_sine = np.array([y_sine])
    
    # Create and train LSTM
    lstm_sine = LSTMNetwork(input_size=1, hidden_size=32, output_size=1, learning_rate=0.01)
    print("Training LSTM on sine wave prediction...")
    loss_history_sine = lstm_sine.train(X_train_sine, y_train_sine, epochs=200, verbose=True)
    
    # Make predictions
    predictions_sine = lstm_sine.predict(X_sine)
    
    # Visualize results
    plt.figure(figsize=(14, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(t, X_sine, 'b-', label='Input', linewidth=2)
    plt.plot(t, y_sine, 'g--', label='Target', linewidth=2)
    plt.plot(t, predictions_sine, 'r-', label='Prediction', linewidth=2, alpha=0.7)
    plt.title('Sine Wave Prediction')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(loss_history_sine)
    plt.title('Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('plots/training_loss.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved to plots/training_loss.png")
    plt.close()
    
    # Example 2: Long-term dependency task
    print("\n" + "=" * 60)
    print("Example 2: Long-Term Dependency Task")
    print("=" * 60)
    lstm_longterm, loss_longterm = demonstrate_long_term_dependencies()
    
    # Example 3: Gate behavior visualization
    print("\n" + "=" * 60)
    print("Example 3: Gate Behavior Visualization")
    print("=" * 60)
    # Use the sine wave sequence for visualization
    visualize_gate_behavior(lstm_sine.lstm_cell, X_sine)
    
    # Example 4: Parameter sensitivity analysis
    print("\n" + "=" * 60)
    print("Example 4: Parameter Sensitivity Analysis")
    print("=" * 60)
    parameter_sensitivity_analysis()
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  - plots/training_loss.png")
    print("  - plots/long_term_dependency.png")
    print("  - plots/gate_behavior.png")
    print("  - plots/cell_state_evolution.png")
    print("  - plots/learning_rate_comparison.png")
    print("  - plots/hidden_size_comparison.png")
    print("  - plots/initialization_comparison.png")
