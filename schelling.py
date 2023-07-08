import argparse
import random

def load_grid(file_path):
    """
    Load grid from file.

    Parameter:
        file_path: path to the file
    Return:
        grid as a list of lists
    """
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f]
    return grid

def print_grid(grid):
    """
    Print grid.

    Parameter:
        grid: grid to print
    """
    for row in grid:
        print(' '.join(row))
    print()

def get_grid_dimensions(grid):
    """
    Get dimensions of the grid.

    Parameter:
        grid: grid to examine

    Return:
        tuple of (row_count, column_count)
    """
    row_count = len(grid)
    column_count = len(grid[0]) if grid else 0
    return row_count, column_count

def print_subregion(grid, start_row, start_col, end_row, end_col):
    """
    Print subregion of the grid.

    Parameters:
        - grid: grid to print from
        - start_row: starting row of subregion
        - start_col: starting column of subregion
        - end_row: ending row of subregion
        - end_col: ending column of subregion
    """

    subregion = grid[start_row:end_row+1]
    subregion = [row[start_col:end_col+1] for row in subregion]
    print_grid(subregion)

def index_of_dissimilarity(grid):

    """
    Reference: Forest, B. (2005). Measures of Segregation and Isolation Index of Dissimilarity (D).
    https://www.dartmouth.edu/~segregation/IndicesofSegregation.pdf

    
    Parameters:
        grid (list of list): The grid represented as a 2D list. 'X', 'O', and ' ' represent different entities.

    Returns:
        float: The calculated index of dissimilarity.

    """
    total_X = sum(row.count('X') for row in grid)
    total_O = sum(row.count('O') for row in grid)

    dissimilarity_index = 0
    for row in grid:
        w_i = row.count('X')  # population of X in specific row
        b_i = row.count('O')  # population of O in specific row

        if total_X > 0:
            x_prop = w_i / total_X
        else:
            x_prop = 0

        if total_O > 0:
            o_prop = b_i / total_O
        else:
            o_prop = 0

        dissimilarity_index += abs(x_prop - o_prop)

    dissimilarity_index *= 0.5  # multiplied by 1/2 as per formula
    return dissimilarity_index


def is_satisfied(grid, row, col, similarity_threshold):

    """
    Determine whether the agent at a specific position in the grid is satisfied with its neighborhood.

    An agent is satisfied if the ratio of similar agents to the total agents in its neighborhood is equal 
    or greater than the similarity_threshold. Empty cells are not considered in the calculation.

    Parameters:
        grid (list of list): The grid represented as a 2D list. 'X', 'O', and ' ' represent different entities.
        row (int): The row index of the agent.
        col (int): The column index of the agent.
        similarity_threshold (float): The minimum ratio of similar agents to total agents for satisfaction.

    Returns:
        bool: True if the agent is satisfied, otherwise False.
    """

    agent = grid[row][col]
    if agent == ' ':
        return True

    count_similar = 0
    count_different = 0

    for i in range(max(0, row - 1), min(len(grid), row + 2)):
        for j in range(max(0, col - 1), min(len(grid[0]), col + 2)):
            if i == row and j == col:
                continue

            neighbor = grid[i][j]
            if neighbor == ' ':
                continue

            if neighbor == agent:
                count_similar += 1
            else:
                count_different += 1

    if count_similar + count_different == 0:
        return True

    return count_similar / (count_similar + count_different) >= similarity_threshold

def move_to_empty(grid, row, col):
    """
    Move the agent at a specific position to a random empty cell in the grid.

    If no empty cells are available, the agent does not move.

    Parameters:
        grid (list of list): The grid represented as a 2D list. 'X', 'O', and ' ' represent different entities.
        row (int): The row index of the agent.
        col (int): The column index of the agent.

    Returns:
        bool: True if the agent has moved, False otherwise.
    """


    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == ' ']
    if not empty_cells:
        return False

    new_row, new_col = random.choice(empty_cells)
    grid[new_row][new_col] = grid[row][col]
    grid[row][col] = ' '

    return True

def simulate(grid, similarity_threshold):
    """
    Perform a simulation of the grid, where unsatisfied agents are moved to an empty cell.

    The simulation is run for as many iterations as there are cells in the grid.

    Parameters:
        grid (list of list): The grid represented as a 2D list. 'X', 'O', and ' ' represent different entities.
        similarity_threshold (float): The minimum ratio of similar agents to total agents for satisfaction.
    """

    for _ in range(len(grid) * len(grid[0])):
        dissatisfied_agents = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if not is_satisfied(grid, i, j, similarity_threshold)]
        if not dissatisfied_agents:
            break

        for row, col in dissatisfied_agents:
            move_to_empty(grid, row, col)

def main():
    """
    Load a grid from a file, perform a simulation, and display the results.

    This is the main function that uses all the other functions together. It takes command line arguments 
    for the grid file path, subregion coordinates, and similarity threshold. It then runs a Schelling 
    segregation simulation, prints the grid and a subregion before and after the simulation, and computes 
    the index of dissimilarity.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the data grid file.")
    parser.add_argument("start_row", type=int, help="Start row of the subregion.")
    parser.add_argument("start_col", type=int, help="Start column of the subregion.")
    parser.add_argument("end_row", type=int, help="End row of the subregion.")
    parser.add_argument("end_col", type=int, help="End column of the subregion.")
    parser.add_argument("similarity_threshold", type=float, help="Similarity threshold for agent satisfaction.")
    args = parser.parse_args()

    print("START: Loading data grid. ...")
    grid = load_grid(args.file_path)
    print("DONE: Loading data grid.\n")

    print("Grid Dimentions:")
    row_count, column_count = get_grid_dimensions(grid)
    print(f" > Row count: {row_count}")
    print(f" > Column count: {column_count}\n")

    print("START: Printing data contents.")
    print_grid(grid)
    print("DONE: Printing data contents.\n")

    print("START: Computing Index of Dissimilarity.")
    print(f"Index of Dissimilarity = {index_of_dissimilarity(grid)}")
    print("DONE: Computing Index of Dissimilarity.\n")

    print("START: Simulation of Schelling Segregation.")
    simulate(grid, args.similarity_threshold)
    print_grid(grid)
    print("DONE: Simulation of Schelling Segregation.\n")


    print("Index of Dissimilarity:")
    print(f"Index of Dissimilarity = {index_of_dissimilarity(grid)}")

    print("START: Printing final subregion.")
    print_subregion(grid, args.start_row, args.start_col, args.end_row, args.end_col)
    print("DONE: Printing final subregion.\n")

if __name__ == "__main__":
    main()