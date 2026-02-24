from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
import re

# Read the markdown file
with open('FLASK_EXPLANATION.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Create PDF
pdf_file = "FLASK_EXPLANATION.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        rightMargin=0.5*inch, leftMargin=0.5*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

# Container for PDF elements
story = []

# Define styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#34495e'),
    spaceAfter=10,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=11,
    alignment=TA_JUSTIFY,
    spaceAfter=8,
    leading=14
)

code_style = ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=9,
    fontName='Courier',
    backgroundColor=colors.HexColor('#f0f0f0'),
    textColor=colors.HexColor('#333333'),
    leftIndent=10,
    rightIndent=10,
    spaceAfter=8,
    leading=11
)

# Split content into lines
lines = content.split('\n')

i = 0
while i < len(lines):
    line = lines[i]
    
    # Title (# )
    if line.startswith('# ') and not line.startswith('## '):
        title = line[2:].strip()
        story.append(Paragraph(title, title_style))
        story.append(Spacer(1, 0.2*inch))
        i += 1
    
    # Heading (## )
    elif line.startswith('## '):
        heading = line[3:].strip()
        story.append(Paragraph(heading, heading_style))
        i += 1
    
    # Code block
    elif line.strip().startswith('```'):
        code_lines = []
        i += 1
        while i < len(lines) and not lines[i].strip().startswith('```'):
            code_lines.append(lines[i])
            i += 1
        
        code_text = '\n'.join(code_lines).strip()
        if code_text:
            story.append(Spacer(1, 0.1*inch))
            # Split long code into smaller chunks
            for code_chunk in code_text.split('\n'):
                if code_chunk:
                    story.append(Paragraph(code_chunk, code_style))
            story.append(Spacer(1, 0.1*inch))
        i += 1
    
    # Table
    elif line.strip().startswith('|'):
        table_data = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            cells = [cell.strip() for cell in lines[i].split('|')[1:-1]]
            if cells and not all(c.replace('-', '').replace(':', '') == '' for c in cells):
                table_data.append(cells)
            i += 1
        
        if table_data:
            table = Table(table_data, colWidths=[2*inch, 2.5*inch, 2*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 11),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#ddd')),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
            ]))
            story.append(Spacer(1, 0.1*inch))
            story.append(table)
            story.append(Spacer(1, 0.1*inch))
    
    # Empty line or separators
    elif line.strip() == '' or line.strip().startswith('---'):
        story.append(Spacer(1, 0.05*inch))
        i += 1
    
    # Regular text
    elif line.strip():
        story.append(Paragraph(line.strip(), normal_style))
        i += 1
    
    else:
        i += 1

# Build PDF
doc.build(story)
print(f"✓ PDF created successfully: {pdf_file}")
