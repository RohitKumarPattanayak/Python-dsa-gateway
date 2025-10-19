# Time and Space Complexity

## Time Complexity

### Definition
**Time complexity** is the rate of increase in execution time with respect to the input/payload size.

> ❌ **Common Misconception**: Time complexity is NOT simply the time taken to run code.
> ✅ **Correct Understanding**: It measures how the runtime grows as input size increases.

### Key Concepts
- **Graphical Representation**: Time complexity curves visualize the relationship between input size and execution time
- **Notation**: Measured using Big O notation
- **Big O Notation**: Represented as `O(n)`, where `n` is the size of the input/payload

### Types of Time Complexity

| Notation | Type | Description |
|----------|------|-------------|
| `O(1)` | **Best Case** (Omega Ω) | Constant time - execution time doesn't change with input size |
| `O(n)` | **Average Case** (Theta Θ) | Linear time - execution time grows proportionally with input |
| `O(n²)` | **Worst Case** (Big O) | Quadratic time - execution time grows quadratically with input |

### Calculation Rules

When calculating time complexity, follow these important rules:

1. **Ignore constant values**
2. **Ignore lower-order terms**
3. **Ignore coefficient multipliers**

#### Example Calculation

Given: `O(8n² + 5n + 3)`

**Step 1**: Start with `O(8n² + 5n + 3)`

**Step 2**: Identify components
- `3` → Constant term
- `5n` → Lower-order term (when compared to `n²`)
- `8n²` → Highest-order term

**Step 3**: Apply rules
- Remove constant: `O(8n² + 5n)`
- Remove lower-order terms: `O(8n²)`
- Remove coefficient: `O(n²)`

**Final Result**: `O(n²)`



---

## Space Complexity

### Definition
**Space complexity** measures the total memory space required by an algorithm, expressed using Big O notation.

### Formula
```
Space Complexity = Auxiliary Space + Input Space
```

### Components

#### Auxiliary Space
- Extra memory used by the algorithm during execution
- Includes variables, data structures, and function call stack space
- Does NOT include the input data

#### Input Space
- Memory required to store the input data
- Fixed based on the size of the input

### Important Note
> ⚠️ **Best Practice**: Never modify input variables to save space. This can lead to unexpected behavior and side effects.

---

## Summary

Understanding time and space complexity is crucial for:
- **Algorithm Analysis**: Comparing different solutions
- **Performance Optimization**: Identifying bottlenecks
- **Scalability Planning**: Predicting behavior with larger inputs
- **Resource Management**: Balancing time vs. space trade-offs