This is a simple python projecvt which uses the concepts of pandas and folium to extract volcano data from a csv file and show it on a website map 

folium: This is a python library used to print out maps on a HTML sheet and has functions to manipulate the dom of the map depending on the location(longitude and latitude )
    *Geojson : type of file ehch tells whats closer to the viewer

pandas: This is a python library used to read large set of datas. pandas is a more suitable way of reading categorised datasets or files like csvs,excels etc... it has builtin module to help navigate through the data and get the things that are absolutely needed. The most intresting fact about using pandas over traditional file reading system is that as the file grows larger the reading becomes more energy consuming 


What has been done in this project is using felium we have created a map with the logitude and latitude of that of the USA and using pandas we extract the data of the volcanoes location using its lang and lats and mark it on the map depending on its Height.


""" To run This project clone it open it in the terminal and run 
python3 map.py
or 
python map.py
