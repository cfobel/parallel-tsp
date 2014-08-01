# “Parallel” Travelling-Salesman Problem #

This project demonstrates a parallel approach to optimizing for the TSP by
iteratively performing concurrent swaps between city positions within a city
tour ordering/permutation.

## Requirements ##

To view the notebooks contained in this project, you must have the following
Python packages installed:

 - `ipython`
 - `matplotlib`
 - `numpy`
 - `pandas`

## Usage ##

From a terminal prompt within the root of this repository, run:

    ipython notebook

This should open a page in your web browser showing a list of `.ipynb`
_(IPython notebook)_ files.

 - `TSP.ipynb`: Describes an example _greedy_ algorithm for the TSP.
  - The proposed algorithm could easily be extended to be non-greedy, e.g.,
    simulated-annealing, etc.
 - `TSP-demo.ipynb`: Demonstrates that the proposed algorithm can reduce tour
   cost.
