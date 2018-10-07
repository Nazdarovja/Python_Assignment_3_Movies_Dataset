import matplotlib.pyplot as plt 
import pandas as pd
import datetime
import numpy as np
import statistics
from mpl_toolkits import mplot3d

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


    # print(release_date, type(release_date), len(release_date))
    # print(runtime, type(runtime), len(runtime))
    
    # to_plot_df = release_date.combine(runtime)
    
    # print(to_plot_df)
    # plt.(release_date, runtime)
    plt.show()

def plot_3d_scatter(plt, df, x_col, y_col, z_col):
    '''
        Adding a 3D scattor plot to plt. Remember to call matplotlib.pyplot.plot() after this function to show plot.
        Args:
            matplotlib.pyplot: plt - 
            pandas.DataFrame: df - data
            str: x_col -
            str: y_col -
            str: z_col -
    '''
    # Data for a three-dimensional line
    z = df[x_col]
    x = df[y_col] 
    y = df[z_col] 
    
    # Building 3D graf
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)
    ax.scatter3D(x, y, z, c=z, cmap='Greens')

def plot_hist(plt, ps):
    '''
        Adding a bar chart plot (which behaves and shows same as histogram 'frequency') to plt. Remember to call matplotlib.pyplot.plot() after this function to show plot.
        Args:
            matplotlib.pyplot: plt - 
            pandas.Series: ps - data
    '''
    ps.plot(kind='bar')
    plt.xticks(np.arange(1, len(ps.index)+1, len(ps.index) / 15))


def plot_assignment(df):
    
    '''
        Første plot
    '''
    ps = statistics.num_of_movies(df, 'y')

    # create plot
    plot_hist(plt, ps)

    '''
        Andet Plot
    '''


    '''
        Tredje Plot
    '''
    # creating needed data for plot
    df['buzzword_count'] = statistics.most_used_words(df,'overview')
    
    # cleaning up rest of needed data for plotting
    df['budget'] = pd.to_numeric(df['budget'], downcast='float', errors='coerce').fillna(0)
    df['revenue'] = pd.to_numeric(df['revenue'], downcast='float', errors='coerce').fillna(0)

    # create plot
    plot_3d_scatter(plt, df, 'budget', 'buzzword_count', 'revenue')



    # show all plots
    plt.show()



