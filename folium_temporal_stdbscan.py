import folium
import pandas as pd
from TweetCrawler import *
from config import *
import pandas as pd
import numpy as np
from models.ModelSTDBSCAN import *
from models.ModelBristol import *
from models.ModelFishNet import *
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


# CREATE GEOJSON POLYGONS (from DB)
geojson_dbscan_daily = create_timestamped_geojson_polygons_stdbscan(
    query_dbscan_004_5_df, 'tfidf_unigrams', 'span_day')
geojson_dbscan_hourly = create_timestamped_geojson_polygons_stdbscan(
    query_dbscan_004_5_df, 'tfidf_unigrams', 'span_hour')


# ADD TIMESTAMPED GEOJSON TO MAP
TimestampedGeoJson(geojson_dbscan_daily,
                   period='P1D',
                   duration='PT1H',  # If None, all previous times show
                   transition_time=2000,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(dualmap_uk.m1)


TimestampedGeoJson(geojson_dbscan_hourly,
                   period='PT1H',
                   duration='PT1M',  # If None, all previous times show
                   transition_time=600,
                   auto_play=False,
                   time_slider_drag_update=True).add_to(dualmap_uk.m2)


# SAVE MAP AS HTML FILE
dualmap_uk.save('html/textclassified_unigrams.html')
