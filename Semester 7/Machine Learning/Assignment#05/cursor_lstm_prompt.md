# Cursor Prompt: LSTM Implementation from Scratch

## Assignment Context
This is a Complex Computing Problem (CCP) for Namal University's Computer Science Department. The assignment requires implementing a Long Short-Term Memory (LSTM) network from scratch using only mathematical equations - NO pre-built LSTM libraries allowed.

## Implementation Requirements

### Code File: `lstm_from_scratch.py`

Create a complete Python implementation with the following specifications:

#### 1. LSTM Cell Implementation
Implement a single-layer LSTM cell from scratch using these exact mathematical equations:

**Forget Gate:**
```
f_t = σ(W_f[h_(t-1), x_t] + b_f)
```

**Input Gate:**
```
i_t = σ(W_i[h_(t-1), x_t] + b_i)
```

**Candidate Cell State:**
```
c̃_t = tanh(W_c[h_(t-1), x_t] + b_c)
```

**Cell State Update:**
```
c_t = f_t ⊙ c_(t-1) + i_t ⊙ c̃_t
```

**Output Gate and Hidden State:**
```
o_t = σ(W_o[h_(t-1), x_t] + b_o)
h_t = o_t ⊙ tanh(c_t)
```

Where:
- σ = sigmoid activation function
- ⊙ = element-wise multiplication (Hadamard product)
- [h_(t-1), x_t] = concatenation of previous hidden state and current input

#### 2. Code Structure
```python
import numpy as np
import matplotlib.pyplot as plt

class LSTMCell:
    """
    Single-layer LSTM cell implemented from scratch using mathematical equations.
    NO pre-built LSTM functions allowed.
    """
    
    def __init__(self, input_size, hidden_size, learning_rate=0.01):
        # Initialize weights and biases for all gates
        # Use appropriate initialization (e.g., Xavier/He)
        pass
    
    def sigmoid(self, x):
        # Implement sigmoid activation
        pass
    
    def tanh(self, x):
        # Implement tanh activation
        pass
    
    def forward(self, x_t, h_prev, c_prev):
        """
        Forward pass through LSTM cell for one timestep.
        Must explicitly show all gate computations.
        
        Returns: h_t, c_t, and intermediate gate values for visualization
        """
        # 1. Concatenate h_prev and x_t
        # 2. Compute forget gate
        # 3. Compute input gate
        # 4. Compute candidate cell state
        # 5. Update cell state
        # 6. Compute output gate
        # 7. Compute hidden state
        pass
    
    def forward_sequence(self, X):
        """
        Process entire sequence and return all hidden states and cell states.
        """
        pass

class LSTMNetwork:
    """
    Complete LSTM network for sequence processing.
    """
    
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.lstm_cell = LSTMCell(input_size, hidden_size, learning_rate)
        # Add output layer
        pass
    
    def train(self, X_train, y_train, epochs=100):
        """
        Training loop with backpropagation through time (BPTT).
        Track loss for visualization.
        """
        pass
    
    def predict(self, X):
        """
        Make predictions on new sequences.
        """
        pass

# Demonstration Functions
def demonstrate_long_term_dependencies():
    """
    Create experiment showing how LSTM preserves long-term dependencies
    compared to issues in vanilla RNNs.
    """
    pass

def visualize_gate_behavior(lstm_cell, sequence):
    """
    Visualize the behavior of each gate over a sequence:
    - Forget gate values
    - Input gate values
    - Output gate values
    - Cell state evolution
    """
    pass

def parameter_sensitivity_analysis():
    """
    Demonstrate effects of different learning parameters on gate outputs:
    - Different weight initializations
    - Different learning rates
    - Different hidden sizes
    """
    pass

# Main execution
if __name__ == "__main__":
    # Example 1: Simple sequence prediction (e.g., sine wave)
    # Example 2: Long-term dependency task
    # Example 3: Gate behavior visualization
    # Example 4: Parameter sensitivity analysis
    pass
```

#### 3. Required Demonstrations

1. **Sequential Data Processing**: Use a meaningful dataset (e.g., time series prediction, sequence classification)

2. **Gate-level Computations**: Print and visualize intermediate gate values at each timestep

3. **Long-term Dependencies**: Create a specific experiment showing LSTM's ability to remember information over long sequences

4. **Parameter Analysis**: Show how different parameters affect each gate's behavior

#### 4. Visualization Requirements
- Plot training loss over epochs
- Visualize gate activations over time
- Show cell state evolution
- Compare predictions vs actual values

---

## Report Generation: `LSTM_Assignment_Report.docx`

