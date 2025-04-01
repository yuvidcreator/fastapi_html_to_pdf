import os
# from io import BytesIO
# import json
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from app.helper.utils import print_file_size
from app.worker import celery_app




# Set up Jinja2 environment with optimized caching
env = Environment(
    loader=FileSystemLoader("templates"),
    auto_reload=False,  # Disable in production
    cache_size=1000  # Cache up to 1000 templates
)

# Function to select templates dynamically
def select_templates(data):
    templates = []
    if "category" in data[0]:  
        categories = set(item["category"] for item in data)
        for category in categories:
            templates.append(f"report_{category}.html")
    else:
        templates = ["report1.html", "report2.html", "report3.html"]

    return templates


def html_to_pdf(html_content, options=None) -> str:
    # Create the HTML object
    html = HTML(string=html_content, base_url="")

    try:
        css_options = f"""
            @page {{
                size: {options.get('page-size', 'A4')};
                margin-top: {options.get('margin-top', '40mm')};
                margin-right: {options.get('margin-right', '0mm')};
                margin-bottom: {options.get('margin-bottom', '0mm')};
                margin-left: {options.get('margin-left', '0mm')};
            }}
        """
        # Add custom CSS to the HTML content
        css = CSS(string=css_options)
        html.write_pdf(stylesheets=[css])
        return html
    except Exception as e:
        print(f"{e}")



@celery_app.task(bind=True)
def generate_pdf_task(self, file_path, output_filename):
    df = pd.read_excel(file_path)
    data = df.to_dict(orient="records")
    print(data)
    templates = select_templates(data)  # Dynamically select templates
    pdf_pages = []

    for template_name in templates:
        template = env.get_template(template_name)
        html_content = template.render(data=data)

        # Convert HTML to PDF page
        pdf_page = HTML(string=html_content, base_url="").write_pdf()
        # pdf_page = HTML(string=html_content, base_url=html_content.build_absolute_uri()).write_pdf()
        # pdf_page = HTML(string=html_content, base_url=self.request.build_absolute_uri()).write_pdf()
        pdf_pages.append(pdf_page)

    # Merge PDFs
    final_pdf = b"".join(pdf_pages)

    with open(output_filename, "wb") as f:
        f.write(final_pdf)
        print_file_size(f)

    os.remove(file_path)
    return output_filename
