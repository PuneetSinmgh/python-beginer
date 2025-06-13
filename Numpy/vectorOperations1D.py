# This module provides various vector operations using NumPy.
# It includes functions for vector addition, subtraction, scalar multiplication,
# dot product, element-wise multiplication, cross product, magnitude, unit vector,
# angle between vectors, and broadcasting.
# It also demonstrates how to handle vectors of different lengths in addition.

import numpy as np


u = [1,2]

v = [3,4]


# Vector addition
def vector_addition(u, v):
    return np.array(u) + np.array(v)

#vector addition without numpy
print( [u[i] + v[i] for i in range(len(u))])

#multi-dimentional vector addition

# Vector subtraction
def vector_subtraction(u, v):
    return np.array(u) - np.array(v)
# Scalar multiplication
def scalar_multiplication(scalar, vector):
    return scalar * np.array(vector)


# Dot product : # The dot product of two vectors u and v is defined as the sum of the products of their corresponding components.
# It can be computed using the formula: u . v = u1*v1 + u2*v2 + ... + un*vn
def dot_product(u, v):
    return np.dot(np.array(u), np.array(v))
#Dot product without numpy : multiplication of corresponding elements and then summing them up is done sequentially
def dot_product_without_numpy(u, v):
    return sum(u[i] * v[i] for i in range(len(u)))
# Example usage

# Element-wise multiplication
def elementwise_multiplication(u, v):
    return np.multiply(np.array(u), np.array(v))

# Cross product (only for 3D vectors)
def cross_product(u, v):
    return np.cross(np.array(u), np.array(v))
# Magnitude of a vector
def magnitude(vector):
    return np.linalg.norm(np.array(vector))
# Unit vector
def unit_vector(vector):
    mag = magnitude(vector)
    if mag == 0:
        raise ValueError("Cannot compute unit vector for zero vector")
    return np.array(vector) / mag
# Angle between two vectors in radians
def angle_between_vectors(u, v):
    u_norm = magnitude(u)
    v_norm = magnitude(v)
    if u_norm == 0 or v_norm == 0:
        raise ValueError("Cannot compute angle with zero vector")
    cos_theta = dot_product(u, v) / (u_norm * v_norm)
    return np.arccos(np.clip(cos_theta, -1.0, 1.0))  # Clip to avoid numerical errors

#broadcasting example
def broadcasting_example():
    """
    Demonstrates broadcasting in NumPy by adding a vector to each row of a matrix.
    
    :return: A matrix after broadcasting.
    """
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    vector = np.array([10, 20, 30])
    return matrix + vector

#what if lenths of u and v are not equal?
def vector_addition_with_different_lengths(u, v):
    """
    Adds two vectors of potentially different lengths by padding the shorter one with zeros.
    
    :param u: First vector.
    :param v: Second vector.
    :return: A new vector that is the element-wise sum of u and v.
    """
    max_length = max(len(u), len(v))
    u_padded = np.pad(u, (0, max_length - len(u)), 'constant')
    v_padded = np.pad(v, (0, max_length - len(v)), 'constant')
    return u_padded + v_padded
# Example usage of vector addition with different lengths
def vector_addition_with_different_lengths_example():
    u = [1, 2, 3]
    v = [4, 5]
    result = vector_addition_with_different_lengths(u, v)
    print("Vector Addition with Different Lengths:", result)
    return result


# Example usage
def __main__():
    u = [1, 2, 6, 8, 9]
    v = [3, 4, 5, 8, 2]
    print("Vector Addition:", vector_addition(u, v))
    print("Vector Subtraction:", vector_subtraction(u, v))
    print("Scalar Multiplication:", scalar_multiplication(2, u))
    print("Dot Product:", dot_product(u, v))
    print("Dot Product without NumPy:", dot_product_without_numpy(u, v))
    print("Element-wise Multiplication:", elementwise_multiplication(u, v))
    # Cross product requires 3D vectors
    u_3d = [1, 2, 3]
    v_3d = [4, 5, 6]
    print("Cross Product:", cross_product(u_3d, v_3d))
    print("Magnitude of u:", magnitude(u))
    print("Unit Vector of u:", unit_vector(u))
    print("Angle between u and v (radians):", angle_between_vectors(u, v))
    print("Broadcasting Example:\n", broadcasting_example())