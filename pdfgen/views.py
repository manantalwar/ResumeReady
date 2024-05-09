from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter
from details.models import Contact, Experience, Education
import io 
from django.contrib.auth.models import User

# Create your views here.

# def create_pdf(request):

    # buf = io.BytesIO()
    # c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # textob = c.beginText()
    # textob.setTextOrigin(inch, inch)
    # textob.setFont('Helvetica', 14)

    # contacts = Contact.objects.filter(owner=request.user.id)
    # experiences = Experience.objects.filter(owner=request.user.id)
    # education = Education.objects.filter(owner=request.user.id)


    # lines = []

    # for contact in contacts: 
    #     lines.append(contact.phone)
    #     lines.append(contact.linkedin)
    #     lines.append(contact.website)
    #     lines.append(contact.address)
    
    # for exp in experiences:
    #     lines.append(exp.role)
    #     lines.append(exp.company)
    #     lines.append(str(exp.start_date))
    #     lines.append(str(exp.end_date))
    #     lines.append(exp.description)

    # for line in lines:
    #     textob.textLine(line)

    # c.drawText(textob)
    # c.showPage()
    # c.save()
    # buf.seek(0)
    # return FileResponse(buf, as_attachment='test.pdf')

import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.http import FileResponse
from details.models import Contact, Experience, Education


def create_pdf(request):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)

    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    heading_style = styles['Heading1']

    # Fetch data from models
    contacts = Contact.objects.filter(owner=request.user.id)
    experiences = Experience.objects.filter(owner=request.user.id)
    education = Education.objects.filter(owner=request.user.id)

    # Initialize Story
    story = []

    # Add Contact Information
    for contact in contacts:
        contact_info = [
            Paragraph(f"<b>Phone:</b> {contact.phone} | <b>LinkedIn:</b> {contact.linkedin} | <b>Website:</b> {contact.website} | <b>Address:</b> {contact.address}", normal_style),
            # Paragraph(f"<b>LinkedIn:</b> {contact.linkedin}", normal_style),
            # Paragraph(f"<b>Website:</b> {contact.website}", normal_style),
            # Paragraph(f"<b>Address:</b> {contact.address}", normal_style),
            Spacer(1, 12)
        ]
        story.extend(contact_info)

    # Add Experiences
    exp_data = []
    for exp in experiences:
        exp_info = [
            # [Paragraph("<b>Role:</b>", heading_style), Paragraph(exp.role, normal_style)],
            # [Paragraph("<b>Company:</b>", heading_style), Paragraph(exp.company, normal_style)],
            # [Paragraph("<b>Start Date:</b>", heading_style), Paragraph(exp.start_date.strftime("%b %Y"), normal_style)],
            # [Paragraph("<b>End Date:</b>", heading_style), Paragraph(exp.end_date.strftime("%b %Y") if exp.end_date else "Present", normal_style)],
            # [Paragraph("<b>Description:</b>", heading_style), Paragraph(exp.description, normal_style)]
            [Paragraph(exp.role, normal_style)],
            [Paragraph(exp.company, normal_style)],
            [Paragraph(exp.start_date.strftime("%b %Y"), normal_style), Paragraph(exp.end_date.strftime("%b %Y") if exp.end_date else "Present", normal_style)],
            [Paragraph(exp.description, normal_style, bulletText='-')]
        ]
   
        exp_data.extend(exp_info)
        exp_data.append(["", ""])  # Add spacing between experiences


    exp_table = Table(exp_data, colWidths=[400, 100])
    exp_table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')]))

    story.append(Paragraph("<b>Experience</b>", normal_style))
    story.append(exp_table)
    story.append(Spacer(1, 12))

    # Add Education
    edu_data = []
    for edu in education:
        edu_info = [
            [Paragraph("<b>Institution:</b>", heading_style), Paragraph(edu.institution, normal_style)],
            [Paragraph("<b>Degree:</b>", heading_style), Paragraph(edu.degree, normal_style)],
            [Paragraph("<b>Field of Study:</b>", heading_style), Paragraph(edu.major, normal_style)],
            [Paragraph("<b>Start Date:</b>", heading_style), Paragraph(edu.start_date.strftime("%b %Y"), normal_style)],
            [Paragraph("<b>End Date:</b>", heading_style), Paragraph(edu.end_date.strftime("%b %Y") if edu.end_date else "Present", normal_style)]
        ]
        edu_data.extend(edu_info)
        edu_data.append(["", ""])  # Add spacing between educations

    edu_table = Table(edu_data, colWidths=[100, 400])
    edu_table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')]))

    story.append(Paragraph("<b>Education</b>", heading_style))
    story.append(edu_table)

    doc.build(story)
    buf.seek(0)
    return FileResponse(buf, as_attachment='resume.pdf')
