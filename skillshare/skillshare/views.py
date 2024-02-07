
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .clean_data import process_data
import csv
import os

# View for hello.html
def say_hello(request):
    return render(request, 'hello.html')

# View for IForm.html
def iform(request):
    return render(request, 'IForm.html')

# View for SForm.html
def sform(request):
    return render(request, 'SForm.html')



def clean_data(request):
    if request.method == 'POST':
        # Call the data processing function
        jobs, candidates = process_data()

        # Save the processed dataframes to CSV files
        jobs.to_csv('data/processed_jobs.csv', index=False)
        candidates.to_csv('data/processed_candidates.csv', index=False)

        return HttpResponse('Data processed successfully')
    else:
        # Handle GET requests (e.g., render a template with the button)
        return render(request, 'process_data.html')



#Function to get user input and populate the candidates csv in the data folder
def submit_student(request):
    if request.method == 'POST':
        fullname = request.POST.get('Fullname', '')
        course = request.POST.get('Course', '')
        score = request.POST.get('Score', '')
        experience = request.POST.get('Experience', '')
        study_mode = request.POST.get('StudyMode', '')
        study_pattern = request.POST.get('StudyPattern', '')

        csv_content = f"{fullname},{course},{score},{experience},{study_mode},{study_pattern}\n"

        file_path = '/home/shaun/SkillPilot/Ibr/DjangoSkeleton/skillshare/data/candidates.csv'

        with open(file_path, 'a') as file:
            if os.path.getsize(file_path) == 0:
                file.write("Fullname,Course,Score,Experience,StudyMode,StudyPattern\n")
            file.write(csv_content)

       
        return HttpResponse('Form submitted')
    else:
        return render(request, 'your_template.html')


#Function to get user input and populate the jobs csv in the data folder
def submit_job(request):
    if request.method == 'POST':
        title = request.POST.get('Title', '')
        company = request.POST.get('Company', '')
        field = request.POST.get('Field', '')
        min_score = request.POST.get('MinScore', '')
        positions = request.POST.get('Positions', '')

        csv_content = f"{title},{company},{field},{min_score},{positions}\n"

        file_path = '/home/shaun/SkillPilot/Ibr/DjangoSkeleton/skillshare/data/jobs.csv'

        with open(file_path, 'a') as file:
            if os.path.getsize(file_path) == 0:
                file.write("Title,Company,Field,MinScore,Experience,Positions\n")
            file.write(csv_content)

        return HttpResponse('Form submitted')
    else:
     
        return render(request, 'your_template.html')
