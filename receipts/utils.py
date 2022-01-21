from io import BytesIO

from xhtml2pdf import pisa


def convert_html_to_pdf(source_html):
    io_bytes = BytesIO()
    pisa_status = pisa.CreatePDF(BytesIO(source_html.encode("UTF-8")), io_bytes)
    return pisa_status, io_bytes
