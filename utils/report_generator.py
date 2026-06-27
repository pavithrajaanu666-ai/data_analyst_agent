from fpdf import FPDF


class PDFReport(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, 'Automated Data Analysis Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


def build_pdf_report(insights_text, output_path="reports/text/data_report.pdf"):
    """Compiles insights into a simple structural PDF file."""
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font('helvetica', '', 12)

    for line in insights_text.split('\n'):
        pdf.cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'), 0, 1)

    pdf.output(output_path)
    return output_path