import matplotlib as plt
import matplotlib
import pandas as pd
import datetime

#  2005-09-13


def count_on_release_date(movies_df):
    # get movie count for release dates format="%Y-%m-%d"
    a = pd.to_datetime(
        movies_df['release_date'], yearfirst=True, errors='coerce', format="%Y-%m-%d")
    pass


def runtime_and_release(movies_df):
    release_date = pd.to_datetime(
        movies_df['release_date'], yearfirst=True, errors='coerce')

    # not needed....
    runtime = pd.to_numeric(
        movies_df['runtime'], errors='raise', downcast='unsigned')

    df = pd.DataFrame(release_date, runtime).reset_index()

    # print(type(df['release_date'][1]))
    # df.plot.scatter(x='release_date',y='runtime')

    # plt.scatter(x="release_date", y="runtime", data=df)
    # plt.show()
    scatter_date(df, 'release_date', 'runtime', '%Y-%m-%d')


def scatter_date(df, x, y, datetimeformat):
    if not isinstance(y, list):
        y = [y]
    for yi in y:
          plt.plot_date(df[x].apply(
              lambda z: matplotlib.dates.date2num(
                  datetime.datetime.strptime(z, datetimeformat))), df[yi], label=yi)
    plt.legend()
    plt.xlabel(x)
