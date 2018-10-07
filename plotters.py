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
    

    df = pd.DataFrame(release_date,runtime)
    # print(df['release_date'][:1],type(df['release_date'][:1]))

    # df.plot.scatter(x='release_date',y='runtime')