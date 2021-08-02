## Leaflet Dualmaps created to visualise Spatiotemporal and Semantic Patterns in the context of the 2021 Bristol Riots

The maps are created using Python's Folium module to create Timestamped GeoJSON objects from the tweets collected for the purposes of this project. Here is a description to the purpose of each maps:

Map 1 and 2 shows the fishnet grids for both inspected resolution side by side and the TF-IDF unigrams and bigrams, respectively. The purpose of these maps is to analyze the Modifiable Areal Unit Problem (MAUP).

- Link to Map 1: https://twitter-folium-visualisations.herokuapp.com/
- Link to Map 2: https://twitter-folium-visualisations.herokuapp.com/map2_fishnet_bigrams

Map 3 shows DBSCAN daily clusters and the 10km^2 fishnet results from Map 2 in order to draw comparisons with respect to the spatial partition dilemma.

- Link to Map 3: https://twitter-folium-visualisations.herokuapp.com/map3_dbscan_fishnet_bigrams

Map 4 displays classified tweets along with the 10km^2 fishnet from Map 2 and is aimed at comparing the classification effect on the TF-IDF results and normalized volumes. Map 4A uses the intra-grid scaling technique while Map 4B shows the spatiotemporal normalized volumes.

- Link to Map 4A: https://twitter-folium-visualisations.herokuapp.com/map4_fishnet_textcat_pure_intraspace
- Link to Map 4B: https://twitter-folium-visualisations.herokuapp.com/map4_fishnet_textcat_pure_normalized

Map 5 shows the spatiotemporal clustering (STDBSCAN) of the positively classified tweets on a daily and hourly basis.

- Link to Map 5: https://twitter-folium-visualisations.herokuapp.com/map5_textcat_stdbscan_bigrams
