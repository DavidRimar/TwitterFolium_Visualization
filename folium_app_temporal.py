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


# INSTANTIATE TweetCrawler object
tweetCrawler = TweetCrawler(DATABASE_URI_RDS_TWEETS)

# -0.023559, 37.9061928
center = [53.890000, -3.711111]  # latitude, longitude

map_uk = folium.Map(location=center, zoom_start=6,
                    control_scale=True)

# ////////// GRID (postgresql)
fishnet_11_5_df = tweetCrawler.crawl_data_with_session(
    GRID_11_5)

grid = get_geoJSON_grids_postgres(fishnet_11_5_df)

print(grid[0])

# iterate over all geo_json objects (each is a FeatureCollection)
for i, geo_json in enumerate(grid):

    color = plt.cm.Reds(i / len(grid))
    color = mpl.colors.to_hex(color)

    gj = folium.GeoJson(geo_json,
                        style_function=lambda feature, color=color: {
                            'fillColor': color,
                            'color': "blue",
                            'weight': 1.5,
                            'dashArray': '1, 1',
                            'fillOpacity': 0.01
                            # Radius in metres
                        })

    map_uk.add_child(gj)

#first_day_df = query_df.loc[query_df['temp_day_id'] == 1]

# ////////// TEMPORAL MARKERS

# GET tweets
query_df = tweetCrawler.crawl_data_with_session(
    BristolFishnet)

query_df = query_df.sort_values(by=['time_day'])

print(query_df.head(10))
print(query_df.tail(10))

geojson_markers = create_geojson_words_circle(query_df)

print("example: ", geojson_markers[0])

TimestampedGeoJson(geojson_markers,
                   period='P1D',
                   duration=None,
                   transition_time=1000,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(map_uk)


# save map to html file
map_uk.save('html/fishnet_11_5.html')
