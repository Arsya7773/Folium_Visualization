#impor modul
import pandas as pd
import folium

#read data csv
data_batas = pd.read_csv("Data/Batas_Kecamatan_Jatinangor.csv")
data_depotminyak = pd.read_csv("Data/DEPOTMINYAK_PT.csv")
data_jembatan = pd.read_csv("Data/JEMBATAN.csv")
data_kesehatan = pd.read_csv("Data/KESEHATAN.csv")
data_pemerintahan = pd.read_csv("Data/PEMERINTAHAN.csv")
data_pendidikan = pd.read_csv("Data/PENDIDIKAN.csv")

#buat map
allmap = folium.Map(location=[float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])], zoom_start=13)
map_depotminyak = folium.Map(location=[float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])], zoom_start=13)
map_Jembatan = folium.Map(location=[float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])], zoom_start=13) 
map_genlistrik = folium.Map(location=[float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])], zoom_start=13)
map_kesehatan = folium.Map(location=[float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])], zoom_start=13)
map_pipaminyak = folium.Map(location=[float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])], zoom_start=13)
map_pemerintahan = folium.Map(location=[float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])], zoom_start=13)
map_pendidikan = folium.Map(location=[float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])], zoom_start=13)

#inisiasi list
koordinat_batas = []
nama_pemerintahan = ["Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Camat 9", "Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Kepala Desa", "Kantor Kepala Desa"]

#ambil koordinat dari data
for x in range(len(data_batas)):
    koordinat_batas.append([float(data_batas["Latitude"][x]), float(data_batas["Longitude"][x])])

#ambil koordinat untuk menghubungkan garis
koordinat_batas.append([float(data_batas["Latitude"][0]), float(data_batas["Longitude"][0])])

#visualisasi garis batas kecamatan jatinangor pada peta
garis_batas = folium.PolyLine(locations=koordinat_batas, color="yellow", opacity=0.3, fill=True, fill_color='yellow', fill_opacity=0.3)
garis_batas_depotminyak = folium.PolyLine(locations=koordinat_batas, color="yellow", opacity=0.3, fill=True, fill_color='yellow', fill_opacity=0.3)
garis_batas_Jembatan = folium.PolyLine(locations=koordinat_batas, color="yellow", opacity=0.3, fill=True, fill_color='yellow', fill_opacity=0.3)
garis_batas_genlistrik = folium.PolyLine(locations=koordinat_batas, color="yellow", opacity=0.3, fill=True, fill_color='yellow', fill_opacity=0.3)
garis_batas_kesehatan = folium.PolyLine(locations=koordinat_batas, color="yellow", opacity=0.3, fill=True, fill_color='yellow', fill_opacity=0.3)
garis_batas_pipaminyak = folium.PolyLine(locations=koordinat_batas, color="yellow", opacity=0.3, fill=True, fill_color='yellow', fill_opacity=0.3)
garis_batas_pemerintahan = folium.PolyLine(locations=koordinat_batas, color="yellow", opacity=0.3, fill=True, fill_color='yellow', fill_opacity=0.3)
garis_batas_pendidikan = folium.PolyLine(locations=koordinat_batas, color="yellow", opacity=0.3, fill=True, fill_color='yellow', fill_opacity=0.3)

#visualisasi depot minyak pada peta
for x in range(len(data_depotminyak)):
    folium.Marker(location=[float(data_depotminyak["Latitude"][x]), float(data_depotminyak["Longitude"][x])], popup = data_depotminyak["Nama"][x], icon=folium.Icon(color="blue", icon="info-sign")).add_to(allmap)
    folium.Marker(location=[float(data_depotminyak["Latitude"][x]), float(data_depotminyak["Longitude"][x])], popup = data_depotminyak["Nama"][x], icon=folium.Icon(color="blue", icon="info-sign")).add_to(map_depotminyak)

#visualisasi jembatan pada peta
for x in range(len(data_jembatan)):
    folium.Marker(location=[float(data_jembatan["Latitude"][x]), float(data_jembatan["Longitude"][x])], popup = data_jembatan["Nama"][x], icon=folium.Icon(color="orange", icon="info-sign")).add_to(allmap)
    folium.Marker(location=[float(data_jembatan ["Latitude"][x]), float(data_jembatan["Longitude"][x])], popup = data_jembatan["Nama"][x], icon=folium.Icon(color="orange", icon="info-sign")).add_to(map_Jembatan)

