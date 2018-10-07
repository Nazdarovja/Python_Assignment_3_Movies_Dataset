import pandas as pd
import numpy as np
import plotters

movies_df = pd.read_csv("movies_metadata.csv", low_memory=False, encoding='utf-8')


def adult_movies_count(movies_df):
    return len(movies_df[movies_df["adult"] == True])

def animation_movies_count(movies_df):
    return len(movies_df[movies_df['genres'].str.contains('Animation')])

def largest_budget_movie(movies_df):
    ## make the budgets numerical and to integers (default is apparently float...) then find the highest value row index number(idxmax()) then get the row from df (iloc())
    movie = movies_df.iloc[pd.to_numeric(movies_df['budget'], errors='coerce', downcast='integer').idxmax()] ## jesus.. what have i done...
    
    ##return only title, and budget thank you python for multiple return 
    return (movie.title, movie.budget)

def most_popular_dk_movie(movies_df):
    # Only god can judge me now....
    movie = movies_df.iloc[pd.to_numeric(movies_df[movies_df['production_countries'].str.contains('Denmark', na=False)]['popularity'], errors='coerce').idxmax()]
   
    return (movie.title, movie.popularity)


def biggest_revenue_english_action_movie(movies_df):
    # Now im just messing with the people reviewing :D sry
    movie = movies_df.iloc[pd.to_numeric(movies_df[movies_df['production_countries'].str.contains('United Kingdom', na=False) & movies_df['genres'].str.contains('Action', na=False)]['revenue'], errors='coerce').idxmax()]
    
    return (movie.title, movie.revenue)

if __name__ == '__main__':

    # 1) How many movie are rated adult? = 9
    print(f'Adult movies count : {adult_movies_count(movies_df)}')
    
    # 2) How many movies are listed as animation? = 1935
    print(f'Animated movies count : {animation_movies_count(movies_df)}')
    
    # 3) Which movie had the highest budget? = ('Pirates of the Caribbean: On Stranger Tides', '380000000')
    lbm = largest_budget_movie(movies_df)
    print(f'Highest budget movie : {lbm[0]} Budget : {lbm[1]}')

    # 4) Which danish movie is most popular?
    mpdkm = most_popular_dk_movie(movies_df)
    print(f'Most popular danish produced movie is : {mpdkm[0]}, with the rating : {mpdkm[1]}')
    
    # 5) Which english action movie had the biggest revenue? 
    bream = biggest_revenue_english_action_movie(movies_df)
    print(f'Biggest revenue of {bream[1]} belongs to English Action movie: {bream[0]}')