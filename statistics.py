from glob import glob
import numpy as np
import pandas as pd


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