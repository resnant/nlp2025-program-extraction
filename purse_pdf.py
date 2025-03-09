# %%
import pymupdf

doc = pymupdf.open("NLP-2025/pdf_dir/A1-1.pdf") # open a document
out = open("output.txt", "wb")
# %%
for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()