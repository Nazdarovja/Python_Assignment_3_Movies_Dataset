import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np


# THIS IS A HOUDINI FIX
def runtime_and_release(movies_df):
    movies_df = movies_df[movies_df['release_date'].str.len() == 10]

    release_date = pd.to_datetime(movies_df['release_date'], errors='coerce')
    runtime = pd.to_numeric(movies_df['runtime'], errors='raise', downcast='unsigned')

    df = pd.DataFrame(release_date, runtime).reset_index()

    df.plot(x='release_date', y='runtime', style='.')
    plt.show()
