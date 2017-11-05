import folium

m = folium.Map([41.9901466,-87.6620448], tiles = "cartodbpositron",
               zoom_start = 13, max_zoom = 14, min_zoom = 6, attr = "")

colormap = folium.LinearColormap(("orange", "white", "purple"),
                                 vmin = 70, vmax = 100,
                                 caption = "Percent of Families Poverty")
colormap.add_to(m)

folium.GeoJson(merged_df,
    style_function = lambda feature: { 
      'fillColor': colormap(feature['properties']["Poverty Rate"]) 
                    if feature["properties"]["Poverty Rate"] else "k",
      "color" : "k", "weight" : 0.3, 
      "fillOpacity" : 0.4 if feature["properties"]["Poverty Rate"] else 0,
    }).add_to(m)

m.save_html("Poverty Rate")


