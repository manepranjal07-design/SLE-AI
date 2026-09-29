# 8-Puzzle Solver: BFS vs A* Search Algorithm Comparison

## 📌 Project Overview

The **8-Puzzle** is a classic Artificial Intelligence problem used to demonstrate search algorithms, state-space exploration, pathfinding, and heuristic-based problem solving.

The puzzle consists of a **3×3 grid** containing eight numbered tiles (`1` to `8`) and one empty space represented by `0`.

The objective is to move the tiles and transform a given **initial state** into a predefined **goal state**.

For example:

### Initial State

```text
1 2 3
5 0 6
4 7 8
```

### Goal State

```text
1 2 3
4 5 6
7 8 0
```

Only tiles directly adjacent to the empty space can be moved into it.

This project implements two search algorithms to solve the puzzle:

* **Breadth-First Search (BFS)**
* **A* Search using Manhattan Distance**

The project compares their behavior and performance based on factors such as:

* Solution path
* Number of nodes explored
* Search depth
* Execution time
* Search efficiency
* Heuristic guidance

---

# 🎯 Objectives

The main objectives of this project are:

* To understand the 8-Puzzle as a state-space search problem.
* To implement **Breadth-First Search (BFS)**.
* To implement **A* Search**.
* To understand the difference between uninformed and informed search.
* To use **Manhattan Distance** as a heuristic.
* To reconstruct and display the solution path.
* To count the number of nodes explored during the search.
* To measure and compare algorithm execution time.
* To analyze how heuristic information affects search performance.
* To understand the practical trade-offs between BFS and A*.

---

# 🧩 Problem Definition

The 8-Puzzle can be represented as a state consisting of nine positions.

For example:

```text
1 2 3
5 0 6
4 7 8
```

The value `0` represents the empty space.

A valid move consists of moving one tile into the empty position.

Depending on the position of the empty space, there can be up to four possible moves:

```text
        Up
        ↑
Left ←  0  → Right
        ↓
       Down
```

The objective is to find a sequence of valid moves that transforms the initial state into the goal state.

---

# 🏁 Goal State

The goal configuration used in the project is:

```text
1 2 3
4 5 6
7 8 0
```

It is represented in the program as:

```python
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
```

---

# 🔢 State Representation

Each puzzle configuration is represented as a tuple containing nine values.

Example:

```python
START = (1, 2, 3, 5, 0, 6, 4, 7, 8)
```

This corresponds to:

```text
1 2 3
5 0 6
4 7 8
```

Using a tuple makes it easier to:

* Store states.
* Compare states.
* Track visited states.
* Use states in sets and dictionaries.
* Avoid modifying an existing state accidentally.

---

# 🔍 Search Space

The 8-Puzzle can be viewed as a **state-space search problem**.

Each puzzle configuration represents a state.

A movement of a tile creates a new state.

For example:

```text
Current State

1 2 3
5 0 6
4 7 8
```

Moving tile `5` into the empty space produces:

```text
1 2 3
0 5 6
4 7 8
```

The two configurations are connected in the search graph.

Therefore:

* **Node** → Puzzle state
* **Edge** → Valid tile movement
* **Initial node** → Starting configuration
* **Goal node** → Goal configuration
* **Path** → Sequence of moves required to solve the puzzle

---

# 🚀 Algorithm 1: Breadth-First Search (BFS)

## What is BFS?

**Breadth-First Search** is an uninformed search algorithm.

It explores the search space **level by level**.

BFS uses a **FIFO (First-In-First-Out) queue**.

The general idea is:

```text
Start
  ↓
Explore all states at depth 1
  ↓
Explore all states at depth 2
  ↓
Explore all states at depth 3
  ↓
Continue until goal is found
```

Because every move in the 8-Puzzle has the same cost, BFS finds the shortest solution path.

---

## BFS Data Structure

The implementation uses:

```python
from collections import deque
```

A queue is created using:

```python
queue = deque()
```

States are added using:

```python
queue.append(state)
```

and removed using:

```python
queue.popleft()
```

This provides FIFO behavior.

---

## BFS Working

The BFS process is:

