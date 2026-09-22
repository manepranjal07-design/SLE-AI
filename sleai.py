"""
SLE-2 Profiling: BFS vs A* on the 8-Puzzle
--------------------------------------------
The 8-puzzle: a 3x3 grid with tiles 1-8 and one blank (0).
Slide tiles into the blank space to reach the goal arrangement.

Algorithm A: BFS (uninformed search)
Algorithm B: A* (informed search, using Manhattan distance heuristic)

Run this file directly: python sle2_8puzzle_profiling.py
Copy the printed numbers into your Word report's comparison table.
"""

import heapq
import time
from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 = blank tile

# A solvable starting puzzle, scrambled several moves away from goal
# so BFS and A* show a meaningful difference (kept small enough that
# BFS still finishes quickly for a classroom demo)
START = (1, 2, 3, 5, 0, 6, 4, 7, 8)


def get_neighbors(state):
    """Return all states reachable by sliding one tile into the blank."""
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = []
    if row > 0: moves.append(-3)   # move blank up
    if row < 2: moves.append(3)    # move blank down
    if col > 0: moves.append(-1)   # move blank left
    if col < 2: moves.append(1)    # move blank right

    for move in moves:
        new_blank = blank + move
        new_state = list(state)
        new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
        neighbors.append(tuple(new_state))

    return neighbors


def manhattan_distance(state):
    """Heuristic for A*: sum of how far each tile is from its goal position."""
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = GOAL.index(tile)
        row1, col1 = divmod(i, 3)
        row2, col2 = divmod(goal_index, 3)
        distance += abs(row1 - row2) + abs(col1 - col2)
    return distance


# -------------------------------------------------------------
# ALGORITHM A: BFS (uninformed search)
# -------------------------------------------------------------
def bfs(start, goal):
    nodes_expanded = 0
    frontier = deque([start])
    visited = {start}
    parent = {start: None}

    while frontier:
        state = frontier.popleft()
        nodes_expanded += 1

        if state == goal:
            return reconstruct_path(parent, state), nodes_expanded

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = state
                frontier.append(neighbor)

    return None, nodes_expanded


# -------------------------------------------------------------
# ALGORITHM B: A* (informed search, Manhattan distance heuristic)
# -------------------------------------------------------------
def a_star(start, goal):
    nodes_expanded = 0
    counter = 0
    frontier = [(manhattan_distance(start), counter, start, 0)]
    best_g = {start: 0}
    parent = {start: None}

    while frontier:
        f, _, state, g = heapq.heappop(frontier)
        nodes_expanded += 1

        if state == goal:
            return reconstruct_path(parent, state), nodes_expanded

        for neighbor in get_neighbors(state):
            new_g = g + 1
            if neighbor not in best_g or new_g < best_g[neighbor]:
                best_g[neighbor] = new_g
                parent[neighbor] = state
                counter += 1
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(frontier, (new_f, counter, neighbor, new_g))

    return None, nodes_expanded


def reconstruct_path(parent, state):
    path = [state]
    while parent[state] is not None:
        state = parent[state]
        path.append(state)
    return list(reversed(path))


# -------------------------------------------------------------
# PROFILING HELPER
# -------------------------------------------------------------
def profile(func, start, goal, runs=5):
    times = []
    nodes_expanded = 0
    path = None

    for _ in range(runs):
        t0 = time.perf_counter()
        path, nodes_expanded = func(start, goal)
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1000)

    avg_time_ms = sum(times) / len(times)
    return {
        "path_length": len(path) if path else None,
        "avg_time_ms": round(avg_time_ms, 4),
        "nodes_expanded": nodes_expanded,
        "all_times_ms": [round(t, 4) for t in times],
    }


if __name__ == "__main__":
    RUNS = 5

    bfs_result = profile(bfs, START, GOAL, runs=RUNS)
    astar_result = profile(a_star, START, GOAL, runs=RUNS)

    print("=" * 60)
    print("SLE-2 PROFILING RESULTS: BFS vs A* on the 8-Puzzle")
    print("=" * 60)

    print("\n--- Algorithm A: BFS ---")
    print(f"Solution length  : {bfs_result['path_length']} moves")
    print(f"Individual times : {bfs_result['all_times_ms']} ms")
    print(f"Avg. Time (ms)   : {bfs_result['avg_time_ms']}")
    print(f"Nodes Expanded   : {bfs_result['nodes_expanded']}")

    print("\n--- Algorithm B: A* (Manhattan distance heuristic) ---")
    print(f"Solution length  : {astar_result['path_length']} moves")
    print(f"Individual times : {astar_result['all_times_ms']} ms")
    print(f"Avg. Time (ms)   : {astar_result['avg_time_ms']}")
    print(f"Nodes Expanded   : {astar_result['nodes_expanded']}")

    print("\n" + "=" * 60)
    print("COMPARISON TABLE (for your Word doc, Section 3)")
    print("=" * 60)
    print(f"{'Metric':<20}{'BFS':<15}{'A*':<15}{'Better?'}")
    print(f"{'Avg. Time (ms)':<20}{bfs_result['avg_time_ms']:<15}{astar_result['avg_time_ms']:<15}"
          f"{'A*' if astar_result['avg_time_ms'] < bfs_result['avg_time_ms'] else 'BFS'}")
    print(f"{'Nodes Expanded':<20}{bfs_result['nodes_expanded']:<15}{astar_result['nodes_expanded']:<15}"
          f"{'A*' if astar_result['nodes_expanded'] < bfs_result['nodes_expanded'] else 'BFS'}")