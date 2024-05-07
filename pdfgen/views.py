from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter
from details.models import Contact
import io 
from django.contrib.auth.models import User

# Create your views here.

def create_pdf(request):

    # Set the page height and width
    # HEIGHT = 11 * inch
    # WIDTH = 8.5 * inch

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    contacts = Contact.objects.filter(owner=request.user.id)

    # my_dict = {
    #     'name': str(User.first_name) + ' ' + str(User.last_name),
    #     'contact': {
    #         'phone': str(contact.phone), 
    #         'linkedin': str(contact.linkedin)
    #     }
    # }

    # c.saveState()  # save the current state
    # c.setFont('Helvetica', 16)  # set the font for the name
    # c.drawString(.4 * inch, HEIGHT - (.4 * inch), my_dict['name'])  # draw the name on top left page 1
    # c.setFont('Helvetica', 8)  # sets the font for contact
    # c.drawRightString(WIDTH - (.4 * inch), HEIGHT - (.4 * inch), my_dict['contact']['linkedin'])  
    # c.line(.4 * inch, HEIGHT - (.47 * inch), WIDTH - (.4 * inch), HEIGHT - (.47 * inch))
    # c.drawString(.4 * inch, HEIGHT - (.6 * inch), my_dict['contact']['phone'])

    lines = []

    for contact in contacts: 
        lines.append(contact.phone)
        lines.append(contact.linkedin)
        lines.append(contact.website)
        lines.append(contact.address)
        lines.append(' ')

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment='test.pdf')