1. Add the initial puzzle state to the queue.
2. Mark the initial state as visited.
3. Remove the first state from the queue.
4. Check whether it is the goal state.
5. Generate all valid neighboring states.
6. Add unvisited neighbors to the queue.
7. Store their parent information.
8. Continue until the goal is reached or the queue becomes empty.
9. Reconstruct the solution path using the stored parent information.

---

## BFS Characteristics

| Property        | BFS                                 |
| --------------- | ----------------------------------- |
| Search Type     | Uninformed                          |
| Data Structure  | FIFO Queue                          |
| Heuristic       | No                                  |
| Complete        | Yes, for finite state spaces        |
| Optimal         | Yes, when all moves have equal cost |
| Memory Usage    | High                                |
| Search Strategy | Level-by-level                      |

---

# ⭐ Algorithm 2: A* Search

## What is A*?

A* is an **informed search algorithm**.

Unlike BFS, A* uses additional information about how close a state is to the goal.

It uses the evaluation function:

```text
f(n) = g(n) + h(n)
```

where:

* `g(n)` = actual cost from the initial state to the current state
* `h(n)` = estimated cost from the current state to the goal
* `f(n)` = estimated total cost of the solution through that state

A* prioritizes states with smaller `f(n)` values.

---

# 📐 Manhattan Distance Heuristic

This project uses **Manhattan Distance** as the heuristic function.

The Manhattan Distance of a tile is the number of horizontal and vertical movements required to move that tile from its current position to its goal position.

For a tile:

```text
Manhattan Distance =
|current row - goal row| +
|current column - goal column|
```

The heuristic value of the complete puzzle is calculated by adding the Manhattan distances of all tiles.

The blank tile (`0`) is not included in the calculation.

---

## Example of Manhattan Distance

Suppose tile `5` is currently located at:

```text
Row = 1
Column = 0
```

and its goal position is:

```text
Row = 1
Column = 1
```

Then:

```text
Distance = |1 - 1| + |0 - 1|
         = 0 + 1
         = 1
```

Therefore, tile `5` contributes `1` to the heuristic value.

---

# 🧠 Why Manhattan Distance?

Manhattan Distance is useful for the 8-Puzzle because it estimates how many horizontal and vertical movements are needed to place the tiles in their correct positions.

It provides A* with information about the direction in which the search should proceed.

Unlike BFS, A* does not blindly explore every state at the same depth.

---

# 🔄 A* Working

The A* algorithm works approximately as follows:

1. Start with the initial puzzle state.
2. Calculate its heuristic value.
3. Add the state to a priority queue.
4. Select the state with the smallest `f(n)` value.
5. Check whether it is the goal.
6. Generate valid neighboring states.
7. Calculate `g(n)`, `h(n)`, and `f(n)` for each neighbor.
8. Add promising states to the priority queue.
9. Continue until the goal state is reached.
10. Reconstruct the solution path.

The priority queue allows the algorithm to process the state that currently appears most promising.

---

# 📊 BFS vs A* Comparison

| Feature         | BFS                          | A*                                           |
| --------------- | ---------------------------- | -------------------------------------------- |
| Search Type     | Uninformed                   | Informed                                     |
| Heuristic       | No                           | Yes                                          |
| Evaluation      | Depth                        | `g(n) + h(n)`                                |
| Data Structure  | Queue                        | Priority Queue                               |
| Guidance        | No goal-distance information | Uses heuristic                               |
| Shortest Path   | Yes for equal-cost moves     | Yes with an appropriate admissible heuristic |
| Memory          | Can be high                  | Can also be high                             |
| Search Behavior | Explores level-by-level      | Focuses toward promising states              |
| Implementation  | Relatively simple            | More complex                                 |
| Heuristic Used  | None                         | Manhattan Distance                           |

---

# 🔁 Solution Path Reconstruction

Finding the goal state is not enough for this project.

The program also reconstructs the sequence of states that leads from the initial state to the goal.

To achieve this, the program stores the **parent state** of each discovered state.

Conceptually:

```text
Initial State
     ↓
    State A
     ↓
    State B
     ↓
    State C
     ↓
Goal State
```

When the goal is found, the program follows the parent references backward:

```text
Goal
 ↓
State C
 ↓
State B
 ↓
State A
 ↓
Initial
```

The resulting path is then reversed so that it can be displayed from:

```text
Initial → Goal
```

