from pypdf import PdfReader,PdfWriter

reader = PdfReader("sample.pdf")

writer = PdfWriter()

writer.add_page(reader.pages[0])

with open("new_sample.pdf", "wb") as file:
    writer.write(file)

print("PDF extracted Successfully")

print("Total Pages:", len(reader.pages))

with open("sample_pdf_text.txt", "w", encoding="utf-8") as file:
    for page in reader.pages:
        text = page.extract_text()
        file.write(text)
        file.write("\n")
print("PDF text saved Successfully")