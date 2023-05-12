import PyPDF2
from pathlib import Path


merger = PyPDF2.PdfMerger()
file_names = ["rotated.pdf", "rotated2.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")




















# path = Path("C:\\Users\\91962\\Downloads\\SAJHRMLowincomeworkers.pdf")


# with open(path, "rb")as file:
#     reader = PyPDF2.PdfReader(file)
#     # print(len(reader.pages))
#     Page = reader.pages[5]
#     Page.rotate(90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(Page)
#     with open('rotated2.pdf', "wb") as output:
#         writer.write(output)

