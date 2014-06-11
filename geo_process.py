
import graphlab as gl
import numpy as np
from graphlab import *

def geo_process(data, n_cluster, fileName):

    keylist = ['latitude', 'longitude']

    lat_log_info = data.select_columns(keylist)
    out = kmeans.create(lat_log_info, num_clusters=n_cluster, max_iter=30)
    cluster_info = out.get('cluster_info')

    center = SFrame( {'lat': cluster_info['latitude'], 'log': cluster_info['longitude']})
    center.save('./center.csv')

    label = out.get('clusterid')
    geo_label = SArray(data = label['clusterid'], dtype=int)
    print geo_label.head(10)
    geo_label.save(fileName)
