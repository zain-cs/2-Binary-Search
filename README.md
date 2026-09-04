<h1 align="center">🎯 Binary Search</h1>

<p align="center">
  <i>An animated, beginner-friendly walkthrough of the Binary Search algorithm with two Python implementations.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Algorithm-Searching-4472C4?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Difficulty-Beginner-3fb950?style=for-the-badge"/>
</p>

---

## 📽️ Visual Walkthrough

Binary Search checks the **middle element** of the current range and eliminates the half that can't contain the target — shrinking the search space until it finds a match.

<p align="center">
  <img src="binary_search_demo.gif" alt="Binary Search animated walkthrough" width="680"/>
</p>

> 🔵 Blue = active search window · 🟡 Amber = `mid` being checked · ⚫ Dim = eliminated · 🟢 Green = found

---

## ⚙️ How It Works

1. Set `low = 0` and `high = length - 1`.
2. While `low <= high`: check `mid = (low + high) // 2`.
3. Match → return `mid`. Too small → `low = mid + 1`. Too big → `high = mid - 1`.
4. Window closes with no match → return `-1`.

> ⚠️ Requires **sorted** data — it won't work correctly otherwise.

---

## ⏱️ Complexity

| Case | Time | Space |
|---|---|---|
| Best | `O(1)` | `O(1)` |
| Average / Worst | `O(log n)` | `O(1)` |

A 1M-element array takes at most ~20 comparisons — versus up to 1,000,000 for Linear Search.

---

## 🐍 Implementation

**Function-based:**
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [5, 12, 19, 23, 28, 33, 42, 56, 67, 72, 88]
binary_search(arr, 42)
```

**Object-oriented** (with sorted insert via `add()`):
```python
class BinarySearch:
    def __init__(self, data=None):
        self.data = data if data is not None else []

    def search(self, target):
        low, high = 0, len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def add(self, item):
        self.data.append(item)
        self.data.sort()
```

> 💡 Full commented version with step-by-step print statements: [`binary_search.py`](./binary_search.py)

---

## ▶️ Run It

```bash
git clone https://github.com/zain-cs/2-Binary-Search.git
cd 2-Binary-Search
python binary_search.py
```

---

## 🗺️ Part of a DSA Series

📌 [Linear Search](https://github.com/zain-cs/1-Linear-Search) → **Binary Search** → more to come as I work through DSA.

---

<p align="center">
  Made with 🐍 by <a href="https://github.com/zain-cs">Muhammad Zain Ul Abidin</a>
</p>
