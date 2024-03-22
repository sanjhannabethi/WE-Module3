def euler001(limit: int) -> int:
    sum_multiples = sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)
    return sum_multiples

# Test the function
print(euler001(1000))  # Output: sum of all multiples of 3 or 5 below 1000

def gEuler001(ns: list[int], limit: int) -> int:
    total_sum = sum(i for i in range(limit) if any(i % n == 0 for n in ns))
    return total_sum

# Test the function
print(gEuler001([3, 5], 1000))  # Output: sum of all multiples of 3 or 5 below 1000

# Test case 1
print("Test case 1:")
print("Expected output:", sum(i for i in range(10) if i % 2 == 0 or i % 3 == 0))
print("Actual output:", gEuler001([2, 3], 10))

# Test case 2
print("Test case 2:")
print("Expected output:", sum(i for i in range(50) if i % 7 == 0 or i % 11 == 0))
print("Actual output:", gEuler001([7, 11], 50))

# Test case 3
print("Test case 3:")
print("Expected output:", sum(i for i in range(100) if i % 2 == 0 or i % 5 == 0 or i % 7 == 0))
print("Actual output:", gEuler001([2, 5, 7], 100))

# Test case 4
print("Test case 4:")
print("Expected output:", sum(i for i in range(30) if i % 3 == 0 or i % 4 == 0 or i % 9 == 0))
print("Actual output:", gEuler001([3, 4, 9], 30))

# Test case 5
print("Test case 5:")
print("Expected output:", sum(i for i in range(1000) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0))
print("Actual output:", gEuler001([2, 3, 5, 7, 11], 1000))

# Edge case 1: ns empty list
print("Edge case 1:")
print("Expected output:", 0)  # No multiples to sum
print("Actual output:", gEuler001([], 10))

# Edge case 2: limit equals 0
print("Edge case 2:")
print("Expected output:", 0)  # No multiples to sum
print("Actual output:", gEuler001([2, 3], 0))

# Edge case 3: Large limit and small ns
print("Edge case 3:")
print("Expected output:", sum(i for i in range(1000000) if i % 2 == 0))
print("Actual output:", gEuler001([2], 1000000))

print("Edge case 4:")
print("Expected output:", 0)  # No multiples to sum
print("Actual output:", gEuler001([1000000, 2000000], 10))

# Edge case 5: Negative limit and ns
print("Edge case 5:")
print("Expected output:", 0)  # No multiples to sum
print("Actual output:", gEuler001([-2, -3], -10))

def gEuler001B(ns: list[int], limit: int) -> int:
    multiples_set = set()
    for num in ns:
        multiples_set |= set(range(num, limit, num))
    return sum(multiples_set)

# Test the function
print(gEuler001B([3, 5], 1000))  # Output: sum of all multiples of 3 or 5 below 1000

# Edge case 1: ns empty list
print("Edge case 1:")
print("Expected output:", 0)  # No multiples to sum
print("Actual output:", gEuler001B([], 10))
print()

# Edge case 2: limit equals 0
print("Edge case 2:")
print("Expected output:", 0)  # No multiples to sum
print("Actual output:", gEuler001B([2, 3], 0))
print()

# Edge case 3: Large limit and small ns
print("Edge case 3:")
print("Expected output:", sum(i for i in range(1000000) if i % 2 == 0))
print("Actual output:", gEuler001B([2], 1000000))
print()

# Edge case 4: Large ns and small limit
print("Edge case 4:")
print("Expected output:", 0)  # No multiples to sum
print("Actual output:", gEuler001B([1000000, 2000000], 10))
print()
