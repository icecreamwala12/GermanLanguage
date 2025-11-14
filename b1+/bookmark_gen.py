from PyPDF2 import PdfReader, PdfWriter
name="1_UB.pdf"
reader = PdfReader(name)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# add bookmarks (page numbers starts from zero)
writer.add_outline_item("Präteritum", 3)
writer.add_outline_item("Plusquamperfekt", 4)
writer.add_outline_item("Dativ oder Akkusativ", 6)



with open(name, "wb") as f:
    writer.write(f)
