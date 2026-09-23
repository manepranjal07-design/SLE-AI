# AI Contribution Log & Engineering Transparency Statement

This document provides a comprehensive log of the collaboration between the human developer and Generative AI systems (Gemini) during the architectural design, implementation, benchmarking, and documentation of the **8-Puzzle BFS vs. A* Search** project.

# AI Contribution Log

## Project: 8-Puzzle — BFS vs A* Search

This contribution log records the development process of the 8-Puzzle project and clearly separates the work directed and performed by the human contributor from the assistance provided by AI.

---

## Step 1: Benchmarking and Profiling Setup (`py-spy`)

### What I Did

* Decided to benchmark and profile BFS and A* Search for the 8-Puzzle problem.
* Provided the initial profiling approach and code patterns from my existing `bfs_dfs` graph project.
* Specified that the profiling should compare BFS and A* Search on different 8-Puzzle difficulty levels.
* Requested repeated executions so that the profiler would have enough execution time to collect meaningful performance data.

### What AI Did

* Created `puzzle_profiling.py` for automated performance testing.
* Added multiple test cases representing **Easy, Medium, and Hard** puzzle configurations.
* Used repeated iterations (`REPETITIONS = 5000`) to create a sufficient profiling window for `py-spy`.
* Provided commands for generating:

  * SVG flamegraphs
  * Speedscope profiling traces
* Helped organize the profiling workflow so that the performance of BFS and A* could be compared consistently.

---

## Step 2: Core Algorithm Development — BFS and A*

### What I Did

* Requested complete implementations of **Breadth-First Search (BFS)** and **A* Search** for the 8-Puzzle.
* Specified that the program should:

  * Solve the puzzle.
  * Display the sequence of tile movements.
  * Show the number of nodes expanded.
  * Allow comparison between BFS and A*.
* Decided that the implementation should remain understandable and suitable for the project requirements.

### What AI Did

* Implemented BFS using Python's `collections.deque`.
* Implemented A* Search using Python's `heapq` priority queue.
* Represented each puzzle state as a flat tuple such as:

```text
(1, 2, 3, 4, 5, 6, 7, 8, 0)
```

* Used tuples because they are hashable and can efficiently be stored in visited sets.
* Implemented the **Manhattan Distance heuristic** for A* Search.
* Pre-computed goal-state coordinates to make Manhattan Distance calculations more efficient.
* Added a sequential counter to A* priority-queue entries to avoid tuple-comparison errors when two nodes have the same priority.
* Implemented `reconstruct_path()` to recover the solution path.
* Implemented `print_board()` to display each 8-Puzzle state as a readable 3×3 grid.
* Added node-expansion counting to support the BFS vs A* performance comparison.

---

## Step 3: Project Documentation and Structure

### What I Did

* Requested documentation for the project, including:

  * `README.md`
  * AI contribution log
  * Project structure
  * Running instructions
* Reviewed the initial documentation and identified that it was too abstract for the purpose of the project.
* Requested a more direct, step-by-step record of the actual development process.
* Ensured that the documentation clearly distinguishes my decisions and directions from AI-generated implementation assistance.

### What AI Did

* Created the initial `README.md`.
* Added sections explaining:

  * The 8-Puzzle problem.
  * BFS and A* Search.
  * Manhattan Distance.
  * Project features.
  * Performance comparison.
  * Project structure.
* Created and organized this contribution log.
* Reformatted the documentation into a clearer chronological development record.

---

## Step 4: System Integration and Execution Setup

### What I Did

* Requested a complete setup procedure for assembling and running the project locally.
* Integrated and tested the provided code on my local system.
* Tested the puzzle-solving scripts and profiling workflow.
* Checked the generated results and execution behaviour.

### What AI Did

* Organized the project into a step-by-step setup workflow.
* Explained how to:

  1. Create the project directory.
  2. Add the required Python files.
  3. Install required dependencies.
  4. Run the BFS and A* implementation.
  5. Run the profiling script.
  6. Generate `py-spy` flamegraphs and Speedscope traces.
* Helped troubleshoot execution and setup issues encountered during testing.

---

## Step 5: Testing and Performance Comparison

### What I Did

* Ran the implemented algorithms on different 8-Puzzle input cases.
* Compared the output produced by BFS and A*.
* Checked the solution paths and node-expansion counts.
* Used profiling results to observe how the algorithms behaved during execution.

### What AI Did

* Helped structure the test cases and comparison format.
* Assisted in interpreting the profiling output.
* Helped identify useful metrics for comparing the algorithms, including:

  * Execution behaviour
  * Number of expanded nodes
  * Solution path length
  * Search efficiency
* Helped explain how the Manhattan Distance heuristic affects A* Search.

---

## Step 6: Final Review and Project Refinement

### What I Did

* Reviewed the complete project and its documentation.
* Checked whether the implementation, profiling setup, and README matched the original project requirements.
* Refined the project based on testing results.
* Ensured that the final repository contained the required source code, documentation, and profiling-related files.

### What AI Did

* Assisted with code review and documentation refinement.
* Helped identify areas where the implementation or instructions could be made clearer.
* Improved the organization and readability of the project documentation.
* Helped prepare the final contribution log and README structure.

---

## Summary of Human Contribution

My primary contributions to the project were:

* Defining the project requirements and objectives.
* Choosing the BFS vs A* comparison for the 8-Puzzle.
* Providing the initial project/code context.
* Deciding the required outputs and comparison metrics.
* Directing the development and documentation process.
* Testing the implementation locally.
* Reviewing and refining the generated code and documentation.
* Integrating the final components into the project.

## Summary of AI Contribution

AI was used as a development and documentation assistant. Its contributions included:

* Generating and modifying Python implementation code.
* Assisting with BFS and A* implementation.
* Implementing the Manhattan Distance heuristic.
* Creating helper functions for path reconstruction and board display.
* Preparing profiling and benchmarking scripts.
* Providing `py-spy` executi
