import streamlit as st
import folium
from streamlit_folium import st_folium
import os

st.set_page_config(layout="wide")


with st.sidebar:
    st.subheader('MAPA DE ARTON')
    
map_path = 'https://i.redd.it/acgreznsj1671.jpg'

m = folium.Map(width=3229, height=2166,                
           tiles= map_path,
           #tiles='https://cartocdn-gusc.global.ssl.fastly.net//ramirocartodb/api/v1/map/named/tpl_756aec63_3adb_48b6_9d14_331c6cbc47cf/all/{z}/{x}/{y}.png',
           attr='Textures and Icons from https://www.textures.com/ & https://thenounproject.com/')




# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)








