import pdfplumber

file_path = 'd:/1 Projects/CEFA/04_ESTUDIANTES/admitidos_2026.pdf'

try:
    with pdfplumber.open(file_path) as pdf:
        print(f"Total Pages: {len(pdf.pages)}")
        for i, page in enumerate(pdf.pages):
            print(f"--- Page {i+1} Tables ---")
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    for row in table:
                        print(row)
            else:
                print("No tables found. Trying raw text density...")
                # Fallback: check chars
                # words = page.extract_words()
                # for word in words[:20]:
                #    print(word)
                
except Exception as e:
    print(f"Error: {e}")
