import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib as mpl


def get_word_string(dictionary):

    words = dictionary.keys()
    display_string = ""
    for word in words:

        display_string += word
        display_string += "<br>"

    # a_list = list(a_view)
    return display_string


def create_timestamped_geojson_polygons(df):

    # new_df = scale_number(0, 1, df)

    features = []

    for _, row in df.iterrows():

        # get the words to display
        words = get_word_string(row['tfidf_bigrams'])

        # get color
        norm_vol = float("{:.12f}".format(row['scaled_vol_06']))
        color = plt.cm.Reds(norm_vol)
        color = mpl.colors.to_hex(color)

        # date_string
        #date_string = str(row['time_day'])
        date_string = pd.to_datetime(row['time_day'], unit='d').__str__()

        #print("day: ", date_string)

        feature = {
            'type': 'Feature',
            'geometry': row["st_asgeojson"],
            'properties': {
                'time': date_string,
                'style': {'color': 'blue',
                          'fillColor': color,
                          'fillOpacity': 0.59},
                'label': words,
            }
        }

        # add feature to features
        features.append(feature)

    print("featureset:", features)

    return features


def create_timestamped_geojson_polygons_dbscan(df, tfidf_results):

    features = []

    for _, row in df.iterrows():

        # if scaled vols are not null
        if (row['scaled_vol_06'] is not None and row['st_asgeojson']['type'] == 'Polygon'):

            # get the words to display
            words = get_word_string(row[tfidf_results])

            # get color
            norm_vol = float("{:.12f}".format(row['scaled_vol_06']))
            color = plt.cm.Reds(norm_vol)
            color = mpl.colors.to_hex(color)

            # date_string
            #date_string = str(row['time_day'])
            date_string = pd.to_datetime(row['time_day'], unit='d').__str__()

            #print("day: ", date_string)

            feature = {
                'type': 'Feature',
                'geometry': row["st_asgeojson"],
                'properties': {
                    'time': date_string,
                    'style': {'color': 'blue',
                              'fillColor': color,
                              'fillOpacity': 0.59},
                    'label': words,
                }
            }

            # add feature to features
            features.append(feature)

    return features
