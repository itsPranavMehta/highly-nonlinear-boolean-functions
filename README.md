# highly-nonlinear-boolean-functions
constructing highly nonlinear boolean functions using genetic algorithm

The files published on this repository are as follow:
  - geneticAlgorithm.py
    - this file contains the python implementation for the genetic algorithm to construct highly nonlinear Boolean funtion
    - upon running, the results are stored in a file named- MyResults_x.txt where x denote the number of variables.
  - randomGeneration.py
    - this file contains code for randomly generating highly nonlinear Boolean function
    - this serves as a benchmark for our geneticAlgorithm.
  - Results_x.txt
    - these files contain the results obtained by the genetic algorithm code (geneticAlgorithm.py) for "x" variables. 
    - the results contain the following information
      - maximum possible nonlinearity
      - nonlinearity of the boolean function obtained 
      - nonlinearity in terms of percentage of the maximum possible nonlinearity
      - the boolean function obtained
