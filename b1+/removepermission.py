from PyPDF2 import PdfReader, PdfWriter

input_path = "Kont_B1+Express_KB_Loesungen_final.pdf"
output_path = "1_Kont_B1+Express_KB_Loesungen_final.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

# Copy all pages
for page in reader.pages:
    writer.add_page(page)

# Write to new file (no encryption)
with open(output_path, "wb") as f:
    writer.write(f)

print(f"✅ Permissions removed. Saved as {output_path}")
