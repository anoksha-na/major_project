import pyttsx3
from bs4 import BeautifulSoup

def read_html_content(html_file_path):
    """Extract text content from an HTML file."""
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Extract the report text from the <p> tag with id 'report'
        report_text = soup.find('p', id='report').get_text()
    return report_text

def read_out_report(report_text):
    """Read out loud the content provided in report_text."""
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Check if report_text is empty
    if not report_text:
        report_text = "The report text is empty or could not be read."

    # Read out the content
    engine.say(report_text)
    engine.runAndWait()

def read_out_report_from_html(html_file_path):
    """Extract text from an HTML file and read it out loud."""
    # Get the content from the HTML
    report_text = read_html_content(html_file_path)
    # Read out the report text
    read_out_report(report_text)

# Usage example
html_file_path = "C:/Users/Ananya/Desktop/major_prjct/templates/result.html"  # Adjust the path as needed
read_out_report_from_html(html_file_path)