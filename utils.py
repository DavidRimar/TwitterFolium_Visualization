import numpy as np
import pandas as pd


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

        # create a Feature Collection for each grid
        geo_json = {"type": "FeatureCollection",
                    "properties": {
                        "random": "random"
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


def create_geojson_words_circle(df):

    features = []

    for _, row in df.iterrows():

        # get the words to display
        words = get_word_string(row['tfidf_topwords'])

        conditionalColor = 'black'
        # if words string above is larger in its length than 1
        if len(words) > 1:
            conditionalColor = 'red'

        #
        # date_string = row['time_day'].strftime("%Y-%m-%d %H:%M:%S")
        date_string_2 = str(row['time_day'])
        # print("date:", pd.to_datetime(row['time_day'], unit='d').__str__())

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['fishnet_geom_center_lon'], row['fishnet_geom_center_lat']]
            },
            'properties': {
                # pd.to_datetime(row['time_day'], unit='d').__str__(),
                'time': date_string_2,
                'style': {'color': ''},
                'icon': 'circle',
                'iconstyle': {
                    'fillColor': conditionalColor,
                    'fillOpacity': 0.99,
                    'stroke': 'true',
                    'radius': 5
                },
                'label': words
            }
        }

        # add feature to features
        features.append(feature)

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
