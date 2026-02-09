import pdfplumber

file_path = 'd:/1 Projects/CEFA/04_ESTUDIANTES/admitidos_2026.pdf'

try:
    with pdfplumber.open(file_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
        
        print("--- Extracted Text Preview (First 1000 chars) ---")
        print(full_text[:1000])
        print("\n--- Total Length ---")
        print(len(full_text))
        
        # Simple extraction attempt assuming line based
        lines = full_text.split('\n')
        print("\n--- First 20 Lines ---")
        for i, line in enumerate(lines[:20]):
            print(f"{i}: {line}")

except Exception as e:
    print(f"Error: {e}")
