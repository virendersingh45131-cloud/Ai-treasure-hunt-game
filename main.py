"""
AI Treasure Hunt - Mini Project
Algorithms used:
1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. Greedy Best First Search

Run: python main.py
Only Python's built-in tkinter library is required.
"""

import tkinter as tk
from tkinter import messagebox
from collections import deque
import heapq

ROWS, COLS = 10, 14
CELL = 42

# 0 = open path, 1 = wall
MAZE = [
    [0,0,0,1,0,0,0,0,1,0,0,0,0,0],
    [1,1,0,1,0,1,1,0,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,0,1,1,1,1,0,1,0],
    [0,0,0,0,0,1,0,0,0,0,1,0,0,0],
    [1,1,1,1,0,1,1,1,1,0,1,1,1,0],
    [0,0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,1,1,1,0,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,1,1,1,0,1,1,1,1,0,0,0],
]
START = (0, 0)
GOAL = (9, 13)
DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]

def neighbors(node):
    r, c = node
    for dr, dc in DIRECTIONS:
        nxt = (r + dr, c + dc)
        nr, nc = nxt
        if 0 <= nr < ROWS and 0 <= nc < COLS and MAZE[nr][nc] == 0:
            yield nxt

def bfs(start, goal):
    queue = deque([start])
    parent = {start: None}
    visited_order = []
    while queue:
        current = queue.popleft()
        visited_order.append(current)
        if current == goal:
            break
        for nxt in neighbors(current):
            if nxt not in parent:
                parent[nxt] = current
                queue.append(nxt)
    return build_path(parent, goal), visited_order

def dfs(start, goal):
    stack = [start]
    parent = {start: None}
    visited_order = []
    while stack:
        current = stack.pop()
        if current in visited_order:
            continue
        visited_order.append(current)
        if current == goal:
            break
        # Reverse gives a consistent exploration order with the stack.
        for nxt in reversed(list(neighbors(current))):
            if nxt not in parent:
                parent[nxt] = current
                stack.append(nxt)
    return build_path(parent, goal), visited_order

def best_first(start, goal):
    def heuristic(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    heap = [(heuristic(start), 0, start)]
    parent = {start: None}
    seen = set()
    visited_order = []
    counter = 1
    while heap:
        _, _, current = heapq.heappop(heap)
        if current in seen:
            continue
        seen.add(current)
        visited_order.append(current)
        if current == goal:
            break
        for nxt in neighbors(current):
            if nxt not in seen and nxt not in parent:
                parent[nxt] = current
                heapq.heappush(heap, (heuristic(nxt), counter, nxt))
                counter += 1
    return build_path(parent, goal), visited_order

def build_path(parent, goal):
    if goal not in parent:
        return []
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    return list(reversed(path))

class TreasureHuntApp:
    def __init__(self, root):
        self.root = root
        root.title("AI Treasure Hunt - Search Algorithms")
        root.configure(bg="#101827")
        root.resizable(False, False)

        tk.Label(root, text="AI TREASURE HUNT", font=("Arial", 22, "bold"),
                 fg="#f8c14a", bg="#101827").pack(pady=(14, 2))
        tk.Label(root, text="Choose an AI search method to find the treasure",
                 font=("Arial", 10), fg="#cbd5e1", bg="#101827").pack(pady=(0, 10))

        controls = tk.Frame(root, bg="#101827")
        controls.pack(pady=4)
        self.algorithm = tk.StringVar(value="BFS")
        for label, value in [("BFS", "BFS"), ("DFS", "DFS"), ("Best First", "BEST")]:
            tk.Radiobutton(controls, text=label, value=value, variable=self.algorithm,
                           indicatoron=False, width=11, font=("Arial", 10, "bold"),
                           bg="#263449", fg="white", selectcolor="#087e8b",
                           activebackground="#087e8b", activeforeground="white",
                           relief="flat", padx=5, pady=7).pack(side="left", padx=4)

        self.canvas = tk.Canvas(root, width=COLS*CELL, height=ROWS*CELL,
                                bg="#101827", highlightthickness=0)
        self.canvas.pack(padx=14, pady=10)

        buttons = tk.Frame(root, bg="#101827")
        buttons.pack(pady=4)
        tk.Button(buttons, text="FIND TREASURE", command=self.solve,
                  bg="#087e8b", fg="white", activebackground="#0b9aa8",
                  font=("Arial", 10, "bold"), relief="flat", padx=16, pady=9).pack(side="left", padx=5)
        tk.Button(buttons, text="RESET", command=self.draw_maze,
                  bg="#334155", fg="white", activebackground="#475569",
                  font=("Arial", 10, "bold"), relief="flat", padx=16, pady=9).pack(side="left", padx=5)

        self.status = tk.Label(root, text="S = Start     T = Treasure     Blue = explored     Green = final path",
                               font=("Arial", 9), fg="#cbd5e1", bg="#101827")
        self.status.pack(pady=(8, 14))
        self.draw_maze()

    def draw_maze(self, explored=None, path=None):
        explored = set(explored or [])
        path = set(path or [])
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x1, y1 = c*CELL, r*CELL
                x2, y2 = x1+CELL, y1+CELL
                pos = (r,c)
                if MAZE[r][c] == 1:
                    color = "#334155"
                elif pos in path:
                    color = "#22c55e"
                elif pos in explored:
                    color = "#2563eb"
                else:
                    color = "#e2e8f0"
                self.canvas.create_rectangle(x1+1, y1+1, x2-1, y2-1,
                                             fill=color, outline="#64748b")
                if pos == START:
                    label, fg = "S", "white"
                elif pos == GOAL:
                    label, fg = "T", "white"
                else:
                    label, fg = "", "#0f172a"
                if label:
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=label,
                                            fill=fg, font=("Arial", 15, "bold"))

    def solve(self):
        method = self.algorithm.get()
        if method == "BFS":
            path, visited = bfs(START, GOAL)
            name = "Breadth First Search (BFS)"
        elif method == "DFS":
            path, visited = dfs(START, GOAL)
            name = "Depth First Search (DFS)"
        else:
            path, visited = best_first(START, GOAL)
            name = "Greedy Best First Search"

        self.draw_maze(visited, path)
        if path:
            self.status.config(text=f"{name}: Treasure found!  Path length: {len(path)-1} steps  |  Visited: {len(visited)} cells",
                               fg="#86efac")
        else:
            self.status.config(text=f"{name}: No path to the treasure was found.", fg="#fca5a5")
            messagebox.showinfo("Search complete", "No path to the treasure was found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TreasureHuntApp(root)
    root.mainloop()
