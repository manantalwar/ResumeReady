from django.shortcuts import render
from g4f.client import Client
from details.models import Contact, Education, Experience, Skills, Jobs
import json

# Create your views here.

def view_res(request, job_id):
    client = Client()
    job = json.dumps(Jobs.objects.filter(pk=job_id)[0].__repr__())
    specs = str(Jobs.objects.filter(pk=job_id)[0].specifications) if Jobs.objects.filter(pk=job_id)[0].specifications else ''
    contact_list = json.dumps([Contact.objects.filter(owner=request.user.id)[0].__repr__()])
    skills_list = [elem.__repr__() for elem in Skills.objects.filter(owner=request.user.id)]
    educ_list = [elem.__repr__() for elem in Education.objects.filter(owner=request.user.id).order_by('start_date')]
    exp_list = [elem.__repr__() for elem in Experience.objects.filter(owner=request.user.id).order_by('start_date')]
    string = 'Contact Details: '.join(contact_list) + 'Skills: ' + json.dumps(skills_list, default=str) + 'Education: ' + json.dumps(educ_list, default=str) + 'Experience ' + json.dumps(exp_list, default=str)
    prompt = 'Given the job description and qualifications as follows: ' + job + ', write a custom resume using the following data: ' + string + ' that will land an interview for this job. Return in HTML format. Each work experience should have at least 3 bullets. Include keywords from the description and qualifications. Make sure to reword experiences to make them sound like the the requiremenrs from job description. Only give html code, nothing else in the response.' + specs
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    res = response.choices[0].message.content[7:]
    res = res[:-3]
    return render(request, 'gpt_builder/show_res.html', {'res': res})

