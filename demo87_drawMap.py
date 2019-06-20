import folium
import pandas as pd

wanhua = pd.read_csv('data\\data6.csv', sep=',')
beitou = pd.read_csv('data\\data5.csv', sep=',')
print beitou.columns, beitou.shape

print wanhua.columns, wanhua.shape
wanhua.columns = ['section','road','road_detail','lon','lat','extra']
beitou.columns = ['section','road','road_detail','lon','lat','extra']

print wanhua.head()
print beitou.head()

location1 = [25.024455, 121.507948]

zoom = 200
map_osm = folium.Map(location=location1, zoom_start=zoom)

map_osm.save('map\\demo86.html')

for i in range(len(wanhua)):
    coordinate = [wanhua.ix[i, 'lat'], float(wanhua.ix[i, 'lon'])]
    message = '%s,%s' % (wanhua.ix[i, 'road'], wanhua.ix[i, 'road_detail'])
    message = unicode(message, 'utf-8')
    folium.Marker(coordinate,
                  icon=folium.Icon(color='red', icon='trash'),
                  popup=message).add_to(map_osm)
    print coordinate

for i in range(len(beitou)):
    coordinate2 =[beitou.ix[i, 'lat'], float(beitou.ix[i, 'lon'])]
    message = '%s,%s' % (beitou.ix[i, 'road'], beitou.ix[i, 'road_detail'])
    message = unicode(message, 'utf-8')
    folium.Marker(coordinate2,
                  icon=folium.Icon(color='blue', icon='home'),
                  popup=message).add_to(map_osm)
    print coordinate2

map_osm.save('map\\demo86.html')



