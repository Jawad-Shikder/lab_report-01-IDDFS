# 🔍 IDDFS Grid Pathfinding — Python Implementation

This repository contains a Python implementation of **Iterative Deepening Depth-First Search (IDDFS)** for finding a path in a 2D grid.  
Cells with `0` are free to move, while cells with `1` are blocked.  
The algorithm starts from a **Start** position and searches for a **Target** position using IDDFS.

## 🚀 Features

- Takes grid input directly from the user  
- Supports any grid size (MxN)  
- Finds the shortest depth at which the target is discovered  
- Displays traversal order exactly like shown in lab tasks  
- Follows the format required by academic lab reports  

## ✔ Case 1 Input

```4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
0 0
2 3
```

## 📤 Case 1 Output

```Path found at depth <depth> using IDDFS
Traversal Order: [(x1, y1), (x2, y2), ...]
```

## ✔ Case 2 Input

```3 3 
0 1 0
0 1 0
0 1 0
0 0
2 2
```

## 📤 Case 2 Output

```Path not found at max depth 6 using IDDFS
```

```Path not found at depth 6 using IDDFS
```




