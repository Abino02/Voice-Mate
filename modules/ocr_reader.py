"""
OCR Reader Module
Handles Image and PDF to Text conversion using OCR
"""

import os
from datetime import datetime
import pytesseract
from PIL import Image
import PyPDF2
import pdfplumber


class OCRReader:
    """Handles OCR operations for images and PDFs."""
    
    def __init__(self):
        """Initialize OCR Reader."""
        # Set Tesseract path for Windows (update if needed)
        # Uncomment and modify if Tesseract is not in PATH
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        self.output_dir = os.path.join("data", "output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def extract_from_file(self, file_path):
        """
        Extract text from image or PDF file.
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            str: Extracted text or error message
        """
        if not os.path.exists(file_path):
            return "Error: File not found!"
        
        file_ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if file_ext == '.pdf':
                return self._extract_from_pdf(file_path)
            elif file_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']:
                return self._extract_from_image(file_path)
            else:
                return f"Error: Unsupported file format '{file_ext}'\nSupported formats: JPG, PNG, BMP, TIFF, GIF, PDF"
        except Exception as e:
            return f"Error during extraction: {str(e)}"
    
    def _extract_from_image(self, image_path):
        """
        Extract text from image using Tesseract OCR.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            str: Extracted text
        """
        try:
            # Open image
            image = Image.open(image_path)
            
            # Extract text using pytesseract
            text = pytesseract.image_to_string(image, lang='eng')
            
            if not text.strip():
                return "No text found in the image.\nTips:\n- Ensure the image has clear, readable text\n- Check if the image quality is good\n- Try a different image"
            
            # Save to file
            output_file = self._save_text(text, "image_ocr")
            
            result = f"✅ Text extracted successfully from image!\n\n"
            result += f"📄 Saved to: {output_file}\n\n"
            result += "=" * 50 + "\n"
            result += "EXTRACTED TEXT:\n"
            result += "=" * 50 + "\n\n"
            result += text
            
            return result
            
        except pytesseract.TesseractNotFoundError:
            return ("Error: Tesseract is not installed or not in PATH!\n\n"
                   "Please install Tesseract-OCR:\n"
                   "Windows: https://github.com/UB-Mannheim/tesseract/wiki\n"
                   "Linux: sudo apt install tesseract-ocr\n"
                   "Mac: brew install tesseract")
        except Exception as e:
            return f"Error extracting text from image: {str(e)}"
    
    def _extract_from_pdf(self, pdf_path):
        """
        Extract text from PDF using multiple methods.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text
        """
        text = ""
        method_used = ""
        
        # Try pdfplumber first (better for complex PDFs)
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n--- Page {page_num} ---\n{page_text}\n"
                method_used = "pdfplumber"
        except Exception as e:
            print(f"pdfplumber failed: {e}")
        
        # If pdfplumber didn't work, try PyPDF2
        if not text.strip():
            try:
                with open(pdf_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    num_pages = len(pdf_reader.pages)
                    
                    for page_num in range(num_pages):
                        page = pdf_reader.pages[page_num]
                        page_text = page.extract_text()
                        if page_text:
                            text += f"\n--- Page {page_num + 1} ---\n{page_text}\n"
                    method_used = "PyPDF2"
            except Exception as e:
                return f"Error extracting text from PDF: {str(e)}"
        
        if not text.strip():
            return ("No text found in the PDF.\n\n"
                   "Possible reasons:\n"
                   "- PDF contains only images (scanned document)\n"
                   "- PDF is encrypted or protected\n"
                   "- PDF uses unsupported encoding\n\n"
                   "Tip: For scanned PDFs, convert pages to images first, then use Image OCR.")
        
        # Save to file
        output_file = self._save_text(text, "pdf_extract")
        
        result = f"✅ Text extracted successfully from PDF!\n\n"
        result += f"📄 Method used: {method_used}\n"
        result += f"📄 Saved to: {output_file}\n\n"
        result += "=" * 50 + "\n"
        result += "EXTRACTED TEXT:\n"
        result += "=" * 50 + "\n"
        result += text
        
        return result
    
    def _save_text(self, text, prefix):
        """
        Save extracted text to a file.
        
        Args:
            text (str): Text to save
            prefix (str): Prefix for filename
            
        Returns:
            str: Path to saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{timestamp}.txt"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        
        return filepath


# Test function
if __name__ == "__main__":
    ocr = OCRReader()
    print("OCR Reader module loaded successfully!")
    print(f"Output directory: {ocr.output_dir}")
