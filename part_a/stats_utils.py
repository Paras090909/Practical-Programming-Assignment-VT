import math
from collections import Counter

def calculate_mean(data):
    """Calculate the arithmetic mean of a list of numbers."""
    if not data:
        raise ValueError("Dataset cannot be empty")
    return sum(data) / len(data)

def calculate_median(data):
    """Calculate the median of a list of numbers."""
    if not data:
        raise ValueError("Dataset cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

def calculate_mode(data):
    """Calculate the mode(s) of a list of numbers. Returns a list of modes and their frequency."""
    if not data:
        raise ValueError("Dataset cannot be empty")
    counts = Counter(data)
    max_count = max(counts.values())
    
    # If all values occur the same number of times, there is no unique mode
    if max_count == 1 and len(data) > 1:
        return [], 0
        
    modes = [val for val, count in counts.items() if count == max_count]
    return modes, max_count

def calculate_variance(data, is_sample=True):
    """Calculate the variance of a list of numbers (sample variance by default)."""
    if len(data) < 2 and is_sample:
        raise ValueError("Sample variance requires at least 2 data points")
    if not data:
        raise ValueError("Dataset cannot be empty")
        
    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    denominator = len(data) - 1 if is_sample else len(data)
    return sum(squared_diffs) / denominator

def calculate_std_dev(data, is_sample=True):
    """Calculate the standard deviation of a list of numbers."""
    return math.sqrt(calculate_variance(data, is_sample))

def calculate_z_scores(data):
    """Calculate Z-Scores for all elements in a list."""
    mean = calculate_mean(data)
    std = calculate_std_dev(data, is_sample=True)
    if std == 0:
        return [0.0] * len(data)
    return [(x - mean) / std for x in data]

def calculate_pearson_correlation(x, y):
    """Calculate the Pearson Correlation Coefficient between two lists."""
    if len(x) != len(y):
        raise ValueError("Datasets must be of the same length")
    n = len(x)
    if n == 0:
        raise ValueError("Datasets cannot be empty")
        
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    
    num = sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y))
    den_x = sum((x_i - mean_x) ** 2 for x_i in x)
    den_y = sum((y_i - mean_y) ** 2 for y_i in y)
    
    if den_x == 0 or den_y == 0:
        return 0.0 # Avoid division by zero
        
    return num / math.sqrt(den_x * den_y)

def print_table(headers, rows, title=None):
    """Helper to print a beautiful, aligned text table."""
    # Convert all cells to strings
    str_rows = [[str(cell) for cell in row] for row in rows]
    
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in str_rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))
            
    # Format line separator
    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    
    # Printing
    if title:
        print("\n" + "=" * (sum(col_widths) + len(col_widths) * 3 + 1))
        print(f" {title.upper()} ".center(sum(col_widths) + len(col_widths) * 3 + 1, "="))
        print("=" * (sum(col_widths) + len(col_widths) * 3 + 1))
        
    print(separator)
    header_line = "|" + "|".join(f" {h.center(w)} " for h, w in zip(headers, col_widths)) + "|"
    print(header_line)
    print(separator)
    
    for row in str_rows:
        row_line = "|" + "|".join(f" {cell.ljust(w)} " for cell, w in zip(row, col_widths)) + "|"
        print(row_line)
        
    print(separator)
