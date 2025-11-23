from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
import os

def export_pdf(csv_file, pdf_file, title):
    df = pd.read_csv(csv_file)
    data = [df.columns.tolist()] + df.values.tolist()

    os.makedirs("report", exist_ok=True)
    doc = SimpleDocTemplate(pdf_file)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph(title, styles['Title']))

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    ]))

    elements.append(table)
    doc.build(elements)
    print(f"[PDF saved] {pdf_file}")
