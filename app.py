import streamlit as st
import pandas as pd
import openpyxl as oppy

# Título de la aplicación
st.title('Cargar y leer archivos Vehicles y Costumers')

# Subir el archivo de Vehicles
uploaded_file1 = st.file_uploader("Carga el archivo Excel de Vehicles", type=["xlsx", "xls"])

# Subir el archivo de Costumers
uploaded_file2 = st.file_uploader("Carga el archivo Excel de Costumers", type=["xlsx", "xls"])

# Verificar si ambos archivos han sido cargados
if uploaded_file1 is not None and uploaded_file2 is not None:
    # Leer los archivos Excel
    df_vehicles = pd.read_excel(uploaded_file1)
    df_costumers = pd.read_excel(uploaded_file2)
    
    # Mostrar la información del archivo de Vehicles
    st.write("Contenido del archivo de Vehicles:")
    st.dataframe(df_vehicles)

    # Asegurarnos que tiene las columnas correctas
    expected_columns_vehicles = ['Referencia', 'Año', 'Cilindraje', 'Comprador']
    if all(col in df_vehicles.columns for col in expected_columns_vehicles):
        st.success("El archivo de Vehicles tiene las columnas correctas.")
    else:
        st.error(f"El archivo de Vehicles debe tener las siguientes columnas: {expected_columns_vehicles}")
    
    # Mostrar la información del archivo de Costumers
    st.write("Contenido del archivo de Costumers:")
    st.dataframe(df_costumers)

    # Asegurarnos que tiene las columnas correctas
    expected_columns_costumers = ['Nombre', 'Cedula', 'Correo', 'Telefono', 'Vehiculo']
    if all(col in df_costumers.columns for col in expected_columns_costumers):
        st.success("El archivo de Costumers tiene las columnas correctas.")
    else:
        st.error(f"El archivo de Costumers debe tener las siguientes columnas: {expected_columns_costumers}")

else:
    st.write("Por favor, carga ambos archivos Excel.")
