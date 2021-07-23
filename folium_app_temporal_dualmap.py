import folium
import pandas as pd
from TweetCrawler import *
from config import *
import pandas as pd
import numpy as np
from ModelBristol import *
from ModelFishNet import *
from ModelGrids import *
from utils import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from folium.plugins import TimestampedGeoJson
from folium.plugins import DualMap

# ###########################
# instantiate TweetCrawler object
tweetCrawler = TweetCrawler(DATABASE_URI_RDS_TWEETS)

# instantiatie map
center = [53.890000, -3.711111]  # latitude, longitude
dualmap_uk = DualMap(location=center,
                     tiles='openstreetmap',  # 'cartodbpositron'
                     zoom_start=6, control_scale=True)

###############################

"""
# ////////// GRID VIEWS
# get the grids from postgreSQL
fishnet_11_5_df = tweetCrawler.crawl_data_with_session(
    GRID_11_5)
fishnet_88_40_df = tweetCrawler.crawl_data_with_session(
    GRID_88_40)

# format to GeoJSON that conforms to Folium
grid_11_5 = get_geoJSON_grids_postgres(fishnet_11_5_df)
grid_88_40 = get_geoJSON_grids_postgres(fishnet_88_40_df)

# iterate over all geo_json objects (each is a FeatureCollection)
for i, geo_json in enumerate(grid_11_5):

    color = plt.cm.Reds(i / len(grid_11_5))
    color = mpl.colors.to_hex(color)

    gj = folium.GeoJson(geo_json,
                        style_function=lambda feature, color=color: {
                            'fillColor': color,
                            'color': "blue",
                            'weight': 1.5,
                            'dashArray': '1, 1',
                            'fillOpacity': 0.99
                            # Radius in metres
                        })

    dualmap_uk.m1.add_child(gj)

for i, geo_json in enumerate(grid_88_40):

    color = plt.cm.Reds(i / len(grid_88_40))
    color = mpl.colors.to_hex(color)

    gjs = folium.GeoJson(geo_json,
                         style_function=lambda feature, color=color: {
                             'fillColor': color,
                             'color': "blue",
                             'weight': 1,
                             'dashArray': '1, 1',
                             'fillOpacity': 0.01
                             # Radius in metres
                         })

    dualmap_uk.m2.add_child(gjs)
"""

# ////////// TEMPORAL MARKERS

# GET tweets
query_11_5_df = tweetCrawler.crawl_data_with_session(
    BristolFishnet_11_5)
query_88_40_df = tweetCrawler.crawl_data_with_session(
    BristolFishnet_88_40)

query_11_5_df = query_11_5_df.sort_values(by=['time_day'])
query_88_40_df = query_88_40_df.sort_values(by=['time_day'])

#query_11_5_df = query_11_5_df[query_11_5_df['temp_day_id'] < 32]
#query_88_40_df = query_88_40_df.loc(query_88_40_df['temp_day_id'] == 33)

# print(query_11_5_df.head(10))
# print(query_df.tail(10))

# CREATE GEOJSON GRIDS (from DB)
geojson_11_5_grids = create_timestamped_geojson_polygons_fishnet(
    query_11_5_df, 'tfidf_topwords2')
geojson_88_40_grids = create_timestamped_geojson_polygons_fishnet(
    query_88_40_df, 'tfidf_topwords_lem')

#print("example: ", geojson_11_5_circles[0])

TimestampedGeoJson(geojson_11_5_grids,
                   period='P1D',
                   duration='PT1H',  # If None, all previous times show
                   transition_time=1000,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(dualmap_uk.m1)


TimestampedGeoJson(geojson_88_40_grids,
                   period='P1D',
                   duration='PT1H',
                   transition_time=1000,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(dualmap_uk.m2)


# save map to html file
dualmap_uk.save('html/fishnet_dualmap_unigrams2.html')
