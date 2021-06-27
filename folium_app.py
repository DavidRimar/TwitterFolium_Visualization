import folium
import pandas as pd
from TweetCrawler import *
from config import *
import pandas as pd
import numpy as np
from ModelBristol import *
from ModelFishNet import *
from utils import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def get_word_string(dictionary):
    words = dictionary.keys()
    display_string = ""
    for word in words:

        display_string += word
        display_string += "\n\n"

    # a_list = list(a_view)
    return display_string


# DATA
# INSTANTIATE TweetCrawler object
tweetCrawler = TweetCrawler(DATABASE_URI_RDS_TWEETS)

# GET tweets
query_df = tweetCrawler.crawl_data_with_session(
    BristolFishnet)

print(query_df.head(10))

# -0.023559, 37.9061928
center = [53.890000, -3.711111]  # latitude, longitude

map_uk = folium.Map(location=center, zoom_start=6,
                    control_scale=True)

lower_left = [49.97, -7.30]  # lon: -7.30, lat: 49.97
upper_right = [60.95, 2.35]  # lon: 2.30, lat: 59.145
grid = get_geojson_grid(upper_right, lower_left, h=5, v=11)

"""
for index, row in query_df.iterrows():
    location = [row['latitude'], row['longitude']]
    folium.Marker(
        location, popup=f'Name:{franchise["store"]}\n Revenue($):{franchise["revenue"]}').add_to(map_kenya)
"""
for i, geo_json in enumerate(grid):

    color = plt.cm.Reds(i / len(grid))
    color = mpl.colors.to_hex(color)

    """
    style_function=lambda feature, color=color: {
                            'fillColor': color,
                            'color': "black",
                            'weight': 2,
                            'dashArray': '5, 5',
                            'fillOpacity': 0.99,
                            # Radius in metres
                        },
                        marker=folium.Marker(location=gj_loc,
                                                icon=folium.DivIcon(
                                                    icon_size=(90, 90),
                                                    class_name="gj_class",
                                                    html=f'''<div style="font-size: 1.1em">{i}</div>''')
                                                )
    """
    gj_loc = geo_json['properties']['center']
    #print("gj_loc:", gj_loc)
    # print(type(gj_loc))

    gj = folium.GeoJson(geo_json,
                        style_function=lambda feature, color=color: {
                            'fillColor': color,
                            'color': "blue",
                            'weight': 2,
                            'dashArray': '1, 1',
                            'fillOpacity': 0.01
                            # Radius in metres
                        })

    first_day_df = query_df.loc[query_df['temp_day_id'] == 1]

    # FOR EACH GRID
    for index, row in first_day_df.iterrows():

        if ((i + 1) == row['fishnet_id']):

            print("sdfsd")

            words = row['tfidf_topwords']

            display_string = get_word_string(words)

            if len(words) > 0:

                # MARKER
                marker = folium.Marker(location=gj_loc,
                                       icon=folium.DivIcon(
                                           class_name="geojson_marker",
                                           html=f'''<div style="font-size: 90%; align:center">{display_string}</div>''')
                                       )

                gj.add_child(marker)

                map_uk.add_child(gj)

    # POPUP
    """
    popup = folium.Popup("example popup {}".format(i))
    gj.add_child(popup)
    """


# map_uk.add_child(grid)

first_day_df = query_df.loc[query_df['temp_day_id'] == 1]

# FOR EACH GRID
for index, row in first_day_df.iterrows():

    row_lon = float(row['fishnet_geom_center_lon'])  # +float(0.3)
    row_lat = float(row['fishnet_geom_center_lat'])  # -float(0.5)

    # print(type(row['tfidf_topwords']))
    # print(row['tfidf_topwords'])
    # this is a list of tuples
    # word_tuples = convert_dict_to_tuple(row['tfidf_topwords'])

    words = row['tfidf_topwords']

    if len(words) > 0:

        # generate wordcloud
        wordcloud = WordCloud().generate_from_frequencies(words)

        # get display string
        display_string = get_word_string(words)

        # ADD TEXT
        """
        folium.Marker(location=[row_lat, row_lon],
                      icon=folium.DivIcon(
            class_name="geojson_marker",
            html=f'''<div style="font-size: 13px">{display_string}</div>''')
        ).add_to(map_uk)
        """
# save map to html file
map_uk.save('index5.html')
