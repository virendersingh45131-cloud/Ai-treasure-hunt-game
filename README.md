# AI Treasure Hunt - Mini Project

## Project idea
A small maze game in which an AI search algorithm tries to travel from the Start (S) to the Treasure (T).

## Syllabus methods used
1. **Breadth First Search (BFS):** explores level by level and finds a shortest path when every move has equal cost.
2. **Depth First Search (DFS):** follows one route deeply before backtracking. It may find a path, but it does not guarantee the shortest path.
3. **Greedy Best First Search:** selects the next cell using the Manhattan-distance heuristic (estimated distance to the treasure). It is guided by the goal but does not guarantee the shortest path.

## Requirements
- Python 3
- Tkinter (usually included with standard Python installations)

## How to run on Windows
1. Extract the ZIP file.
2. Open the `ai_treasure_hunt_project` folder in VS Code.
3. Open Terminal > New Terminal.
4. Run: `python main.py`
5. Select BFS, DFS, or Best First, then click **FIND TREASURE**.
6. Click **RESET** to clear the previous result.

If `python` is not recognized, try `py main.py`.

## Colour guide
- Dark grey: wall
- White: unvisited path
- Blue: cells explored by the algorithm
- Green: final path
- S: starting point
- T: treasure

## Suggested project explanation / viva
**Problem:** Find a route through a maze from a starting point to a target.

**Input:** A fixed maze, a start cell, a goal cell, and the selected search method.

**Process:** The selected algorithm explores connected open cells and records each cell's parent. The parent links are used to rebuild the route.

**Output:** The explored cells, final route, route length, and number of visited cells.

**Comparison:** BFS guarantees the shortest path in this unweighted maze. DFS is useful for understanding backtracking but may return a longer path. Greedy Best First uses Manhattan distance to guide the search and may reach the goal quickly, but it is not guaranteed to find the shortest route.

## Files
- `main.py` - complete application code
- `README.md` - setup and project explanation