Create a comprehensive Word document report with the following structure:

### Report Structure

**Title Page:**
- Assignment title: "Complex Computing Problem: LSTM Implementation from Scratch"
- Namal University Mianwali, Department of Computer Science
- Student name and registration number
- Date: January 18, 2026

**Table of Contents**

**1. Introduction (1 page)**
- Brief overview of LSTM networks
- Purpose of the assignment
- Objectives achieved

**2. Theoretical Background (2-3 pages)**

**2.1 LSTM Architecture**
- Explanation of why LSTMs were developed (vanishing gradient problem)
- Overview of the four gating mechanisms

**2.2 Mathematical Formulation**
- Present each equation with detailed explanation:
  - Forget Gate: What it does and why
  - Input Gate: Purpose and mechanism
  - Candidate Cell State: How new information is proposed
  - Cell State Update: How information is retained/forgotten
  - Output Gate: How hidden state is computed

**3. Implementation Details (3-4 pages)**

**3.1 Code Architecture**
- Class structure explanation
- Design decisions
- Why certain approaches were chosen

**3.2 Gate-Level Computations**
- Step-by-step walkthrough of one forward pass
- Include actual code snippets with explanations

**3.3 Implementation Challenges**
- Difficulties encountered
- How they were resolved

**4. Gate Behavior Analysis (3-4 pages)**

**4.1 Forget Gate Analysis**
- What values mean (close to 0 vs close to 1)
- When and why it activates
- Effect of weight initialization
- Effect of learning rate

**4.2 Input Gate Analysis**
- Role in controlling new information
- Behavior patterns observed
- Parameter sensitivity

**4.3 Output Gate Analysis**
- How it filters cell state
- Observed behavior patterns
- Parameter effects

**4.4 Cell State Evolution**
- How cell state changes over time
- Long-term vs short-term patterns

**5. Long-term Dependency Demonstration (2-3 pages)**
- Experimental setup
- Results showing LSTM's ability to preserve information
- Comparison with what vanilla RNN would struggle with
- Include graphs and visualizations

**6. Parameter Sensitivity Analysis (2-3 pages)**

**6.1 Learning Rate Effects**
- Test with different learning rates (0.001, 0.01, 0.1)
- Impact on each gate
- Include comparison plots

**6.2 Weight Initialization Effects**
- Different initialization strategies
- Impact on convergence and gate behavior

**6.3 Hidden Size Effects**
- How hidden dimension affects capacity
- Trade-offs observed

**7. Experimental Results (2-3 pages)**
- Dataset description
- Training process and convergence
- Performance metrics
- Visualizations of results

**8. Personal Understanding and Insights (2 pages)**
- Key learnings from implementing LSTM from scratch
- Intuition developed about how gates work together
- Understanding of why LSTM solves vanishing gradient problem
- Reflections on the mathematics vs implementation

**9. Conclusion (1 page)**
- Summary of work completed
- Achievement of objectives
- Future improvements possible

**10. References**
- Cite relevant papers (Hochreiter & Schmidhuber, 1997)
- Course lecture materials
- Any other resources used

**Appendix: Complete Code**
- Include full Python code with comments

### Formatting Requirements
- Font: Times New Roman, 12pt
- Spacing: 1.5 line spacing
- Margins: 1 inch all sides
- Page numbers
- Professional formatting
- All equations properly formatted
- Clear, labeled figures and plots
- Code snippets with syntax highlighting

### Critical Report Elements
1. **All equations must be explained in detail**
2. **Include screenshots/plots from code execution**
3. **Demonstrate understanding, not just implementation**
4. **Show parameter experimentation with concrete examples**
5. **Explain the "why" behind each gate's design**

---

## Additional Instructions for Cursor

1. **Code Quality**: Use clean, well-commented code with docstrings
2. **No Libraries**: Do NOT use PyTorch, TensorFlow, or Keras LSTM implementations
3. **Allowed Libraries**: NumPy for matrix operations, Matplotlib for visualization
4. **Testing**: Include validation that implementation works correctly
5. **Documentation**: Every function should be thoroughly documented
6. **Reproducibility**: Set random seeds for reproducible results

## Deliverables
1. `lstm_from_scratch.py` - Complete implementation
2. `LSTM_Assignment_Report.docx` - Comprehensive report
3. Generated plots and visualizations (automatically saved by code)

## Success Criteria
- LSTM correctly implements all 5 equations
- Code runs without errors
- Demonstrates clear understanding of gate mechanisms
- Shows long-term dependency preservation
- Report thoroughly explains both theory and implementation
- Parameter analysis shows thoughtful experimentation