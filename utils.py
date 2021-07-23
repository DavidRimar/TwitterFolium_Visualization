import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime, timedelta
from datetime_truncate import *


def get_word_string(dictionary):

    words = dictionary.keys()
    display_string = ""
    for word in words:

        display_string += word
        display_string += "<br>"

    # a_list = list(a_view)
    return display_string


def create_timestamped_geojson_polygons_fishnet(df, tfidf):

    # new_df = scale_number(0, 1, df)

    features = []

    for _, row in df.iterrows():

        # get the words to display
        words = get_word_string(row[tfidf])

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
                          'stroke': 1,
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
                              'stroke-width': 1,
                              'fillColor': color,
                              'fillOpacity': 0.59},
                    'label': words,
                }
            }

            # add feature to features
            features.append(feature)

    return features


def create_timestamped_geojson_polygons_dbscan_times(df, tfidf_results):

    features = []

    for _, row in df.iterrows():

        # if scaled vols are not null
        if (row['st_asgeojson']['type'] == 'Polygon'):

            # get the words to display
            words = get_word_string(row[tfidf_results])

            # get color
            norm_vol = float("{:.12f}".format(row['scaled_vol_1']))
            color = plt.cm.Reds(norm_vol)
            color = mpl.colors.to_hex(color)

            # get time
            #string_of_dates = [row['start_date'], row['end_date']]
            # string_of_dates = ["2021-03-03 00:00:00",
            #                   "2021-03-04 00:00:00", "2021-03-05 00:00:00"]
            string_of_dates = create_dates_array_daily(row)

            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': row["st_asgeojson"]['type'],
                    # duplication for matching 6 timestamps
                    'coordinates': row["st_asgeojson"]['coordinates'] * row['span_day'],
                },
                'properties': {
                    'times': string_of_dates,
                    'style': {'color': 'blue',
                              'fillColor': color,
                              'fillOpacity': 0.59},
                    'label': words,
                }
            }

            # add feature to features
            features.append(feature)

    return features


def create_dates_array_daily(row):

    dates_array = []
    # if 1, nothing gets added part from start_date
    time_span = row['span_day']
    start_date = row['start_date']
    # start_date_str = pd.to_datetime(row['start_date'], unit='d').__str__()
    # dt.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date_str = truncate(row['start_date'], 'day').__str__()

    dates_array.append(start_date_str)

    for i in range(1, time_span):

        start_date += timedelta(days=1)

        #next_day_str = pd.to_datetime(start_date, unit='d').__str__()
        next_day_str = truncate(start_date, 'day').__str__()

        # append to dates_array
        dates_array.append(next_day_str)

    print(row['stdbscan_id'], " - ", dates_array)

    return dates_array
