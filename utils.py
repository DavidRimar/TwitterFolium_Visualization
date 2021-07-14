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


"""
How to create GeoJSOn from database ishnet grid
ST_
GDAL - ogr2ogr
"""

# passing in fishnet_11_5_sem


def get_geoJSON_grids_postgres(df):
    """Returns a grid of geojson rectangles as a Feature Collection.

    Parameters
    ----------
    df: The dataframe from the PostGreSQL

    Returns
    -------

    list
        List of "geojson style" dictionary objects
    """
    all_grids = []

    for index, row in df.iterrows():

        # get time
        date_string = str(row['time_day'])

        # get the words to display
        words = get_word_string(row['tfidf_bigrams'])

        # get the color based on normalized volumes

        # set color based on normalized volumes
        n_random = random.random()

        print("n_RANDOM: ", n_random)

        cmap = plt.cm.get_cmap('OrRd')

        num = 0.0

        if (index % 2) == 0:
            num = 1.0

        colorVolume = cmap(num)

        # create a Feature Collection for each grid
        geo_json = {"type": "FeatureCollection",
                    "properties": {
                        "random": "random",
                        "color": colorVolume,
                        'label': words,
                        'time': date_string
                    },
                    "features": []}

        # get the grid as geoJSON
        grid_feature = {
            "type": "Feature",
            "geometry": row["st_asgeojson"]
        }

        geo_json["features"].append(grid_feature)

        all_grids.append(geo_json)

    return all_grids


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
                # 'icon': 'circle',
                # 'iconstyle': {
                #    'fillColor': conditionalColor,
                #    'fillOpacity': 0.99,
                #    'stroke': 'true',
                #    'radius': 5
                # },
            }
        }

        # add feature to features
        features.append(feature)

    print("featureset:", features)

    return features


def create_geojson_words_markers(df):

    features = []

    for _, row in df.iterrows():

        words = get_word_string(row['tfidf_topwords'])

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['fishnet_geom_center_lon'], row['fishnet_geom_center_lat']]
            },
            'properties': {
                # pd.to_datetime(row['day'], unit='h').__str__(),
                'time': '1999-09-09 12:00:00',
                'style': {'color': 'red'},
                'icon': 'DivIcon',
                'iconstyle': {
                    'icon_size': (30, 20),
                    'html': f'''<div style="font-size: 90%; align:center">{words}</div>'''
                }

            }
        }

        # add feature to features
        features.append(feature)

    return features


def scale_number(scale_lower, scale_upper, df):
    """
    Returns a new dataframe with an extra column of the scaled numbers.
    """
    a, b = scale_lower, scale_upper
    x, y = df.normalized_volumes.min(), df.normalized_volumes.max()
    spat_df['scaled_normalized'] = (
        df.normalized_volumes - x) / (y - x) * (b - a) + a

    """
    # scale using values from within the same spatial division
    for day in range(1, days):

        spat_df = df[df['temp_day_id'] == day]
        x, y = spat_df.normalized_volumes.min(), spat_df.normalized_volumes.max()

        spat_df['scaled_normalized'] = (
            df.normalized_volumes - x) / (y - x) * (b - a) + a
    """

    return df
