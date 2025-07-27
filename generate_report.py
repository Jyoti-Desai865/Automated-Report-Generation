import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

def read_data(file_path):
    """Reads data from a CSV file."""
    return pd.read_csv(file_path)

def analyze_data(data):
    """Performs basic data analysis and returns summary statistics."""
    return data.describe(include='all')

def generate_pdf_report(summary_df, output_file):
    """Generates a formatted PDF report from summary DataFrame."""
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("📊 Automated Data Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # Description
    elements.append(Paragraph("This report summarizes the key statistics of the provided dataset.", styles['BodyText']))
    elements.append(Spacer(1, 12))

    # Table header
    summary_df = summary_df.round(2)  # Round for better readability
    table_data = [ [ "Metric" ] + list(summary_df.columns) ]
    for index, row in summary_df.iterrows():
        table_data.append([index] + list(row))

    # Create table
    table = Table(table_data, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    print(f"PDF report generated: {output_file}")


if __name__ == "__main__":
    input_file = "data.csv"           
    output_pdf = "sample_report.pdf"  

    data = read_data(input_file)
    summary = analyze_data(data)
    generate_pdf_report(summary, output_pdf)
