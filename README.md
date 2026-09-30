# 8-Puzzle Solver: BFS vs A* Search Algorithm Comparison

* The 8-Puzzle is a classic Artificial Intelligence problem used to demonstrate search algorithms, state-space exploration, pathfinding, and heuristic-based problem solving.
* The puzzle consists of a 3×3 grid containing eight numbered tiles from 1 to 8 and one empty space represented by 0.
* The objective is to transform an initial state into a predefined goal state by moving tiles into the empty space.

## Project Objectives

* Understand the 8-Puzzle as a state-space search problem.
* Implement Breadth-First Search (BFS).
* Implement A* Search.
* Understand the difference between uninformed and informed search.
* Use Manhattan Distance as a heuristic.
* Reconstruct and display the solution path.
* Count the number of nodes explored.
* Measure algorithm execution time.
* Compare BFS and A* performance.

## Problem Representation

* Each puzzle configuration is represented as a state.
* The value 0 represents the empty space.
* A valid move consists of moving a tile into the empty position.
* The empty space can have up to four possible movements: up, down, left, and right.
* The initial state used in the project is:

```text
1 2 3
5 0 6
4 7 8
```

* The goal state is:

```text
1 2 3
4 5 6
7 8 0
```

* The goal state is represented as:

```python
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
```

* The starting state is represented as:

```python
START = (1, 2, 3, 5, 0, 6, 4, 7, 8)
```

## State-Space Search

* Each puzzle configuration represents a node or state.
* A valid tile movement represents an edge between two states.
* The initial configuration is the initial node.
* The goal configuration is the goal node.
* The sequence of states from the initial state to the goal represents the solution path.

## Breadth-First Search

* BFS stands for Breadth-First Search.
* BFS is an uninformed search algorithm.
* It explores the search space level by level.
* BFS uses a FIFO queue.
* FIFO means First-In-First-Out.
* BFS first explores states at depth 1, then depth 2, then depth 3, and continues until the goal is found.
* Since every move in the 8-Puzzle has the same cost, BFS can find the shortest solution path.

## BFS Data Structure

* BFS uses Python's `deque`.

```python
from collections import deque
```

* A queue can be created using:

```python
queue = deque()
```

* A state is added using:

```python
queue.append(state)
```

* A state is removed using:

```python
queue.popleft()
```

* This provides FIFO behavior.

## BFS Working

* Add the initial state to the queue.
* Mark the initial state as visited.
* Remove the first state from the queue.
* Check whether the state is the goal.
* Generate all valid neighboring states.
* Add unvisited states to the queue.
* Store parent information for each state.
* Continue searching until the goal is reached or the queue becomes empty.
* Reconstruct the solution path using the stored parent information.

## BFS Characteristics

* Search type: Uninformed search.
* Data structure: FIFO queue.
* Heuristic: Not used.
* Complete: Yes, for finite state spaces.
* Optimal: Yes, when all moves have equal cost.
* Memory usage: Can be high.
* Search strategy: Level-by-level exploration.

## A* Search

* A* is an informed search algorithm.
* A* uses additional information about how close a state is to the goal.
* A* uses the evaluation function:

```text
f(n) = g(n) + h(n)
```

* `g(n)` represents the actual cost from the initial state to the current state.
* `h(n)` represents the estimated cost from the current state to the goal.
* `f(n)` represents the estimated total cost of reaching the goal through the current state.
* A* prioritizes states with smaller `f(n)` values.

## Manhattan Distance

* The project uses Manhattan Distance as the heuristic function.
* Manhattan Distance estimates the number of horizontal and vertical movements required to move a tile from its current position to its goal position.
* The formula is:

```text
Manhattan Distance =
|current row - goal row| +
|current column - goal column|
```

* The Manhattan Distance of the complete puzzle is calculated by adding the distances of all tiles.
* The blank tile represented by 0 is not included.

## Example of Manhattan Distance

* Suppose tile 5 is currently at row 1 and column 0.
* Its goal position is row 1 and column 1.
* The calculation is:

```text
Distance = |1 - 1| + |0 - 1|
         = 0 + 1
         = 1
```

* Therefore, tile 5 contributes 1 to the heuristic value.

## Why Manhattan Distance Is Used

* Manhattan Distance gives A* information about how close the tiles are to their goal positions.
* It helps A* decide which states are more promising.
* Unlike BFS, A* uses information about the goal while searching.

## A* Working

* Start with the initial puzzle state.
* Calculate its heuristic value.
* Add the state to a priority queue.
* Select the state with the smallest `f(n)` value.
* Check whether it is the goal.
* Generate valid neighboring states.
* Calculate `g(n)`, `h(n)`, and `f(n)` for each neighbor.
* Add promising states to the priority queue.
* Continue until the goal is reached.
* Reconstruct the solution path.

## A* Data Structure

* A* uses a priority queue.
* Python's `heapq` module can be used for the priority queue.

```python
import heapq
```

* The priority queue selects the state with the lowest priority or `f(n)` value.

## BFS vs A* Comparison

* BFS is an uninformed search algorithm.
* A* is an informed search algorithm.
* BFS does not use a heuristic.
* A* uses Manhattan Distance as a heuristic.
* BFS uses a normal queue.
* A* uses a priority queue.
* BFS explores states level by level.
* A* focuses on states that appear more promising based on `g(n) + h(n)`.
* BFS can use high memory.
* A* can also use significant memory.
* BFS is relatively simple to implement.
* A* is more complex because it requires a heuristic.
* Both can find optimal solutions under appropriate conditions.

## Solution Path Reconstruction

