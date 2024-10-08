class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.values, other.values)])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.values, other.values))

    def magnitude(self):
        return sum(a ** 2 for a in self.values) ** 0.5

    def __repr__(self):
        return f"Vector({self.values})"

# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Vector addition
v_add = v1 + v2
print("Addition:", v_add)

# Vector subtraction
v_sub = v1 - v2
print("Subtraction:", v_sub)

# Dot product
v_dot = v1.dot(v2)
print("Dot Product:", v_dot)

# Magnitude of v1
v1_magnitude = v1.magnitude()
print("Magnitude of v1:", v1_magnitude)
