import folium

gps_file = "gps.log"

def gps_entry_list(filename):
    with open(filename, 'r') as gps:
        gps_entry_list = gps.read().split('\n\n')
    point_dict_list = []
    for index, entry in enumerate(gps_entry_list):
        data_fields = entry.split('\n')
        data_string = ''
        for field in data_fields:
            if field != '':
                data_string += field
                if index < len(gps_entry_list) - 1:
                    data_string += '\n'
        if data_string != '':
            fieldo = data_string.split('\n')
            date = fieldo[0].split(' ')[0]
            time = fieldo[0].split(' ')[1]
            lat = fieldo[1].split(' ')[1]
            long = fieldo[2].split(' ')[1]
            speed = fieldo[4].split(' ')[1]
            point_dict = {'date': date, 'time': time, 'lat': float(lat), 'long': float(long), 'speed': float(speed)}
            point_dict_list.append(point_dict)
    return point_dict_list

data = gps_entry_list(gps_file)

m = folium.Map(location=(data[0].get("lat"), data[0].get("long")), zoom_start=15)
for index, point in enumerate(data):
    folium.Marker(
        location=(point.get('lat'), point.get('long')),
        tooltip=f"Point {index+1}",
        popup=f"Date: {point.get('date')}\nTime: {point.get('time')}\nLat: {point.get('lat')}\nLong: {point.get('long')}\nSpeed: {point.get('speed')}"
        ).add_to(m)

folium.PolyLine([(p["lat"], p["long"]) for p in data], color="blue", weight=2.5).add_to(m)
m.save("gps_path_map.html")
print("Map saved to gps_path_map.html")