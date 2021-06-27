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
from folium.plugins import TimestampedGeoJson


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
# ////////// GRID
"""
for i, geo_json in enumerate(grid):

    color = plt.cm.Reds(i / len(grid))
    color = mpl.colors.to_hex(color)

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

    map_uk.add_child(gj)

"""

first_day_df = query_df.loc[query_df['temp_day_id'] == 1]

# ////////// TEMPORAL MARKERS
geojson_markers = create_geojson_words_circle(first_day_df)

print("example: ", geojson_markers[0])

TimestampedGeoJson(geojson_markers,
                   period='PT1H',
                   duration='PT1M',
                   transition_time=1000,
                   auto_play=False).add_to(map_uk)
"""
for i, feature in enumerate(geojson_markers):

    color = plt.cm.Reds(i / len(grid))
    color = mpl.colors.to_hex(color)

    feat = folium.GeoJson(feature)

    map_uk.add_child(feat)
"""

# save map to html file
map_uk.save('index_temp.html')
