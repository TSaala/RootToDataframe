# RootToDataFrame

Code transforming root files into pandas dataframes.
The code, including an example run lies within RootToDF.py
An example root file containing 100 events lies in Data/Root.



## Required Packages

- uproot
- numpy
- pandas
- pyarrow

## Running the code

To test the code, simply run RootToDF.py. The example root file should be transformed to a pandas dataframe called TTJets.feather, located in Data/Pandas.


## Benchmarking

Benchmarking results of using different filetypes for saving the dataframes can be found in the Images folder. Additionally, a visualization of the change in order when going from root file to dataframe can be found there.
