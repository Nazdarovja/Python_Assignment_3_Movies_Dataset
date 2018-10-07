import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np



# THIS IS A HOUDINI FIX 
def runtime_and_release(movies_df):
    release_date = pd.to_datetime(movies_df['release_date'], errors='')
    runtime = pd.to_numeric(movies_df['runtime'], errors='raise', downcast='unsigned')

    df = pd.DataFrame(release_date, runtime).reset_index()
    df = df[df['release_date'].notnull()]

    df.plot(x='release_date', y='runtime', style='.')
    plt.show()
