from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

a = int(input("How may PDFs do you want to merge: "))

for i in range(0,a):
    name = str(input(f"Enter the PDF {i + 1} file name: "))
    pdfs.append(name)


for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()