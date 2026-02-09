import pandas as pd

try:
    file_path = 'd:/1 Projects/CEFA/04_ESTUDIANTES/lista_seleccionados.xlsx'
    # Skip first 3 rows as header is on row 4 (index 3)
    df = pd.read_excel(file_path, header=3)
    
    # Filter out empty rows if any
    df = df.dropna(subset=['Nombres'])
    
    print(f"Total Students: {len(df)}")
    print("\n--- Universities ---")
    print(df['Universidad'].value_counts())
    
    print("\n--- Names ---")
    print(df['Nombres'].tolist())
except Exception as e:
    print(f"Error: {e}")