This allows the complete solution to be visualized step by step.

---

# 🖥️ Example Solution Display

A solution can be represented as:

```text
Initial State:

1 2 3
5 0 6
4 7 8

        ↓

1 2 3
0 5 6
4 7 8

        ↓

1 2 3
4 5 6
0 7 8

        ↓

1 2 3
4 5 6
7 0 8

        ↓

Goal State:

1 2 3
4 5 6
7 8 0
```

The exact sequence depends on the selected initial state.

---

# 📈 Performance Analysis

The project does not only solve the puzzle. It also compares the practical performance of BFS and A*.

The following metrics can be collected:

### 1. Execution Time

Measures how long the algorithm takes to find the solution.

Example:

```text
BFS Time  = 0.0021 seconds
A* Time   = 0.0014 seconds
```

The actual values depend on the input puzzle and computer system.

---

### 2. Nodes Explored

This measures how many states were processed during the search.

A smaller number of explored nodes can indicate that the algorithm avoided exploring unnecessary parts of the search space.

---

### 3. Solution Depth

Solution depth represents the number of moves required to reach the goal.

For example:

```text
Solution Depth = 8 moves
```

For the same puzzle and equal move costs, BFS can be used as a shortest-path reference.

---

### 4. Search Efficiency

The project can compare how much of the available state space each algorithm explores before reaching the goal.

A* uses Manhattan Distance to guide its exploration.

---

# 🧪 Test Cases

The project can be tested using different puzzle difficulties.

For example:

### Easy

```text
1 2 3
4 5 6
7 0 8
```

### Medium

```text
1 2 3
5 0 6
4 7 8
```

### Hard

A more scrambled configuration can be used to increase the search depth and make the performance differences more visible.

Testing multiple configurations provides a better understanding of how the algorithms behave as the problem becomes more difficult.

---

# 🛠️ Technologies Used

The project is implemented using **Python**.

Main Python concepts and libraries used include:

* Python 3
* `collections.deque`
* `heapq`
* Tuples
* Sets
* Dictionaries
* Functions
* Loops
* Priority queues
* State-space representation

---

# 📁 Project Structure

A possible project structure is:

```text
8-Puzzle-BFS-AStar/
│
├── bfs.py
├── astar.py
├── puzzle.py
├── puzzle_profiling.py
├── README.md
├── Contribution_Log.md
└── results/
    └── performance_results.csv
```

The exact filenames may vary depending on the final project implementation.

---

# 🔧 Important Python Components

## BFS Queue

```python
from collections import deque

queue = deque()
queue.append(start)

current = queue.popleft()
```

The `deque` provides efficient insertion and removal from the front of the queue.

---

## A* Priority Queue

A* can use Python's `heapq` module:

```python
import heapq
```

The priority queue stores states according to their `f(n)` value.

Conceptually:

```text
f(n) = g(n) + h(n)
```

The state with the lowest priority is selected for exploration.

---

# 🔐 Visited States

The search algorithms need to avoid repeatedly exploring the same puzzle configuration.

For this purpose, visited states can be stored in a set:

```python
visited = set()
```

When a state is encountered, the program checks whether it has already been explored.

This prevents unnecessary repeated searches and helps avoid cycles.

---

# 🧮 Complexity

The theoretical complexity of search algorithms depends on the branching factor and solution depth.

For BFS, the time and space requirements can grow rapidly as the search depth increases.

A common general representation is:

```text
Time:  O(b^d)
Space: O(b^d)
```

where:

* `b` = branching factor
* `d` = depth of the shallowest solution

For A*, performance depends strongly on the quality of its heuristic.

With a useful heuristic such as Manhattan Distance, A* can reduce unnecessary exploration compared with uninformed search.

The exact practical performance depends on the input state and implementation.

---

# 🧠 BFS and A* — Conceptual Difference

The main difference can be understood as:

### BFS asks:

> "Which states are closest in terms of number of moves from the starting state?"

### A* asks:

> "Which states have the lowest estimated total cost to reach the goal?"

BFS does not use information about the goal's location.

A* uses the Manhattan Distance heuristic to estimate how close a state is to the goal.

---

# 📌 Advantages of BFS

* Simple to understand and implement.
* Complete for a finite state space.
* Finds the shortest solution when every move has equal cost.
* Does not require a heuristic.
* Useful as a baseline for comparison.

