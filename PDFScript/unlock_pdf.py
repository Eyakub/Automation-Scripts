import PyPDF2
import sys
import re
from pdf2image import convert_from_path
import os


def unlock_pdf(input_pdf_path, password):
    try:
        # Extract the date from the filename
        output_pdf_path = None
        match = re.search(r'\d{4}_\d{2}_\d{2}', input_pdf_path)
        if match:
            date_str = match.group().replace('_', '-')
            output_pdf_path = f"PB_{date_str}.pdf"

        # Open the encrypted PDF
        with open(input_pdf_path, 'rb') as input_pdf:
            reader = PyPDF2.PdfReader(input_pdf)

            # Check if the PDF is encrypted
            if reader.is_encrypted:
                # Try to decrypt the PDF
                if reader.decrypt(password):
                    writer = PyPDF2.PdfWriter()

                    # Copy all pages to a new PDF writer
                    for page_num in range(len(reader.pages)):
                        writer.add_page(reader.pages[page_num])

                    # Write the unlocked PDF to a new file
                    with open(output_pdf_path, 'wb') as output_pdf:
                        writer.write(output_pdf)

                    print(f"PDF unlocked successfully and saved as '{output_pdf_path}'")

                    # Convert the unlocked PDF to JPG images
                    images = convert_from_path(output_pdf_path)
                    output_dir = f"PB_{date_str}_images"
                    os.makedirs(output_dir, exist_ok=True)
                    
                    for i, image in enumerate(images):
                        image_path = os.path.join(output_dir, f"page_{i + 1}.jpg")
                        image.save(image_path, 'JPEG')

                    print(f"PDF pages saved as JPG images in '{output_dir}'")
                else:
                    print("Incorrect password or unable to decrypt the PDF.")
            else:
                print("The PDF is not encrypted.")
    except FileNotFoundError:
        print(f"File '{input_pdf_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python unlock_pdf.py <directory_path> <password>")
    else:
        directory_path = sys.argv[1]
        password = sys.argv[2]

        # Iterate over all PDF files in the directory
        for filename in os.listdir(directory_path):
            if filename.lower().endswith('.pdf'):
                input_pdf_path = os.path.join(directory_path, filename)
                unlock_pdf(input_pdf_path, password)
