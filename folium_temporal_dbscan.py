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

# ////////// TEMPORAL MARKERS

# GET tweets
query_dbscan_004_5_df = tweetCrawler.crawl_data_with_session(
    BristolDBSCAN_004_5_SEM)
query_88_40_df = tweetCrawler.crawl_data_with_session(
    BristolFishnet_88_40)

# sort values
query_dbscan_004_5_df = query_dbscan_004_5_df.sort_values(by=['time_day'])
query_88_40_df = query_88_40_df.sort_values(by=['time_day'])

# CREATE GEOJSON POLYGONS (from DB)
geojson_dbscan_bigrams = create_timestamped_geojson_polygons_dbscan(
    query_dbscan_004_5_df, 'tfidf_bigrams')
geojson_88_40_grids = create_timestamped_geojson_polygons_fishnet(
    query_88_40_df, 'tfidf_bigrams')


# ADD TIMESTAMPED GEOJSON TO MAP
TimestampedGeoJson(geojson_dbscan_bigrams,
                   period='P1D',
                   duration='PT1H',  # If None, all previous times show
                   transition_time=2000,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(dualmap_uk.m1)


TimestampedGeoJson(geojson_88_40_grids,
                   period='P1D',
                   duration='PT1H',  # If None, all previous times show
                   transition_time=1000,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(dualmap_uk.m2)


# SAVE MAP AS HTML FILE
dualmap_uk.save('html/map3_dbscan_fishnet_bigrams.html')