### Limitations

* Can explore many unnecessary states.
* Memory usage can become large.
* Becomes less practical as the solution depth increases.

---

# 📌 Advantages of A*

* Uses heuristic information to guide the search.
* Can avoid exploring many irrelevant states.
* Can find optimal solutions when used with an appropriate admissible heuristic.
* Manhattan Distance is particularly suitable for the 8-Puzzle.
* Provides a useful example of informed search.

### Limitations

* More complex than BFS.
* Requires a heuristic function.
* Can still require significant memory.
* Performance depends on the heuristic and implementation.

---

# 🎯 Project Outcome

The project demonstrates how two different AI search strategies can solve the same problem using different approaches.

**BFS** explores the state space systematically without additional knowledge about the goal.

**A*** uses the Manhattan Distance heuristic to estimate which states are more promising and prioritize them.

By running both algorithms on the same puzzle configurations and recording their performance, the project provides an empirical comparison of **uninformed search versus informed search**.

---

# 📚 Key AI Concepts Demonstrated

This project demonstrates several important Artificial Intelligence concepts:

* State-space search
* Graph traversal
* Uninformed search
* Informed search
* Breadth-First Search
* A* Search
* Heuristic functions
* Manhattan Distance
* Priority queues
* Search depth
* Path reconstruction
* Visited-state management
* Performance benchmarking
* Algorithm comparison

---

# 🚀 How to Run the Project

## Requirements

Install Python 3.x on your system.

Check the Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

Most components of this project use Python's standard library, so additional packages may not be required for the basic solver.

---

## Run BFS

```bash
python bfs.py
```

---

## Run A*

```bash
python astar.py
```

---

## Run Performance Testing

If the project contains a profiling or benchmarking script:

```bash
python puzzle_profiling.py
```

The benchmarking script can be used to execute the algorithms repeatedly and collect performance information.

---

# 📊 Profiling and Benchmarking

For more detailed performance analysis, the project may use profiling tools to identify where the program spends its execution time.

For example, Python profiling can help identify:

* Frequently executed functions
* Time spent in search operations
* State-generation overhead
* Heuristic calculation cost
* Queue/priority-queue operations

Repeated executions can also provide more reliable measurements than relying on a single run.

---

# 🔬 Experimental Methodology

To make the comparison meaningful, BFS and A* should be tested using the **same initial puzzle configurations**.

For every test case:

1. Use the same initial state for both algorithms.
2. Use the same goal state.
3. Run both algorithms.
4. Record the solution depth.
5. Record the number of explored nodes.
6. Record execution time.
7. Compare the results.

This ensures that the comparison is based on the same problem conditions.

---

# ⚠️ Important Observation

Execution time can vary depending on:

* Computer hardware
* Python version
* Operating system
* Background processes
* Number of repetitions
* Implementation details

Therefore, execution-time results should be treated as experimental measurements rather than universal values.

The number of explored states and solution depth are also dependent on the specific input puzzle.

---

# 📝 Conclusion

The 8-Puzzle provides a useful example for understanding search algorithms in Artificial Intelligence.

In this project, **BFS** and **A*** are implemented to solve the same puzzle problem.

BFS performs an uninformed level-by-level search, while A* uses the **Manhattan Distance heuristic** to guide its search toward promising states.

The project goes beyond simply finding a solution by also reconstructing the solution path and measuring algorithm performance.

The experimental comparison helps demonstrate an important AI concept: **the way an algorithm explores a search space can significantly affect the amount of computation required to find a solution.**

Overall, the project provides practical experience with:

```text
State Representation
       ↓
Search Algorithms
       ↓
BFS / A*
       ↓
Heuristic Search
       ↓
Path Reconstruction
       ↓
Performance Measurement
       ↓
Algorithm Comparison
```

---

# 👩‍💻 Author

**Pranjal Vijemane**

Engineering Student
Artificial Intelligence / Machine Learning

---

# 📜 License

This project was developed for educational and academic purposes as part of Artificial Intelligence coursework.

# 🙏 Acknowledgement

This project was developed as an academic implementation and learning exercise to understand search algorithms, heuristic functions, state-space problems, and algorithm performance analysis.
