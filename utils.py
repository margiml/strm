import datetime
import re
import matplotlib.pyplot as plt


def fix_missing_values(df):
    """
    Rreturns a dataframe that changes missing values to default values: "not reported" and for date variable
    31-Dec-99
    :param df: dataframe

    Returns:
    df: dataframe with NaN values changed
    """

    df.fillna({'date_added': "31-Dec-99"}, inplace=True)
    df.fillna({'rating': "not reported"}, inplace=True)
    df.fillna({'director': "not reported"}, inplace=True)
    df.fillna({'cast': "not reported"}, inplace=True)
    df.fillna({'country': "not reported"}, inplace=True)

    return df

def format_date(x):

    """
    Return a date with a new format since there are three differents date formats, this function unifies them in the
    format yyyy-mm-dd
    :param date
    :return date with the new format
    """

    # this if analyzes the format dd-mes-yy

    if re.findall(r'\w{2}-\w+-\w{2}', x):
        i2 = str(datetime.datetime.strptime(x, "%d-%b-%y"))
        i3 = i2.replace(" 00:00:00", "")
        return i3

    # this if analyzes the format month d, yyyy, for example: November 1, 2019

    elif re.findall(r' \d{1},', x):
        d = str(re.findall(r'\d{1},', x))
        d2 = re.sub(r'\d{1},', "0" + d[2] + ",", x)
        i4 = str(datetime.datetime.strptime(d2, " %B %d, %Y"))
        i5 = i4.replace("00:00:00", "")
        return i5

    # this if analyzes the format month dd, yyyy, for example: November 10, 2019

    else:
        i6 = str(datetime.datetime.strptime(x, " %B %d, %Y"))
        i7 = i6.replace("00:00:00", "")
        return i7

def create_graphs(gp):

    """
    generates a bar chart showing the number of videos and tv shows for each rating.
    :param gp: receives a tuple containing the number of movies and tv shows for each genre
    :return: a graph
    """
    ratings = [name for name, group in gp]
    counts = [len(group) for name, group in gp]

    fig, ax = plt.subplots()
    # axis Y
    ax.set_ylabel('Videos')
    # axis X
    ax.set_title('Number of videos per rating')

    # creation of the graphic
    plt.barh(ratings, counts)
    plt.savefig('bar_graphic.png')
    plt.show()

def identifies_genres_countries(gr):

    """
    returns a list with de the differents genres or countries
    :param gr: array of one dimension
    :return data_list: list with the differents genres or countries
    """

    # An empty list is created
    data_dict = {}

    # Each element of the array gr is iterated, converting it into a list of lists.
    for i in list(gr):

        # Separate each item in the list by commas and spaces
        y = i.split(sep=", ")

        for x in y:

            x = x.replace(",", "")

            if x in data_dict:
                data_dict[x] += 1

            else:
                data_dict[x] = 1

    return data_dict

