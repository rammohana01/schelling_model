# Schelling's Model of Segregation Simulation

Hello, this is a Python script for simulating Schelling's Model of Segregation. Schelling's Model is a type of agent-based model which demonstrates how individual tendencies regarding neighbors' types could lead to segregation. The script takes in a data grid of 'X', 'O', and ' ' characters, where 'X' and 'O' are two different types of agents and ' ' is an empty cell. The model then simulates the agents' movement based on their satisfaction level with their current neighbors.


## Code Overview

The script is structured around several key functions:

- `load_grid(file_path)`: This function reads in the data grid from a text file, where each character ('X', 'O', or ' ') represents an agent or an empty cell.

- `print_grid(grid)` and `print_subregion(grid, start_row, start_col, end_row, end_col)`: These functions print the entire grid or a specific subregion, respectively.

- `index_of_dissimilarity(grid)`: This function calculates the index of dissimilarity, which measures the degree of segregation in the grid.

- `is_satisfied(grid, row, col, similarity_threshold)`: This function checks whether an agent at a specific location is satisfied, based on the similarity threshold. If the proportion of similar neighboring agents is greater than or equal to the threshold, the agent is satisfied.

- `move_to_empty(grid, row, col)`: If an agent is not satisfied, this function randomly moves it to an empty cell in the grid.

- `simulate(grid, similarity_threshold)`: This function performs the simulation of Schelling's model. It iteratively checks for dissatisfied agents and moves them until there are no more dissatisfied agents or it reaches a maximum number of iterations.

The `main()` function coordinates these tasks, utilizing Python's `argparse` library to allow user input for customization of the simulation.


## Requirements

The script was written in Python and requires no additional libraries beyond what comes with a standard Python installation. Ensure that you have Python installed on your machine to run the script.

## How to run the script

1. Open your terminal (or command prompt on Windows).
2. Navigate to the directory containing the `schelling.py` script.
3. Run the script with the command: `py schelling.py [file_path] [start_row] [start_col] [end_row] [end_col] [similarity_threshold]`
   - `file_path`: Path to the data grid file.
   - `start_row`: Start row of the subregion.
   - `start_col`: Start column of the subregion.
   - `end_row`: End row of the subregion.
   - `end_col`: End column of the subregion.
   - `similarity_threshold`: Similarity threshold for agent satisfaction.

For example:
```text
py schelling.py data/schelling10.txt 6 0 9 3 0.4
```





## Sample Output

Below is a sample output when the script is run with the "schelling10.txt" file and the arguments 6 0 9 3 0.4:

```text
START: Loading data grid. ...
DONE: Loading data grid.

Grid Dimentions:
 > Row count: 10
 > Column count: 10

START: Printing data contents.
X X O O X O X O X O
X O O X O X O X O X
O X X   X O O X O X
O X X X O O X   X O
X O O X O X O X X O
X O X   X X O   O X
X X O O X O X O X O
X O   O X O O X O O
O X X X O O   O X O
O O O O O O O X O X
DONE: Printing data contents.

START: Computing Index of Dissimilarity.
Index of Dissimilarity = 0.17545454545454545
DONE: Computing Index of Dissimilarity.

START: Simulation of Schelling Segregation.
X X O O O O O O X X
X X X O O O O X X X
X X X X   O O X X X
X X X X O O O X X X
X X X X O O X X X O
X X X O X X X X O O
X X O O   X X O O O
X X   O O O O   O O
O O O   O O O O O O
O O O O O O O   O O
DONE: Simulation of Schelling Segregation.

Index of Dissimilarity:
Index of Dissimilarity = 0.4727272727272728
START: Printing final subregion.
X X O O
X X   O
O O O
O O O O
DONE: Printing final subregion.
```





The script outputs the original data grid, the dimensions of the grid, the index of dissimilarity before the simulation, the data grid after running the simulation, the index of dissimilarity after the simulation, and the final state of the specified subregion. The index of dissimilarity is a measure of the segregation in the grid, with higher values indicating higher segregation.




## References

- Luca Mingarelli. (2021, September). Schelling’s Model of Racial Segregation - Towards Data Science. Medium; Towards Data Science. [Link](https://towardsdatascience.com/schellings-model-of-racial-segregation-4852fad06c13)

- Game theory and racism: the Schelling Segregation Model – Mind Your Decisions. (2016, March 27). Mindyourdecisions.com. [Link](https://mindyourdecisions.com/blog/2008/10/28/game-theory-and-racism-the-schelling-segregation-model/)

- The Math of Segregation. (2017, February 6). American Scientist. [Link](https://www.americanscientist.org/article/the-math-of-segregation)

- The Schelling Model of Ethnic Residential Dynamics: Beyond the Integrated - Segregated Dichotomy of Patterns. (2012, January 31). Jasss.org; JASSS. [Link](https://www.jasss.org/15/1/6.html)

- Wikipedia Contributors. (2023, March 19). Schelling’s model of segregation. Wikipedia; Wikimedia Foundation. [Link](https://en.wikipedia.org/wiki/Schelling's_model_of_segregation)

- Social Networks. (2017). Spatial Segregation: Simulation of the Schelling Model [YouTube Video]. In YouTube. [Link](https://www.youtube.com/watch?v=FriCuzLKYE4)

- actuarialsci13. (2016). Schellings Segregation Model [YouTube Video]. In YouTube. [Link](https://www.youtube.com/watch?v=42STyM7RfrU&t=9s)

- Wayback Machine. (n.d.). Web.archive.org. Retrieved July 8, 2023, from [Link](https://web.archive.org/web/20101011030909/http://hsd.soc.cornell.edu:80/curricular/schelling_chapter_on_segregation.pdf)

- William, & Fossett, M. (2008). Understanding the social context of the Schelling segregation model. 105(11), 4109–4114. [Link](https://doi.org/10.1073/pnas.0708155105)

- RandomEconomist. (2009). The Logic of Life: Racial segregation [YouTube Video]. In YouTube. [Link](https://www.youtube.com/watch?v=JjfihtGefxk)

- Forest, B. (2005). Measures of Segregation and Isolation Index of Dissimilarity (D). [Link](https://www.dartmouth.edu/~segregation/IndicesofSegregation.pdf)

‌
