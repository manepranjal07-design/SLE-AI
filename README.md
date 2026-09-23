# 8-Puzzle Solver: Breadth-First Search (BFS) vs. A* Search Algorithm Comparison

## Project Overview

The 8-Puzzle is a fundamental benchmark problem in Artificial Intelligence used to evaluate graph traversal and pathfinding heuristics. It consists of a 3x3 grid containing 8 numbered tiles (1 through 8) and a single empty slot (`0`). A tile adjacent to the empty slot can be slid into it, with the objective of transitioning from a given initial arrangement to a designated goal configuration.

This project provides a comprehensive implementation, visual step-by-step path reconstructor, and empirical performance analysis comparing two foundational search strategies:
1. **Breadth-First Search (BFS):** An uninformed, blind search algorithm that explores state space level-by-level using a First-In-First-Out (FIFO) queue. While it guarantees finding the shortest solution path, its spatial and temporal complexity scales exponentially as path depth increases.
2. **A* Search:** An informed, heuristic-driven search algorithm that prioritizes state evaluation using the evaluation function \(f(n) = g(n) + h(n)\), where \(g(n)\) represents the exact cost to reach the current node and \(h(n)\) represents the estimated cost to the goal using the **Manhattan Distance** heuristic.