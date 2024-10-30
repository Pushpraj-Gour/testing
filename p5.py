from pptx import Presentation
from pptx.util import Pt

def create_ppt_from_data(data, pptx_file_name):
    # Create a presentation object
    presentation = Presentation()
    
    def add_slide(pres, title, content=None):
        """Helper function to add a slide with title and optional content."""
        slide_layout = pres.slide_layouts[1]  # Title and Content layout
        slide = pres.slides.add_slide(slide_layout)
        
        # Add title
        slide_title = slide.shapes.title
        slide_title.text = title
        
        if content:
            content_placeholder = slide.shapes.placeholders[1]  # Placeholder for content
            text_frame = content_placeholder.text_frame
            
            # Create a single paragraph for the content
            paragraph = text_frame.add_paragraph()  # Create the first paragraph for the content
            add_content_to_slide(paragraph, content)

    def add_content_to_slide(paragraph, content):
        """Recursive function to add bullet points, paragraphs, and nested data to a given paragraph."""
        if isinstance(content, str):
        
            paragraph.text += content + "\n" 
        elif isinstance(content, dict):
    
            for key, value in content.items():
           
                paragraph.text += key + "\n" 
                
                # Recursively handle nested content
                add_content_to_slide(paragraph, value)
        elif isinstance(content, list):
           
            for item in content:
                if isinstance(item, dict):
               
                    for key, value in item.items():
                        paragraph.text += key + "\n" 
                        add_content_to_slide(paragraph, value)
                else:
            
                    paragraph.text += str(item) + "\n" 

    # Iterate over the data structure to create slides
    for section_title, section_content in data.items():
    
        add_slide(presentation, section_title, section_content)


    presentation.save(pptx_file_name)
    print(f"Presentation '{pptx_file_name}' created successfully!")

data = {
    "Title Slide": {
        "Subtitle": "This is an example of a generic data-driven PPT",
    },
    "Section 1": {
        "Introduction": "This is an introductory section",
        "Details": {
            "Point 1": "Description of point 1",
            "Point 2": "Description of point 2",
            "Nested List": ["Item A", "Item B", "Item C"]
        }
    },
    "Section 2": {
        "Summary": "This section contains a summary.",
        "Points": [
            {"Subsection 1": "Subsection 1 details"},
            {"Subsection 2": "Subsection 2 details"}
        ]
    },
    "Conclusion": "This is the conclusion of the presentation."
}

# Call the function with the data
create_ppt_from_data(data, "output.pptx")
