import fitz  # PyMuPDF


def extract_internal_hyperlinks_with_context(pdf_file_path, page_number):
    hyperlinks = []

    # Open the PDF file
    document = fitz.open(pdf_file_path)

    # Check if the specified page exists
    if page_number - 1 < len(document):
        page = document[page_number - 1]

        # Get the links on the page
        for link in page.get_links():
            if link.get('kind') == fitz.LINK_GOTO:  # Check if it's an internal link
                dest_page_number = link.get('page') + 1  # Convert to 1-based index
                rect = link.get('from')  # Get the rectangle coordinates of the link

                # Extract text in the rectangle area around the link
                text_within_rect = page.get_text("text", clip=rect)

                # Extract text nearby the link (e.g., within a certain range)
                nearby_text = page.get_text("text",
                                            clip=fitz.Rect(rect.x0 - 50, rect.y0 - 20, rect.x1 + 50, rect.y1 + 20))

                # Combine the text to provide context
                context_text = nearby_text.strip()  # Get nearby text
                hyperlinks.append((f"Page {dest_page_number}", text_within_rect.strip(), context_text))

    document.close()  # Close the document
    return hyperlinks


# Define the PDF file path and the page number
pdf_file_path = 'jnj_2023.pdf'  # Replace with your PDF file path
page_number = 3  # Change to the desired page number

# Call the function and print the extracted internal hyperlinks
internal_hyperlinks = extract_internal_hyperlinks_with_context(pdf_file_path, page_number)
for link, link_text, context in internal_hyperlinks:
    print(f'Link: {link}\nLink Text: {link_text}\nContext: {context}\n')
