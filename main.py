import PyPDF2

# pdf merger


# take input pdf path from user 
pdf_path1 = input("Enter Path to pdf 1 : ")
pdf_path2 = input("Enter Path to pdf 2 : ")
new_pdf = input("Enter New Merge pdf Name : ")

pdfiles = [pdf_path1, pdf_path2]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write(f"{new_pdf}.pdf")
print("pdf merge successfully")


