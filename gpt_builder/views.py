from django.shortcuts import render
from g4f.client import Client
from details.models import Contact, Education, Experience, Skills, Jobs
import json

def test(request, job_id):

    client = Client()
    job = json.dumps(Jobs.objects.filter(pk=job_id)[0].__repr__())
    contact_list = json.dumps([Contact.objects.filter(owner=request.user.id)[0].__repr__()])
    skills_list = [elem.__repr__() for elem in Skills.objects.filter(owner=request.user.id)]
    educ_list = [elem.__repr__() for elem in Education.objects.filter(owner=request.user.id).order_by('start_date')]
    exp_list = [elem.__repr__() for elem in Experience.objects.filter(owner=request.user.id).order_by('start_date')]

    string = 'Contact Details: '.join(contact_list) + 'Skills: ' + json.dumps(skills_list, default=str) + 'Education: ' + json.dumps(educ_list, default=str) + 'Experience ' + json.dumps(exp_list, default=str)
    
    # jd = 'We are seeking a talented and passionate Software Engineer to join our dynamic team. The Software Engineer will play a key role in designing, developing, and maintaining high-quality software solutions that meet the needs of our customers and contribute to the success of our products. The ideal candidate is highly skilled in programming languages, has a strong understanding of software development methodologies, and is driven to deliver results in a fast-paced environment. Key Responsibilities: Collaborate with cross-functional teams to define software requirements and develop technical solutions that align with business objectives. Design, develop, test, and deploy software applications and features using best practices and industry standards. Write clean, efficient, and maintainable code, following coding standards and guidelines. Participate in code reviews, debugging sessions, and troubleshooting efforts to identify and resolve issues. Stay updated on emerging technologies and trends in software development, and proactively contribute ideas for improving processes and technologies. Work closely with product managers, designers, and other stakeholders to ensure the successful delivery of software projects on time and within budget. Provide technical guidance and mentorship to junior engineers, fostering a culture of learning and growth within the team.'
    # qual = 'Bachelors degree in computer science, software engineering, or related field; advanced degree preferred. 5+ years of experience in software development, with proficiency in Java. Solid understanding of software development methodologies, such as Agile or Scrum, and experience working in an agile environment. Strong problem-solving skills and ability to think creatively to overcome technical challenges. Excellent communication and interpersonal skills, with the ability to effectively collaborate with team members and stakeholders. Demonstrated ability to manage multiple projects and priorities simultaneously, while maintaining attention to detail.'
    prompt = 'Given the job description and qualifications as follows: ' + job + ', write a custom resume using the following data: ' + string + ' that will land an interview for this job. Return in HTML format. Each work experience should have at least 3 bullets. Include keywords from the description and qualifications. Make sure to reword experiences to make them sound like the the requiremenrs from job description. Only give html code, nothing else in the response.'
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    res = response.choices[0].message.content[7:]
    res = res[:-3]

    # import re

    # res = re.search('```html(.*)```', res)
    # res = res.group(1)

    return render(request, 'gpt_builder/show_res.html', {'res': res})

# Create your views here.
