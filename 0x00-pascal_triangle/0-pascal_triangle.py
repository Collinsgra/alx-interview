def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        # Initialize the row with None, then fill it with 1s at the ends
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1
        
        # Each triangle element is the sum of the two elements above it
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    
    return triangle
