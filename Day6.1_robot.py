import random

# Define the game grid size
GRID_SIZE = 5
EMPTY = ' '  # Empty space
ROBOT = 'R'  # Robot's position
TARGET = 'T'  # Target's position
OBSTACLE = 'X'  # Obstacle

# Directions for robot movement
MOVES = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def generate_grid():
    # Create an empty grid
    grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Randomly place obstacles
    num_obstacles = GRID_SIZE * 2  # Number of obstacles
    for _ in range(num_obstacles):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        while grid[x][y] != EMPTY:  # Ensure no overlap
            x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[x][y] = OBSTACLE

    # Place robot and target
    while True:
        robot_x, robot_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if grid[robot_x][robot_y] == EMPTY:
            grid[robot_x][robot_y] = ROBOT
            break

    while True:
        target_x, target_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if grid[target_x][target_y] == EMPTY:
            grid[target_x][target_y] = TARGET
            break

    return grid, (robot_x, robot_y), (target_x, target_y)

def move_robot(grid, robot_pos, direction):
    x, y = robot_pos
    dx, dy = MOVES[direction]
    new_x, new_y = x + dx, y + dy

    # Check if the new position is within bounds and not an obstacle
    if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and grid[new_x][new_y] != OBSTACLE:
        # Move robot to the new position
        grid[x][y] = EMPTY
        grid[new_x][new_y] = ROBOT
        return (new_x, new_y)
    return robot_pos  # No movement if invalid

def main():
    # Generate the grid and initialize the robot and target positions
    grid, robot_pos, target_pos = generate_grid()

    print("Welcome to the Robot Puzzle Game!")
    print("Use 'w' for up, 's' for down, 'a' for left, 'd' for right.")
    print("Your goal is to move the robot to the target ('T').")
    
    while robot_pos != target_pos:
        print_grid(grid)
        print("Robot's position:", robot_pos)
        
        move = input("Enter your move (w/s/a/d): ").lower()

        if move in MOVES:
            robot_pos = move_robot(grid, robot_pos, move)
        else:
            print("Invalid move. Please use 'w', 's', 'a', or 'd'.")
    
    print_grid(grid)
    print("Congratulations! You've reached the target!")

if __name__ == "__main__":
    main()
