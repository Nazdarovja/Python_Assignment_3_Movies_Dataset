import os.path
import sys
import statistics
from Utility.Downloader import download_as_file as downloader
import pandas as pd
import os
import plotters


if __name__ == "__main__":
    try:
        _, url, file_name = sys.argv
    except:
        try:
            _, url, = sys.argv
            file_name = os.path.basename(url)
            downloader(url, file_name)
        except Exception as e:
            print("Something went wrong.. : ", e)
            sys.exit(1)

    # download file from given url as file_name
    downloader(url, file_name)

    # extract data from downloaded file, as a pandas dataframe
    movies_metadata = pd.read_csv(file_name, low_memory=False)

    # feed dataframe to sub methods

    # 1
    num_of_adult_movies = statistics.num_of_adult_movies(movies_metadata)
    print('Number of movies rated as adult = {}'.format(num_of_adult_movies))

    # 2
    num_of_animation_movies = statistics.num_of_animation_movies(
        movies_metadata)
    print('Number of movies of type animation  = {}'.format(
        num_of_animation_movies))

    # 3
    movie_with_highest_budget = statistics.movie_with_highest_budget(
        movies_metadata)
    print('Movies with the highest budget  = {}'.format(movie_with_highest_budget))

    #4
    print(statistics.most_popular_danish_movie(movies_metadata))

    #5
    print(statistics.english_movie_with_most_revenue(movies_metadata))

    #6,7,8
    plotters.plot_assignment(movies_metadata)