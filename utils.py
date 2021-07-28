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


def create_timestamped_geojson_polygons_fishnet(df, tfidf, volume):

    # new_df = scale_number(0, 1, df)

    features = []

    for _, row in df.iterrows():

        # get the words to display
        words = get_word_string(row[tfidf])

        # get color
        norm_vol = float("{:.12f}".format(row[volume]))
        color = plt.cm.Reds(norm_vol)
        color = mpl.colors.to_hex(color)

        # date_string
        # date_string = str(row['time_day'])
        date_string = pd.to_datetime(row['time_day'], unit='d').__str__()

        # print("day: ", date_string)

        feature = {
            'type': 'Feature',
            'geometry': row["st_asgeojson"],
            'properties': {
                'time': date_string,
                'style': {'color': 'blue',
                          # 'width': 1,
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
            # date_string = str(row['time_day'])
            date_string = pd.to_datetime(row['time_day'], unit='d').__str__()

            # print("day: ", date_string)

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


def create_timestamped_geojson_polygons_stdbscan(df, tfidf_results, time_interval):

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

            # get array of times
            if time_interval == 'span_day':

                string_of_dates = create_dates_array_daily(row)

            elif time_interval == 'span_hour':

                string_of_dates = create_dates_array_hourly(row)

            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': row["st_asgeojson"]['type'],
                    # duplication of geoJSONs for each time window
                    'coordinates': row["st_asgeojson"]['coordinates'] * row[time_interval],
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

        # next_day_str = pd.to_datetime(start_date, unit='d').__str__()
        next_day_str = truncate(start_date, 'day').__str__()

        # append to dates_array
        dates_array.append(next_day_str)

    # print(row['stdbscan_id'], " - ", dates_array)

    return dates_array


def create_dates_array_hourly(row):

    dates_array = []
    # if 1, nothing gets added part from start_date
    time_span = row['span_hour']
    start_date = row['start_date']
    # start_date_str = pd.to_datetime(row['start_date'], unit='d').__str__()
    # dt.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date_str = truncate(row['start_date'], 'hour').__str__()

    dates_array.append(start_date_str)

    for i in range(1, time_span):

        start_date += timedelta(hours=1)

        # next_day_str = pd.to_datetime(start_date, unit='d').__str__()
        next_day_str = truncate(start_date, 'hour').__str__()

        # append to dates_array
        dates_array.append(next_day_str)

    print(row['stdbscan_id'], " - ", dates_array)

    return dates_array
