import pandas as pd
import numpy as np
from utils import fix_missing_values, format_date, create_graphs, identifies_genres_countries

if __name__ == "__main__":

    # Load dataset
    data = pd.read_csv("data/NetFlix.csv")

    # The number of missing values in each variable is identified.
    print(data.isnull().sum())

    # The function that assigns default values to the variables that have missing values is applied
    fix_missing_values(data)

    # The variables: rating, director, cast and country with missing values are replaced with not reported
    y = data[(data.rating == "not reported")]
    z = data[(data.director == "not reported")]
    w = data[(data.cast == "not reported")]
    v = data[(data.country == "not reported")]
    p = data[(data.date_added == "31-Dec-99")]
    print("{} NaN were replaced in variable rating".format(len(y["rating"])))
    print("{} NaN were replaced in variable director".format(len(z["director"])))
    print("{} NaN were replaced in variable cast".format(len(w["cast"])))
    print("{} NaN were replaced in variable country".format(len(v["country"])))
    print("{} NaN were replaced in variable date_added".format(len(p["date_added"])))

    # The format date is changed in the column date_added. New format is yyyy-mm-dd
    data["date_added"] = data["date_added"].apply(format_date)
    print(data["date_added"])

    # Unique values are checked in the column title
    u = data.type.unique()
    print("There are {} unique values in the  column type:\n{}".format(len(u), u))

    movies = data[data.type == "Movie"]
    tv_shows = data[data.type == "TV Show"]
    print("{} are movies".format(len(movies)))
    print("{} are TV-shows".format(len(tv_shows)))

    # Unique values are checked in the column rating
    rating = pd.unique(data["rating"])
    print("There are {} unique values in the column rating:\n{}".format(len(rating), rating))

    # Identify how many TV-shows and movies there are for each classification
    grouped = data.groupby("rating")
    for name, group in grouped:
        print(name + ":", len(group))

    # The proportion of movies and tv-shows by rating is shown in a bar graph
    create_graphs(grouped)

    # Dataframe grouping by type and rating
    print()
    grouped2 = data.groupby(["rating", "type"])
    print("Number of Movies and Tv-shows by rating are:")
    print()
    for name, group in grouped2:
        print("there are {} {} that are rating {}".format(len(group), name[1], name[0]))

    # the different genres that exist are searched
    genres = pd.unique(data["genres"])
    print()
    print("There are {} differents genres, they are:".format(len(identifies_genres_countries(genres))))
    print()

    dic_g = identifies_genres_countries(genres)
    for k, v in dic_g.items():
        print(k, v)

    # The different release years contained in the dataframe are checked.
    year = data.release_year.unique()
    np.sort(year)

    countries = pd.unique(data["country"])
    print()
    print("There are {} countries, where the movie/show was produced:".format(len(identifies_genres_countries(countries))))
    print()

    dic_c = identifies_genres_countries(countries)
    for k, v in dic_c.items():
        print(k, v)
