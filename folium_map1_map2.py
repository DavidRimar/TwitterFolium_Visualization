import folium
import pandas as pd
from TweetCrawler import *
from config import *
import pandas as pd
import numpy as np
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
query_11_5_df = tweetCrawler.crawl_data_with_session(Fishnet_11_5)
query_88_40_df = tweetCrawler.crawl_data_with_session(Fishnet_88_40)

# CREATE GEOJSON GRIDS (from DB)
geojson_11_5_grids = create_timestamped_geojson_polygons_fishnet(
    query_11_5_df, 'tfidf_bigrams', 'normalized_volumes')
geojson_88_40_grids = create_timestamped_geojson_polygons_fishnet(
    query_88_40_df, 'tfidf_bigrams', 'normalized_volumes') 


# ADD TIMESTAMPED GEOJSON TO MAPS
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
dualmap_uk.save(
    'html/fishnet_map2.html')