#visualisasi generator listrik pada peta
folium.Marker(location=[-6.94939, 107.78483], popup = "Generator Listrik", icon=folium.Icon(color="pink", icon="info-sign")).add_to(allmap)
folium.Marker(location=[-6.94939, 107.78483], popup = "Generator Listrik", icon=folium.Icon(color="pink", icon="info-sign")).add_to(map_genlistrik)

#visualisasi pipa minyak pada peta
pipaminyak1 = folium.PolyLine(locations=[[-6.92810, 107.78757], [-6.92816, 107.78744]], popup = "Pipa Minyak", color="red", opacity=1, weight=10)
pipaminyak2 = folium.PolyLine(locations=[[-6.93683, 107.78622], [-6.93689, 107.78625]], popup = "Pipa Minyak", color="red", opacity=1, weight=10)
pipaminyak3 = folium.PolyLine(locations=[[-6.93673, 107.78617], [-6.93683, 107.78622]], popup = "Pipa Minyak",color="red", opacity=1, weight=10)
pipaminyak1_copy = folium.PolyLine(locations=[[-6.92810, 107.78757], [-6.92816, 107.78744]], popup = "Pipa Minyak", color="red", opacity=1, weight=10)
pipaminyak2_copy = folium.PolyLine(locations=[[-6.93683, 107.78622], [-6.93689, 107.78625]], popup = "Pipa Minyak", color="red", opacity=1, weight=10)
pipaminyak3_copy = folium.PolyLine(locations=[[-6.93673, 107.78617], [-6.93683, 107.78622]], popup = "Pipa Minyak", color="red", opacity=1, weight=10)

#visualisasi sarana kesehatan pada peta
for x in range(len(data_kesehatan)):
    folium.Marker(location=[float(data_kesehatan["Latitude"][x]), float(data_kesehatan["Longitude"][x])], popup = data_kesehatan["Nama"][x], icon=folium.Icon(color="purple", icon="info-sign")).add_to(allmap)
    folium.Marker(location=[float(data_kesehatan["Latitude"][x]), float(data_kesehatan["Longitude"][x])], popup = data_kesehatan["Nama"][x], icon=folium.Icon(color="purple", icon="info-sign")).add_to(map_kesehatan)

#visualisasi sarana pemerintahan pada peta
for x in range(len(data_pemerintahan)):
    folium.Marker(location=[float(data_pemerintahan["Latitude"][x]), float(data_pemerintahan["Longitude"][x])], popup = nama_pemerintahan[x], icon=folium.Icon(color="darkblue", icon="info-sign")).add_to(allmap)
    folium.Marker(location=[float(data_pemerintahan["Latitude"][x]), float(data_pemerintahan["Longitude"][x])], popup = nama_pemerintahan[x], icon=folium.Icon(color="darkblue", icon="info-sign")).add_to(map_pemerintahan)

#visualisasi sarana pendidikan pada peta
for x in range(len(data_pendidikan)):
    folium.Marker(location=[float(data_pendidikan["Latitude"][x]), float(data_pendidikan["Longitude"][x])], popup = data_pendidikan["Nama"][x], icon=folium.Icon(color="black", icon="info-sign")).add_to(allmap)
    folium.Marker(location=[float(data_pendidikan["Latitude"][x]), float(data_pendidikan["Longitude"][x])], popup = data_pendidikan["Nama"][x], icon=folium.Icon(color="black", icon="info-sign")).add_to(map_pendidikan)

#masukkan garis ke peta
garis_batas.add_to(allmap)
garis_batas_depotminyak.add_to(map_depotminyak)
garis_batas_Jembatan.add_to(map_Jembatan)
garis_batas_genlistrik.add_to(map_genlistrik)
garis_batas_kesehatan.add_to(map_kesehatan)
garis_batas_pipaminyak.add_to(map_pipaminyak)
garis_batas_pemerintahan.add_to(map_pemerintahan)
garis_batas_pendidikan.add_to(map_pendidikan)

#masukkan pipa minyak pada peta
pipaminyak1.add_to(allmap)
pipaminyak2.add_to(allmap)
pipaminyak3.add_to(allmap)
pipaminyak1_copy.add_to(map_pipaminyak)
pipaminyak2_copy.add_to(map_pipaminyak)
pipaminyak3_copy.add_to(map_pipaminyak)

#simpan data ke peta dalam website HTML
allmap.save("Allmap.html")
map_depotminyak.save("map_Depotminyak.html")
map_Jembatan.save("map_Jembatan.html")
map_genlistrik.save("map_Genlistrik.html")
map_kesehatan.save("map_Kesehatan.html")
map_pipaminyak.save("map_pipaminyak.html")
map_pemerintahan.save("map_pemerintahan.html")
map_pendidikan.save("map_pendidikan.html")