from collections import deque
from heapq import heappop, heappush

# ------------------------------------------------------------------------------
# 1. CORE PUZZLE SETUP & HELPERS
# ------------------------------------------------------------------------------

# Goal state: 1 to 8 in row-major order, with 0 representing the blank space
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Pre-calculated grid coordinates (row, col) for goal positions to speed up heuristic
GOAL_POSITIONS = {val: (i // 3, i % 3) for i, val in enumerate(GOAL_STATE)}

def get_neighbors(state):
    """Generates valid next states by sliding a tile into the blank (0) space."""
    idx = state.index(0)
    r, c = idx // 3, idx % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            state_list = list(state)
            state_list[idx], state_list[n_idx] = state_list[n_idx], state_list[idx]
            neighbors.append(tuple(state_list))

    return neighbors

def manhattan_distance(state):
    """Heuristic function for A*: sum of Manhattan distances of tiles from goal positions."""
    dist = 0
    for idx, val in enumerate(state):
        if val != 0:
            r, c = idx // 3, idx % 3
            gr, gc = GOAL_POSITIONS[val]
            dist += abs(r - gr) + abs(c - gc)
    return dist

def reconstruct_path(parent_map, start_state, goal_state):
    """Traces back through the parent map to rebuild the full solution sequence."""
    path = []
    curr = goal_state
    while curr != start_state:
        path.append(curr)
        curr = parent_map[curr]
    path.append(start_state)
    path.reverse()
    return path

# ------------------------------------------------------------------------------
# 2. BREADTH-FIRST SEARCH (BFS)
# ------------------------------------------------------------------------------

def bfs(start_state):
    """
    Solves 8-Puzzle using BFS.
    Guarantees optimal (shortest) path, but expands a large number of nodes.
    """
    queue = deque([start_state])
    visited = {start_state}
    parent = {}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == GOAL_STATE:
            path = reconstruct_path(parent, start_state, GOAL_STATE)
            return path, nodes_expanded

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None, nodes_expanded  # Unsolvable

# ------------------------------------------------------------------------------
# 3. A* SEARCH (A_STAR)
# ------------------------------------------------------------------------------

def a_star(start_state):
    """
    Solves 8-Puzzle using A* Search with Manhattan Distance.
    Uses f(n) = g(n) + h(n) to prioritize paths.
    """
    # Unique sequence counter to break priority queue ties safely
    counter = 0

    # Heap elements: (f_score, tie_breaker, current_state)
    heap = [(manhattan_distance(start_state), counter, start_state)]
    
    # Store lowest g_score found so far for each state
    g_score = {start_state: 0}
    parent = {}
    nodes_expanded = 0

    while heap:
        _, _, current = heappop(heap)
        nodes_expanded += 1

        if current == GOAL_STATE:
            path = reconstruct_path(parent, start_state, GOAL_STATE)
            return path, nodes_expanded

        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor)
                parent[neighbor] = current
                
                counter += 1
                heappush(heap, (f_score, counter, neighbor))

    return None, nodes_expanded  # Unsolvable

# ------------------------------------------------------------------------------
# 4. FORMATTING & EXECUTION DEMO
# ------------------------------------------------------------------------------

def print_board(state):
    """Prints a 9-tuple as a 3x3 grid."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else " " for x in state[i:i+3]]
        print(" | ".join(row))
    print("-" * 9)

if __name__ == "__main__":
    # Example state (Requires 8 moves to reach goal)
    start = (1, 2, 3, 
             0, 4, 6, 
             7, 5, 8)

    print("Initial State:")
    print_board(start)

    # --- Run BFS ---
    bfs_path, bfs_nodes = bfs(start)
    print(f"BFS Solution Length: {len(bfs_path) - 1} moves")
    print(f"BFS Nodes Expanded:  {bfs_nodes}")

    # --- Run A* ---
    a_star_path, a_star_nodes = a_star(start)
    print(f"A* Solution Length:  {len(a_star_path) - 1} moves")
    print(f"A* Nodes Expanded:   {a_star_nodes}")

    # --- Display Step-by-Step Solution ---
    print("\nStep-by-step solution path (A*):")
    for step_num, state in enumerate(a_star_path):
        print(f"Step {step_num}:")
        print_board(state)