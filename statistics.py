from glob import glob
import numpy as np

# """ glob for .csv files in directory and store name of first occurrence as csv_filename."""
# csv_filename = glob("./*.csv")[0]


def num_of_adult_movies(movies_metadata):
    """
    Given a pandas DataFrame, return number of movies classified as adult.
    """
    return len(movies_metadata[movies_metadata["adult"] == "True"])