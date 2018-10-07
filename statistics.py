from glob import glob
import numpy as np
import pandas as pd
from Utility.date_time import str_2_datetime
import re


def num_of_adult_movies(movies_metadata):
    """
    Given a pandas DataFrame, return number of movies classified as adult.
    """
    return len(movies_metadata[movies_metadata["adult"] == "True"])


def num_of_animation_movies(movies_metadata):
    """
    Given a pandas DataFrame, return number of movies classified as animation.
    """
    return len(movies_metadata[movies_metadata["genres"].str.contains("Animation")])


def movie_with_highest_budget(movies_metadata):
    """
    Given a pandas DataFrame, return the movie with the highest budget.
    """
    # convert budget numbers from str to numerics, set invalids (strings) to NaN
    movies_metadata["budget"] = pd.to_numeric(movies_metadata["budget"], errors='coerce') 
    # sort list of movies by budget, descending, and return top 1 
    found_movie = movies_metadata.sort_values(by=["budget"], ascending=False).head(1)
    # strip title & budget and return as formatted tuple
    title = "".join(found_movie.title)
    budget = "".join(str(int(found_movie.budget)))
    return (title, budget)

def most_popular_danish_movie(movies_metadata):
    """
    Given a pandas DataFrame, return the most popular danish movie.
    """
    danish_movies = movies_metadata[movies_metadata['production_countries'].str.contains('Denmark', na=False)]
    danish_movies["popularity"] = pd.to_numeric(danish_movies["popularity"], errors='coerce')
    movie = danish_movies.sort_values(by=["popularity"], ascending=False).head(1)
    title = "".join(movie.title)
    popularity = "".join(str(float(movie.popularity)))
    return (title, popularity)

def english_movie_with_most_revenue(movies_metadata):
    """
    Given a pandas DataFrame, return the english action movie with most revenue.
    """
    english_movies = movies_metadata[movies_metadata['production_countries'].str.contains('United Kingdom', na=False) & movies_metadata["genres"].str.contains("Action")]
    movie = english_movies.sort_values(by=["revenue"], ascending=False).head(1)
    title = "".join(movie.title)
    revenue = "".join(str(int(movie.revenue)))
    return (title, revenue)

def most_used_words(df, col_with_strings, max=100):
    '''
        Returns a pandas.Series with keys = words, and values = frequency
        Args:
            pandas.DataFrame: df - data
            str: col_with_strings - name of the column in df where the strings to analyze are stored
            int: max (default=100) - specifies the max amount of words to be returned in pandas.Series
        Returns:
            pandas.Series: most used words
    '''

    # laver alle ord om til lowercase
    df[col_with_strings] = df[col_with_strings].str.lower()

    #   1. df['overview'].astype(str) --> returnere en pandas.Serie, hvor alle sætninger typecastes til Strings
    #   2. ''.join( <punkt 1.> ).split() --> laver én liste med alle ord
    #   3. pd.Series( <punkt 2.> ) --> lave punkt 1. om til et pandas.Series objekt
    #   4. pandas.Series.value_counts() --> returnere pandas.Series som indeholder optælling af unikke værdier
    #   5. pandas.Series.head(100) --> only keep the first 100 values
    popu_words = pd.Series(''.join(df[col_with_strings].astype(str)).split()).value_counts().head(max)

    # denne regex sammensætning generere et regex der sørger for, at ord som 'i' eller 'is'
    # ikke bliver matches op imod f.eks. 'his', men kun et nøjagtigt match bliver talt.
    regex = re.compile(r'\b(?:%s)\b' % '|'.join(popu_words.keys().tolist()))

    # tæller antallet af buzzwords i sætninger. ét buzzword kan godt bliver talt mere end én 
    # gang, hvis ordet oprtæder mere end én gang
    # - pandas.Series.fillna(0).astype(int) --> cleaning data before plotting
    return df['overview'].str.count(regex).fillna(0).astype(int)

def num_of_movies(df, per_criteria='ym'):
    '''
        Returns the state with biggest increase in death in specified interval
        Args:
            pandas.DataFrame: df - data
            str: per_criteria - 'y' (year) or 'ym' (year month) for specifying wether to count movies pr. year or pr. month pr. year
        Returns:
            pandas.Series: movies pr. specified criteria
    '''

    df = df[df['release_date'].str.len() == 10]

    # Lav str om til datetime, for alle release dage
    # df['release_date'] = df['release_date'].apply(str_2_datetime)
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    # df['Week/Year'] = df['release_date'].apply(lambda x: "%d/%d" % (x.week, x.year))

    # antal film releases pr. år
    if per_criteria == 'y':
        ps = df['release_date'].groupby([df['release_date'].dt.year.rename('year')]).count()

    # antal film releases pr. år og måned
    if per_criteria == 'ym':
        ps = df['release_date'].groupby([df['release_date'].dt.year.rename('year'), df['release_date'].dt.month.rename('month')]).count()

    return ps