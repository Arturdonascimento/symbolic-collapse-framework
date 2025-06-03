
import random
import math

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_neighbors(entity, board, size):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = entity.x + dx, entity.y + dy
        if 0 <= nx < size and 0 <= ny < size:
            for e in board:
                if e.x == nx and e.y == ny:
                    neighbors.append(e)
    return neighbors

def get_possible_moves(entity, size):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    moves = []
    for dx, dy in directions:
        nx, ny = entity.x + dx, entity.y + dy
        if 0 <= nx < size and 0 <= ny < size:
            moves.append((nx, ny))
    return moves

def compute_transition(entity, neighbors):
    return random.uniform(0, 1)

def compute_curvature(entity, board, size):
    cx, cy = size / 2, size / 2
    dist = math.sqrt((entity.x - cx)**2 + (entity.y - cy)**2)
    return dist / size

def collapse_entity(entity, board):
    board.remove(entity)

def move_entity(entity, Delta, board, size):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = entity.x + dx, entity.y + dy
        if 0 <= nx < size and 0 <= ny < size:
            if not any(e.x == nx and e.y == ny for e in board):
                entity.x = nx
                entity.y = ny
                break

def simulate_board(size=10, iterations=10, collapse_threshold=0.15, gamma_critical=1.0):
    board = [Entity(random.randint(0, size-1), random.randint(0, size-1)) for _ in range(size)]
    collapse_count = 0
    tau_gradients = []

    for _ in range(iterations):
        for entity in board[:]:
            neighbors = get_neighbors(entity, board, size)
            total_moves = len(get_possible_moves(entity, size))
            blocked = sum(1 for move in get_possible_moves(entity, size) if any(e.x == move[0] and e.y == move[1] for e in board))
            F_j = 1 - (blocked / total_moves) if total_moves > 0 else 0
            Delta = compute_transition(entity, neighbors)
            nabla_tau = compute_curvature(entity, board, size)
            tau_gradients.append(nabla_tau)

            if F_j < collapse_threshold or abs(nabla_tau) > gamma_critical:
                collapse_entity(entity, board)
                collapse_count += 1
            else:
                move_entity(entity, Delta, board, size)

    collapse_frequency = collapse_count / (iterations * size)
    return collapse_frequency, sum(tau_gradients)/len(tau_gradients), collapse_count

if __name__ == "__main__":
    freq, avg_tau, total_collapse = simulate_board()
    print(f"Collapse Frequency: {freq:.2f}")
    print(f"Average ∇τ: {avg_tau:.4f}")
    print(f"Total Collapsed Entities: {total_collapse}")
