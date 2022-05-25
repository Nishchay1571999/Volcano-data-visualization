from asyncore import read
import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lang = list(data["LON"])
names = list(data["NAME"])
elev = list(data["ELEV"])
statuses = list(data["STATUS"])

def color_decider(elevation):
    if elevation>2500:
        return 'black'
    elif elevation>2000:
        return 'darkblue'
    elif elevation>1500:
        return 'red'
    else:
        return 'orange'

html = """
<h4>%s</h4>
<h4>Volcano information:</h4>
Height: %s m
<br/>
<br/>
Status: %s
"""

map = folium.Map(location=[30.58,-99.09], zoom_start=5, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")



for el,name,la,lg,status in zip(elev,names,lat,lang,statuses):
    iframe = folium.IFrame(html=html % (str(name),str(el), str(status)), width=300, height=100)
    fgv.add_child(folium.Marker(location=[la,lg],popup=folium.Popup(iframe),icon=folium.Icon(color=color_decider(el))))


fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                                 style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000>= x['properties']['POP2005']<=20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl( ))
map.save("index.html")