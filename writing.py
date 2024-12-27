import fitz  # PyMuPDF
from bs4 import BeautifulSoup

# PDF path
pdf_file_path = "C:/Users/Ananya/Desktop/pdf_check/lung_condition_report.pdf"
# HTML output file path
html_file_path = "C:/Users/Ananya/Desktop/pdf_check/result.html"

def extract_text_from_pdf(pdf_path):
    """Extracts text content from each page of a PDF file."""
    text_content = ""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            text_content += page.get_text()
    return text_content

def format_text_for_html(text_content):
    """Formats the extracted text into structured HTML sections."""
    # Split by full stops and new lines
    sentences = [sentence.strip() for sentence in text_content.replace('.', '.\n').splitlines() if sentence.strip()]

    structured_content = {
        "report": "",
        "info": "",
        "recommendations": ""
    }

    current_section = None
    for line in sentences:
        if "Report:" in line:
            current_section = "report"
        elif "Info:" in line:
            current_section = "info"
        elif "Recommendations:" in line:
            current_section = "recommendations"
        
        # Add the line to the corresponding section with a line break
        if current_section:
            structured_content[current_section] += line + "<br>"

    formatted_html = ""
    for section, content in structured_content.items():
        if content:
            formatted_html += f"<h3>{section.capitalize()}</h3><p>{content}</p>"

    return formatted_html 

def write_to_html_file(html_content, html_path):
    """Writes the HTML content to an output file."""
    # Create basic HTML structure using BeautifulSoup
    soup = BeautifulSoup("<html><head><title>Lung Condition Report</title></head><body></body></html>", "html.parser")
    
    # Add formatted report content
    body = soup.body
    body.append(BeautifulSoup(html_content, "html.parser"))
    
    # Write the full HTML structure to file
    with open(html_path, "w", encoding="utf-8") as file:
        file.write(str(soup))

# Extract content from PDF
pdf_text_content = extract_text_from_pdf(pdf_file_path)

# Format the extracted text into structured HTML
html_content = format_text_for_html(pdf_text_content)

# Write the HTML content to file
write_to_html_file(html_content, html_file_path)

print(f"Report content has been written to {html_file_path}")