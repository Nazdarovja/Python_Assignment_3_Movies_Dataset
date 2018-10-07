import matplotlib.pyplot as plt 
import pandas as pd
import datetime

#  2005-09-13
def count_on_release_date(movies_df):
    ## get movie count for release dates format="%Y-%m-%d"
    a = pd.to_datetime(movies_df['release_date'], yearfirst=True , errors='coerce')
    pass
    
def runtime_and_release(movies_df):
    release_date = pd.to_datetime(movies_df['release_date'], yearfirst=True , errors='coerce')

    runtime = pd.to_numeric(movies_df['runtime'], errors='raise', downcast='unsigned')  ### not needed....
    

    # print(release_date, type(release_date), len(release_date))
    # print(runtime, type(runtime), len(runtime))
    
    # to_plot_df = release_date.combine(runtime)
    
    # print(to_plot_df)
    plt.(release_date, runtime)
    plt.show()