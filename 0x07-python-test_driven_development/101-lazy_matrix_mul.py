#!/usr/bin/python3

"""Function that multiplies 2 matrices."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of 2 matrices.

    Args:
        m_a (list of lists of ints/floats): The First Matrix.
        m_b (list of lists of ints/floats): The Second Matrix.
    """

    return (np.matmul(m_a, m_b))
