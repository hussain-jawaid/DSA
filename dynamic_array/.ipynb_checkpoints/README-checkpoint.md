# Own Dynamic Array in Python

This project is a manual implementation of a **dynamic array** (similar to Python's built-in list) using **low-level C-type arrays (`ctypes`)** in Python.

I built this during my **Data Structures and Algorithms (DSA)** learning journey to understand how dynamic arrays work under the hood — including resizing, indexing, slicing, and memory handling.

> Built and tested inside a **Jupyter Notebook environment** (e.g., VS Code, Jupyter Lab, Google Colab)

---

## Features

- Append, Insert, Pop, Remove
- Indexing (`arr[2]`)
- Slicing (`arr[1:4]`, `arr[::-1]`)
- Extend with another array
- Operator Overloading:
  - `+` → merge two arrays
  - `sum()` support
- Clear, Delete by index
- Manual resizing like low-level arrays

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/hussain-jawaid/OwnDynamicArray.git
cd OwnDynamicArray