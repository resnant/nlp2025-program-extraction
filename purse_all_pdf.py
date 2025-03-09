#!/usr/bin/env python3
import os
import glob
import pymupdf
from tqdm import tqdm

def process_pdf(pdf_path, output_dir):
    """
    Extract text from a PDF and save it as a .txt file in the output directory.
    The text from each page is separated by a form feed (byte 12).
    """
    doc = pymupdf.open(pdf_path)
    base_name = os.path.basename(pdf_path)
    output_file = os.path.join(output_dir, base_name.replace('.pdf', '.txt'))
    with open(output_file, "wb") as out:
        for page in doc:
            text = page.get_text().encode("utf8")
            out.write(text)
            out.write(bytes((12,)))  # form feed as page delimiter
    doc.close()

def main():
    pdf_dir = os.path.join("NLP-2025", "pdf_dir")
    output_dir = os.path.join("NLP-2025", "pursed_text")
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process all PDF files in the pdf_dir directory with a progress bar
    pdf_files = glob.glob(os.path.join(pdf_dir, "*.pdf"))
    for pdf_file in tqdm(pdf_files, desc="Processing PDFs"):
        process_pdf(pdf_file, output_dir)
    print("Processing complete.")

if __name__ == "__main__":
    main()
