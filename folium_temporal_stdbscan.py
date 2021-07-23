import folium
import pandas as pd
from TweetCrawler import *
from config import *
import pandas as pd
import numpy as np
from ModelBristol import *
from ModelFishNet import *
from ModelSTDBSCAN import *
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

# ////////// TEMPORAL MARKERS

# GET tweets
query_dbscan_004_5_df = tweetCrawler.crawl_data_with_session(
    STDBSCAN_02_10800_3_SEM)

"""
single_area = query_dbscan_004_5_df.loc[query_dbscan_004_5_df["temp_day_id"]
                                        == 3]

single_area = single_area.loc[single_area["dbscan_004_5_temp_id"] == 1]

print("df: ", single_area)
"""

# CREATE GEOJSON POLYGONS (from DB)
geojson_dbscan_unigrams = create_timestamped_geojson_polygons_dbscan_times(
    query_dbscan_004_5_df, 'tfidf_bigrams')
# geojson_dbscan_bigrams = create_timestamped_geojson_polygons_dbscan(
#    query_dbscan_004_5_df, 'tfidf_igrams')


# ADD TIMESTAMPED GEOJSON TO MAP
TimestampedGeoJson(geojson_dbscan_unigrams,
                   period='P1D',
                   duration='PT1H',  # If None, all previous times show
                   transition_time=2000,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(dualmap_uk.m1)

"""
TimestampedGeoJson(geojson_dbscan_bigrams,
                   period='P1D',
                   duration='PT1H',  # If None, all previous times show
                   transition_time=1000,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(dualmap_uk.m2)
"""

# SAVE MAP AS HTML FILE
dualmap_uk.save('html/textclassified_stdbscan_bigrams_dualmap.html')
