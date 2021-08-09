import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime, timedelta
from datetime_truncate import *
from utils import *
from folium.plugins import TimestampedGeoJson
from folium.plugins import DualMap


class FoliumMapMaker():

    ### CONSTRUCTOR ###
    def __init__(self):

        ### INSTANCE VARIABLES ###
        self.center_uk = [53.890000, -3.711111]  # latitude, longitude
        self.dualmap_uk = DualMap(location=self.center_uk,
                                  tiles='openstreetmap',  # 'cartodbpositron'
                                  zoom_start=6, control_scale=True)

     ### METHODS ###

    def create_dualmap_fishnet_daily(self, df1, df2, tfidf_map1, tfidf_map2, volume_1, volume_2, save_location):

        # CREATE GEOJSON GRIDS (from DB)
        geojson_df1 = create_timestamped_geojson_polygons_fishnet(
            df1, tfidf_map1, volume_1)
        geojson_df2 = create_timestamped_geojson_polygons_fishnet(
            df2, tfidf_map2, volume_1)

        # ADD TIMESTAMPED GEOJSON TO MAPS
        TimestampedGeoJson(geojson_df1,
                           period='P1D',
                           duration='PT1H',  # If None, all previous times show
                           transition_time=1000,
                           auto_play=False,
                           time_slider_drag_update=True).add_to(self.dualmap_uk.m1)

        TimestampedGeoJson(geojson_df1,
                           period='P1D',
                           duration='PT1H',
                           transition_time=1000,
                           auto_play=False,
                           time_slider_drag_update=True).add_to(self.dualmap_uk.m2)

        # save map to html file
        self.dualmap_uk.save(save_location)

    def create_timestamped_geojson_polygons_fishnet(self, df, tfidf, volume):

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

    def create_timestamped_geojson_polygons_dbscan(self, df, tfidf_results):

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
                date_string = pd.to_datetime(
                    row['time_day'], unit='d').__str__()

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

    def create_timestamped_geojson_polygons_stdbscan(self, df, tfidf_results, time_interval):

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
