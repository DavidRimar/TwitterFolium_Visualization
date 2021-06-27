import numpy as np
import pandas as pd


def get_word_string(dictionary):

    words = dictionary.keys()
    display_string = ""
    for word in words:

        display_string += word
        display_string += "\n\n"

    # a_list = list(a_view)
    return display_string


def get_geojson_grid(upper_right, lower_left, h=5, v=11):
    """Returns a grid of geojson rectangles, and computes the exposure in each section of the grid based on the vessel data.

    Parameters
    ----------
    upper_right: array_like
        The upper right hand corner of "grid of grids" (the default is the upper right hand [lat, lon] of the USA).

    lower_left: array_like
        The lower left hand corner of "grid of grids"  (the default is the lower left hand [lat, lon] of the USA).

    n: integer
        The number of rows/columns in the (n,n) grid.

    Returns
    -------

    list
        List of "geojson style" dictionary objects   
    """

    all_boxes = []

    lat_steps = np.linspace(lower_left[0], upper_right[0], v+1)
    lon_steps = np.linspace(lower_left[1], upper_right[1], h+1)

    lat_stride = lat_steps[1] - lat_steps[0]
    lon_stride = lon_steps[1] - lon_steps[0]

    for lat in lat_steps[:-1]:
        for lon in lon_steps[:-1]:
            # Define dimensions of box in grid
            upper_left = [lon, lat + lat_stride]
            upper_right = [lon + lon_stride, lat + lat_stride]
            lower_right = [lon + lon_stride, lat]
            lower_left = [lon, lat]
            # center
            center = [lat + (lat_stride/2), lon + (lon_stride/2)]

            # Define json coordinates for polygon
            coordinates = [
                upper_left,
                upper_right,
                lower_right,
                lower_left,
                upper_left
            ]

            geo_json = {"type": "FeatureCollection",
                        "properties": {
                            "lower_left": lower_left,
                            "upper_right": upper_right,
                            "center": center
                        },
                        "features": []}

            grid_feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [coordinates],
                }
            }

            geo_json["features"].append(grid_feature)

            all_boxes.append(geo_json)

    return all_boxes


def create_geojson_words_circle(df):

    features = []

    for _, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['fishnet_geom_center_lon'], row['fishnet_geom_center_lat']]
            },
            'properties': {
                'time': '1999-09-09 12:00:00',
                'style': {'color': ''},
                'icon': 'circle',
                'iconstyle': {
                    'fillColor': 'red',
                    'fillOpacity': 0.8,
                    'stroke': 'true',
                    'radius': 5
                },
                'label': 'eee'
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
