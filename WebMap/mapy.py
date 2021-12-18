import folium

map = folium.Map(location=[50.21803255103559, 14.62273954043936], tiles = "Stamen Terrain")

map.add_child(folium.Marker())

map.save("Mapa2.html")