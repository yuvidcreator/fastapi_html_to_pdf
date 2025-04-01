from weasyprint import HTML, CSS



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