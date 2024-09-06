import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Cargar, leer y combinar archivos Excel')

# Subir el archivo de Vehicles
uploaded_file1 = st.file_uploader("Carga el archivo Excel de Vehicles", type=["xlsx", "xls"])

# Subir el archivo de Costumers
uploaded_file2 = st.file_uploader("Carga el archivo Excel de Costumers", type=["xlsx", "xls"])

# Verificar si ambos archivos han sido cargados
if uploaded_file1 is not None and uploaded_file2 is not None:
    # Leer los archivos Excel
    df_vehicles = pd.read_excel(uploaded_file1)
    df_costumers = pd.read_excel(uploaded_file2)
    
    # Mostrar la información de ambos archivos
    st.write("Contenido del archivo de Vehicles:")
    st.dataframe(df_vehicles)
    
    st.write("Contenido del archivo de Costumers:")
    st.dataframe(df_costumers)
    
    # Realizar el merge basado en la columna 'Vehiculo'
    merged_df = pd.merge(df_costumers, df_vehicles, left_on='Vehiculo', right_on='Referencia')
    
    # Mostrar el DataFrame combinado
    st.write("Datos combinados (Costumers y Vehicles):")
    st.dataframe(merged_df)
else:
    st.write("Por favor, carga ambos archivos Excel.")
