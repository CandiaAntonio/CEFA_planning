import pandas as pd

try:
    file_path = 'd:/1 Projects/CEFA/04_ESTUDIANTES/lista_seleccionados.xlsx'
    df = pd.read_excel(file_path)
    print("Columns:", df.columns.tolist())
    print("First 5 rows:")
    print(df.head())
    print("Shape:", df.shape)
except Exception as e:
    print(f"Error reading Excel file: {e}")
