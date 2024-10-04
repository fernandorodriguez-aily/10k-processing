import requests
from pypdf import PdfReader

# Download the PDF from the URL (if running locally)
# APPL 10-k 2023
url = "https://s2.q4cdn.com/470004039/files/doc_earnings/2023/q4/filing/_10-K-Q4-2023-As-Filed.pdf"
pdf_file_path = "appl_2023.pdf"

# JNJ 10-k 2023
url = "https://d18rn0p25nwr6d.cloudfront.net/CIK-0000200406/2d8bead4-a89a-4802-8c63-1266ad78e6a2.pdf"
pdf_file_path = "jnj_2023.pdf"

# Download and save the PDF
response = requests.get(url)
with open(pdf_file_path, 'wb') as f:
    f.write(response.content)

# Open the downloaded PDF
reader = PdfReader(pdf_file_path)

# Function to extract all bookmarks and their page numbers
def list_bookmarks(bookmarks, parent_title=""):
    bookmark_list = []
    for outline in bookmarks:
        if isinstance(outline, list):
            # Handle nested bookmarks recursively
            bookmark_list.extend(list_bookmarks(outline, parent_title))
        else:
            title = outline.title
            page = reader.get_destination_page_number(outline)
            bookmark_list.append((parent_title + title, page + 1))  # Page is 0-indexed, so +1
    return bookmark_list

# Extracting bookmarks
if reader.outline:
    bookmarks = list_bookmarks(reader.outline)

    # Printing the bookmarks and their corresponding pages
    print("Bookmarks and their corresponding pages:")
    for title, page in bookmarks:
        print(f"'{title}' -> Page {page}")
else:
    print("No bookmarks found in the PDF.")
