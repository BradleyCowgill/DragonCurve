# This program recursively generates and displays the user defined nth iteration (iteration_num) dragon curve fractal.
# The algorithm is intended to be constructive on previous iterations, they are certainly faster ways of achieving a
# similar final result. Note the user input value can result in large processing times for iteration_num greater
# than 18 on some computers due to the exponential nature of the fractal.
#
# Written by Bradley J. Cowgill 02/21/2023

import copy
import numpy as np
import matplotlib.pyplot as plt

# Ask the user to input the iteration number
print("Note: Values greater than 18 may take significant time to compute.")
print("Please pick an iteration number:")
iteration_num = input("")

# Validate the user input
while not iteration_num.isdigit():
    print("Invalid input. Please input an integer for the iteration number:")
    iteration_num = input("")
iteration_num = int(iteration_num)

# Calculate the number of folds based on the user input iteration number
fold_num = 2 ** iteration_num - 1

# Create lists that contain boolean (and string equivalents) values for each paper fold
paper_folds = np.zeros(fold_num, dtype=bool)
string_paper_folds = [''] * fold_num

# Performs paper folding algorithm, assumes folding left side clockwise over right side of paper
for current_iteration in range(iteration_num):
    subsection = paper_folds[int(len(paper_folds) / 2) - (int(2 ** current_iteration) - 1):
                             int(len(paper_folds) / 2) + (int(2 ** current_iteration))]
    for idx, item in enumerate(subsection):
        if idx % 4 == 0:
            subsection[idx] = 1
        elif idx % 4 == 2:
            subsection[idx] = 0

    if current_iteration + 1 < iteration_num:
        section = paper_folds[int(len(paper_folds) / 2) - (int(2 ** current_iteration) - 1):
                              int(len(paper_folds) / 2) + (int(2 ** current_iteration))]
        # Deep copy required to in order to not change paper_folds list
        subsection = copy.deepcopy(subsection)
        for idx, item in enumerate(subsection):
            paper_folds[(int(len(paper_folds) / 2) - (int(2 ** (current_iteration + 1)) - 1)) + idx * 2 + 1] \
                = subsection[idx]

# Flip and invert to match traditional dragon curve pattern
paper_folds = np.flip(paper_folds)
for idx, fold in enumerate(paper_folds):
    paper_folds[idx] = not fold

# Initialize coordinate lists for plotting, setting first coordinate to (0,1) for unfolded paper (zero folds edge case)
x_paper_folds = np.zeros((len(paper_folds) + 2), dtype=int)
y_paper_folds = np.zeros((len(paper_folds) + 2), dtype=int)
y_paper_folds[1] = 1

# Populate coordinate lists for plotting based on fold pattern
for idx, item in enumerate(paper_folds):
    if all(x_paper_folds[idx + 1] - x_paper_folds[idx] == [1]):
        if paper_folds[idx] == 0:
            x_paper_folds[idx + 2] = x_paper_folds[idx + 1]
            y_paper_folds[idx + 2] = y_paper_folds[idx + 1] + 1
        elif paper_folds[idx] == 1:
            x_paper_folds[idx + 2] = x_paper_folds[idx + 1]
            y_paper_folds[idx + 2] = y_paper_folds[idx + 1] - 1
    elif all(x_paper_folds[idx + 1] - x_paper_folds[idx] == [-1]):
        if paper_folds[idx] == 0:
            x_paper_folds[idx + 2] = x_paper_folds[idx + 1]
            y_paper_folds[idx + 2] = y_paper_folds[idx + 1] - 1
        elif paper_folds[idx] == 1:
            x_paper_folds[idx + 2] = x_paper_folds[idx + 1]
            y_paper_folds[idx + 2] = y_paper_folds[idx + 1] + 1
    elif all(y_paper_folds[idx + 1] - y_paper_folds[idx] == [1]):
        if paper_folds[idx] == 0:
            x_paper_folds[idx + 2] = x_paper_folds[idx + 1] - 1
            y_paper_folds[idx + 2] = y_paper_folds[idx + 1]
        elif paper_folds[idx] == 1:
            x_paper_folds[idx + 2] = x_paper_folds[idx + 1] + 1
            y_paper_folds[idx + 2] = y_paper_folds[idx + 1]
    elif all(y_paper_folds[idx + 1] - y_paper_folds[idx] == [-1]):
        if paper_folds[idx] == 0:
            x_paper_folds[idx + 2] = x_paper_folds[idx + 1] + 1
            y_paper_folds[idx + 2] = y_paper_folds[idx + 1]
        elif paper_folds[idx] == 1:
            x_paper_folds[idx + 2] = x_paper_folds[idx + 1] - 1
            y_paper_folds[idx + 2] = y_paper_folds[idx + 1]

# Fill fold string list with Peaks and Valleys from binary data, display in terminal
for idx, fold in enumerate(paper_folds):
    if fold == 0:
        string_paper_folds[idx] = "Valley"
    elif fold == 1:
        string_paper_folds[idx] = "Peak"
print(string_paper_folds)

# Plot data for user to see
plt.figure("Dragon Curve")
plt.plot(x_paper_folds, y_paper_folds, '-')
plt.axis('off')
plt.axis('equal')
plt.title(f'Dragon Curve for iteration n = {iteration_num}')
plt.show()


# Hold for user input before terminating
hold = input("Press Enter to continue...")