* Finding the goal state is not enough because the complete sequence of moves is also required.
* The program stores the parent state of each discovered state.
* When the goal is found, the program follows the parent references backward.
* The path is then reversed to display it from the initial state to the goal state.
* This allows the complete solution to be displayed.

## Performance Analysis

* The project compares the practical performance of BFS and A*.
* Important performance measurements include:

  * Execution time.
  * Number of nodes explored.
  * Solution depth.
  * Search efficiency.
* Execution time measures how long the algorithm takes to find the solution.
* Nodes explored represents the number of states processed during the search.
* Solution depth represents the number of moves required to reach the goal.
* Search efficiency measures how much of the search space is explored before reaching the goal.

## Test Cases

* The project can use different puzzle configurations.
* Easy example:

```text
1 2 3
4 5 6
7 0 8
```

* Medium example:

```text
1 2 3
5 0 6
4 7 8
```

* A more scrambled configuration can be used as a hard test case.
* Testing different configurations helps demonstrate how the algorithms behave as the problem becomes more difficult.

## Technologies Used

* Python 3.
* `collections.deque`.
* `heapq`.
* Tuples.
* Sets.
* Dictionaries.
* Functions.
* Loops.
* Priority queues.
* State-space representation.

## Important Python Components

* BFS uses `deque` for queue operations.

```python
from collections import deque

queue = deque()
queue.append(start)

current = queue.popleft()
```

* A* uses `heapq` for priority queue operations.

```python
import heapq
```

* The program uses sets to store visited states.

```python
visited = set()
```

* Visited states help prevent repeated exploration and cycles.

## Complexity

* The theoretical complexity of BFS depends on the branching factor and solution depth.
* General BFS complexity can be represented as:

```text
Time:  O(b^d)
Space: O(b^d)
```

* `b` represents the branching factor.
* `d` represents the depth of the shallowest solution.
* A* performance depends on the quality of its heuristic.
* Manhattan Distance helps A* guide the search toward promising states.
* Actual performance depends on the input state and implementation.

## Conceptual Difference

* BFS asks which states are closest to the starting state in terms of number of moves.
* A* considers both the cost already travelled and the estimated cost to the goal.
* BFS does not use information about the goal's location.
* A* uses Manhattan Distance to estimate how close a state is to the goal.

## Advantages of BFS

* Simple to understand and implement.
* Complete for a finite state space.
* Finds the shortest solution when every move has equal cost.
* Does not require a heuristic.
* Useful as a baseline for comparison.

## Limitations of BFS

* Can explore many unnecessary states.
* Memory usage can become large.
* Becomes less practical as the solution depth increases.

## Advantages of A*

* Uses heuristic information to guide the search.
* Can avoid exploring many irrelevant states.
* Can find optimal solutions when used with an appropriate admissible heuristic.
* Manhattan Distance is suitable for the 8-Puzzle.
* Demonstrates informed search.

## Limitations of A*

* More complex than BFS.
* Requires a heuristic function.
* Can still require significant memory.
* Performance depends on the heuristic and implementation.

## Project Outcome

* The project demonstrates two different AI search strategies for solving the same problem.
* BFS explores the state space systematically without additional information about the goal.
* A* uses Manhattan Distance to estimate which states are more promising.
* Both algorithms can be tested using the same puzzle configurations.
* Their solution depth, explored nodes, and execution time can be compared.
* The project demonstrates the difference between uninformed and informed search.

## Key AI Concepts

* State-space search.
* Graph traversal.
* Uninformed search.
* Informed search.
* Breadth-First Search.
* A* Search.
* Heuristic functions.
* Manhattan Distance.
* Priority queues.
* Search depth.
* Path reconstruction.
* Visited-state management.
* Performance benchmarking.
* Algorithm comparison.

## How to Run

* Install Python 3.x.
* Check the Python version using:

```text
python --version
```

* Run BFS using:

```text
python bfs.py
```

* Run A* using:

```text
python astar.py
```

* Run the profiling or benchmarking program using:

```text
python puzzle_profiling.py
```

## Profiling and Benchmarking

* Profiling helps identify where the program spends execution time.
* It can identify frequently executed functions.
* It can measure time spent in search operations.
* It can measure state-generation overhead.
* It can measure heuristic calculation cost.
* It can analyze queue and priority-queue operations.
* Repeated executions can provide more reliable performance measurements.

## Experimental Methodology

* Use the same initial state for BFS and A*.
* Use the same goal state.
* Run both algorithms.
* Record solution depth.
* Record the number of explored nodes.
* Record execution time.
* Compare the collected results.

## Important Observation

* Execution time can vary depending on:

  * Computer hardware.
  * Python version.
  * Operating system.
  * Background processes.
  * Number of repetitions.
  * Implementation details.
* Therefore, execution-time results are experimental measurements and are not universal values.
* The number of explored states and solution depth also depend on the selected puzzle.

## Conclusion

* The 8-Puzzle is useful for understanding search algorithms in Artificial Intelligence.
* BFS performs an uninformed level-by-level search.
* A* uses Manhattan Distance to guide its search.
* The project reconstructs the solution path.
* The project measures algorithm performance.
* Comparing BFS and A* demonstrates how different search strategies explore a search space differently.
* The project provides practical experience with state representation, search algorithms, heuristic search, path reconstruction, performance measurement, and algorithm comparison.

## Author

* Pranjal Vijemane.
* Engineering Student.
* Artificial Intelligence / Machine Learning.

## License

* This project was developed for educational and academic purposes as part of Artificial Intelligence coursework.

## Acknowledgement

* This project was developed as an academic implementation and learning exercise to understand search algorithms, heuristic functions, state-space problems, and algorithm performance analysis.
