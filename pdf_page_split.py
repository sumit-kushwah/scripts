pdf_path = "/home/sumit/Downloads/the-giver.pdf"

from pypdf import PdfWriter, PdfReader

reader = PdfReader(pdf_path)
writer = PdfWriter()

for i in range(reader._get_num_pages()):
    page = reader.pages[i]
    original_right = page.mediabox.top
    page.mediabox.upper_right = (page.mediabox.right, page.mediabox.top / 2)
    writer.add_page(page)
    page.mediabox.upper_right = (page.mediabox.right, original_right)
    page.mediabox.lower_left = (0, page.mediabox.top / 2)
    writer.add_page(page)

with open("pypdf-output.pdf", "wb") as fp:
    writer.write(fp)
