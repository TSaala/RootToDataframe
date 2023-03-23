# RootToDataframe
Code transforming root files into pandas dataframes

The actual code including an example run lies in RootToDF.py

An example root file lies in Data/Root called TTJets_0.root

Required packages:
    - uproot
    - numpy
    - pandas
    - pyarrow


To test, run RootToDF.py, the example root file should be transformed to a pandas dataframe called TTJets.feather,
located in Data/Pandas

Benchmarking results of using different filetypes for saving the dataframes can be found in the Images folder, 
additionally a visualization of the change in order when going from root file to dataframe can be found there.
