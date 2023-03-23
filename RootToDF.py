import uproot
import pandas as pd
import numpy as np


def transform_root_to_dataframe(path, folder, fileName):
    # Function transforming a given .root file to a pandas dataframe
    # Important:    Root trees here are saved variable wise, e.g. #variable vectors of length #events
    #               Dataframes instead are saved event wise, e.g. #event vectors of length #variables

    # Parameters:
    #   path (str):     A string defining the path where the initial .root file is located
    #   folder (str):   A string defining the path where the final dataframe is to be saved
    #   fileName (str): A string defining the name the final dataframe is supposed to be saved as (without file ending)

    print("Begin transforming " + fileName)

    # Get the first fEventTree in the .root File
    with(uproot.open(path)) as tmp:
        firstTree = tmp.keys()[[idx for idx, s in enumerate(tmp.keys()) if 'fEventTree' in s][0]]

    # Open the first fEventTree, iterate over it
    with uproot.open(path + ":" + firstTree) as events:

        values = []
        for x in events.keys():
                values.append(events[x].array(library="np"))

        # Get Keys in order to use them as columns for the dataframe
        keys = events.keys()
        keys = np.asarray(keys)
        # print(keys)

        final = np.stack(values, axis=1)

        # Convert np array (final) to the desired dataframe
        final_df = pd.DataFrame(final, columns=keys)

        # Save dataframe as feather file, this can be exchanged as wanted
        # e.g. final_df.to_pickle(folder + "/" + fileName + ".pkl") would save the dataframe as a pickle file
        final_df.to_feather(folder + "/" + fileName + ".feather")

        print("Finished transforming " + fileName)


# Example run for the above Method
path = './Data/Root/TTJets_0.root'
folder = './Data/Pandas'
fileName = 'TTJets'

transform_root_to_dataframe(path=path, folder=folder, fileName=fileName)