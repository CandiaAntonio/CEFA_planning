import pdfplumber

file_path = 'd:/1 Projects/CEFA/04_ESTUDIANTES/admitidos_2026.pdf'

try:
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words()
            # Sort by top (y) then x
            words.sort(key=lambda w: (int(w['top']), w['x0']))
            
            print(f"--- Page 1 Words (Sorted) ---")
            current_top = -1
            line_text = []
            
            for word in words:
                # Group by line (approximate y)
                if current_top == -1:
                    current_top = word['top']
                
                if abs(word['top'] - current_top) > 5: # New line threshold
                    print(" ".join(line_text))
                    line_text = []
                    current_top = word['top']
                
                line_text.append(word['text'])
            
            if line_text:
                print(" ".join(line_text))

except Exception as e:
    print(f"Error: {e}")
