{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "deb06c6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"Summary : \n",
    "We can create NumPy arrays from a Python List or manually.\n",
    "Indexing is used to access specific elements of an array.\n",
    "Slicing is used to extract a specific subset of a string. \n",
    "NumPy functions include:\n",
    "Universal functions\n",
    "Boolean operations\n",
    "Aggregation\n",
    "Broadcasting\n",
    "\"\"\"\"\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ee159f5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 4, 2, 5, 3])"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Create an Array\n",
    "# Array of integers:\n",
    "np.array([1, 4, 2, 5, 3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fc71ce32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3.14, 4.  , 2.  , 3.  ])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array([3.14, 4, 2, 3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "27d7ffb5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1., 2., 3., 4.], dtype=float32)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array([1, 2, 3, 4], dtype='float32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "71ab8bb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# A list of lists in converted to a 2-dimensional array\n",
    "original_list = [[1,2,3],[3,4,5],[6,7,8]]\n",
    "two_dimensional_array = np.array(original_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "25fd1623",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 0., 0.],\n",
       "       [0., 1., 0.],\n",
       "       [0., 0., 1.]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# An array of length 10, filled with 0:\n",
    "np.zeros(10, dtype=int)\n",
    "# An array of size 3x5 filled with 1.0 (float)\n",
    "np.ones((3, 5), dtype=float)\n",
    "# An array of size 3x5 filled with 3.14\n",
    "np.full((3, 5), 3.14)\n",
    "# An array containing a linear sequence starting at 0 and \n",
    "# going up to 20, with steps of 2\n",
    "np.arange(0, 20, 2)\n",
    "# An array of 5 numbers, linearly spaced between 0 and 1\n",
    "np.linspace(0, 1, 5)\n",
    "# An array of the given shape and populate it with random\n",
    "# samples. You can also try using \"randint\" and \"normal\"\n",
    "np.random.random((3, 3))\n",
    "# The identity matrix of size 3\n",
    "np.eye(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "88c9fae5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of dimensions:  1\n",
      "Shape:  (6,)\n",
      "Size:  6\n",
      "Type:  int32\n"
     ]
    }
   ],
   "source": [
    "np.random.seed(0)\n",
    "x1 = np.random.randint(10, size=6)  \n",
    "# 1-dimensional array\n",
    "print(\"Number of dimensions: \", x1.ndim)\n",
    "print(\"Shape: \", x1.shape)\n",
    "print(\"Size: \", x1.size)\n",
    "print(\"Type: \", x1.dtype)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "01f5d408",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 0 3 3 7 9]\n",
      "5\n",
      "9\n",
      "5\n",
      "[   5 1000    3    3    7    9]\n",
      "[5 3 3 3 7 9]\n"
     ]
    }
   ],
   "source": [
    "## Accessing a single element\n",
    "\n",
    "print(x1)\n",
    "# The first element\n",
    "print(x1[0])\n",
    "# The last element\n",
    "print(x1[-1])\n",
    "\n",
    "x2 = np.random.randint(10, size=(3, 4))  \n",
    "# 2-dimensional array\n",
    "print(x2[0,1])\n",
    "\n",
    "# You can also modify values:\n",
    "x1[1] = \"1000\"\n",
    "print(x1)\n",
    "\n",
    "# Mind the type \n",
    "x1[1] = 3.14\n",
    "print(x1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c43056ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 3 3 3 7]\n",
      "[9]\n",
      "[5 3 7]\n"
     ]
    }
   ],
   "source": [
    "## Accessing several elements \n",
    "# First 5 elements\n",
    "print(x1[:5])\n",
    "# Elements from the 6th on\n",
    "print(x1[5:])  \n",
    "# Every two elements\n",
    "print(x1[::2])  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0dc0003a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([9, 7, 3, 3, 3, 5])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x1[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e2e148bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 3, 2, 1])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Concatenating arrays\n",
    "x = np.array([1, 2, 3])\n",
    "y = np.array([3, 2, 1])\n",
    "np.concatenate([x, y])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e03260f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [9, 8, 7],\n",
       "       [6, 5, 4]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.array([1, 2, 3])\n",
    "grid = np.array([[9, 8, 7], [6, 5, 4]])\n",
    "np.vstack([x, grid])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f5c0b82a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.11111111 0.5        0.16666667 0.11111111 0.2       ]\n",
      "2.41 s ± 393 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)\n"
     ]
    }
   ],
   "source": [
    "## Operating on Numpy Arrays\n",
    "def calculate_inverse(values):    \n",
    "    output = np.empty(len(values))    \n",
    "    for i in range(len(values)):        \n",
    "        output[i] = 1.0 / values[i]    \n",
    "    return output       \n",
    "\n",
    "values = np.random.randint(1, 10, size=5)\n",
    "print(calculate_inverse(values))\n",
    "\n",
    "large_array = np.random.randint(1, 100, size=1000000)\n",
    "\n",
    "# This is a Jupyter notebook tool to measure the execution\n",
    "# time of an instruction\n",
    "%timeit calculate_inverse(large_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c43fe8ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 ms ± 125 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)\n"
     ]
    }
   ],
   "source": [
    "%timeit (1.0 / large_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a035b2fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x     = [0 1 2 3]\n",
      "x + 5 = [5 6 7 8]\n",
      "x - 5 = [-5 -4 -3 -2]\n",
      "x * 2 = [0 2 4 6]\n",
      "x / 2 = [0.  0.5 1.  1.5]\n",
      "x // 2 = [0 0 1 1]\n"
     ]
    }
   ],
   "source": [
    "## Universal Functions\n",
    "\n",
    "# Simple mathematics first\n",
    "x = np.arange(4)\n",
    "print(\"x     =\", x)\n",
    "print(\"x + 5 =\", x + 5)\n",
    "print(\"x - 5 =\", x - 5)\n",
    "print(\"x * 2 =\", x * 2)\n",
    "print(\"x / 2 =\", x / 2)\n",
    "# Divide and round\n",
    "print(\"x // 2 =\", x // 2)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ad08472c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Absolute value:  [2 1 1 2]\n",
      "Exponential:  [0.13533528 0.36787944 2.71828183 7.3890561 ]\n",
      "Logarithm:  [0.69314718 0.         0.         0.69314718]\n"
     ]
    }
   ],
   "source": [
    "x = [-2, -1, 1, 2]\n",
    "\n",
    "print(\"Absolute value: \", np.abs(x))\n",
    "print(\"Exponential: \", np.exp(x))\n",
    "print(\"Logarithm: \", np.log(np.abs(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "fdd35712",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ True,  True, False],\n",
       "       [ True,  True,  True],\n",
       "       [False,  True, False]])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Booleans Operations\n",
    "x = np.random.rand(3,3)\n",
    "x > 0.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cf87dbd2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 0, 1, 1, 1, 2], dtype=int64),\n",
       " array([0, 1, 0, 1, 2, 1], dtype=int64))"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.where(x > 0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "5952948d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "49.09899667867994"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L = np.random.random(100)\n",
    "np.sum(L)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2d954464",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "102 ms ± 9.8 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)\n",
      "292 µs ± 3.59 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)\n"
     ]
    }
   ],
   "source": [
    "%timeit sum(large_array)\n",
    "%timeit np.sum(large_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "bde6653d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.81001412 0.08782143 0.15618846 0.73099033]\n",
      " [0.6427996  0.09425156 0.1035502  0.32354189]\n",
      " [0.3706353  0.87966194 0.44429964 0.67253984]]\n",
      "Sum of all elements of M:  5.316294300734639\n",
      "Sums of the columns of M:  [1.82344903 1.06173492 0.7040383  1.72707205]\n"
     ]
    }
   ],
   "source": [
    "## Aggregation\n",
    "\n",
    "M = np.random.random((3, 4))\n",
    "print(M)\n",
    "# Note the syntax variable.function instead of \n",
    "# np.fonction(variable). Both are acceptable if\n",
    "# variable is a Numpy array.\n",
    "print(\"Sum of all elements of M: \", M.sum())\n",
    "print(\"Sums of the columns of M: \", M.sum(axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "52451130",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 6, 7])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = np.array([0, 1, 2])\n",
    "b = np.array([5, 5, 5])\n",
    "a + b # same as a + 5 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "801ad9a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 6, 7])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# same as a + b \n",
    "a + 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "6f77b701",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "M is: \n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 1. 1.]]\n",
      "M+a is: \n",
      " [[1. 2. 3.]\n",
      " [1. 2. 3.]\n",
      " [1. 2. 3.]]\n"
     ]
    }
   ],
   "source": [
    "M = np.ones((3, 3))\n",
    "print(\"M is: \\n\", M)\n",
    "print(\"M+a is: \\n\", M+a)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
