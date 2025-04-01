import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
# from app.worker import celery_app


# Set up Jinja2 environment with optimized caching
jinja_env = Environment(
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
            # templates.append(f"report_{category}.html")
            templates.append(f"report{category}.html")
    else:
        templates = ["report1.html", "report2.html", "report3.html"]

    return templates



# @celery_app.task(bind=True)
# def generate_pdf_task(self, file_path, output_filename):
def generate_pdf_task(file_path, output_filename):
    df = pd.read_excel(file_path)
    data = df.to_dict(orient="records")
    print(data)

    ''' 
    # templates = select_templates(data)  # Dynamically select templates
    # pdf_pages = []

    # for template_name in templates:
    #     template = jinja_env.get_template(template_name)
    #     html_content = template.render(data=data)

    #     # Convert HTML to PDF page
    #     pdf_page = HTML(string=html_content, base_url="").write_pdf()
    #     # pdf_page = HTML(string=html_content, base_url=html_content.build_absolute_uri()).write_pdf()
    #     # pdf_page = HTML(string=html_content, base_url=self.request.build_absolute_uri()).write_pdf()
    #     pdf_pages.append(pdf_page)
    '''

    template_1 = jinja_env.get_template(f"report1.html")
    # # # template_2 = jinja_env.get_template(f"report_2.html")
    # # template_3 = jinja_env.get_template(f"report_3.html")
    html_content1 = template_1.render(data=data)
    # # # html_content2 = template_2.render(data=data)
    # # html_content3 = template_3.render()

    # # # Convert HTML to PDF page
    pdf_page_1 = HTML(string=html_content1, base_url="").write_pdf()
    # # # pdf_page_2 = HTML(string=html_content2, base_url="").write_pdf()
    # # pdf_page_3 = HTML(string=html_content3, base_url="").write_pdf()

    # # pdf_pages = [pdf_page_1, pdf_page_3]


    # Merge PDFs
    # final_pdf = b"".join(pdf_page)
    # final_pdf = b"".join(pdf_pages)

    with open(output_filename, "wb") as f:
        f.write(pdf_page_1)
        # f.write(pdf_page_1)

    os.remove(file_path)
    return output_filename
