from ast import Or
from django.shortcuts import redirect, render
from django.http import HttpResponse, FileResponse
from .models import assessment, submission
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SubmissionForm, Grading, AssessmentForm





def is_student(user):
  return user.groups.filter(name='Student').exists()
def is_mentor(user):
  return user.groups.filter(name='Mentor').exists()
def is_admin(user):
  return user.groups.filter(name='Admin').exists()

@login_required 
def index(request):
  if request.user.groups.all()[0].name == "Admin":
    return redirect('/login')
  elif request.user.groups.all()[0].name == "Mentor":
    return redirect(mentor)
  else:
    return redirect(student)




@user_passes_test(is_mentor)
def mentor(request):
  name = request.user.get_full_name()
  submissions = list(submission.objects.all())
  if request.method == 'POST':
    form = AssessmentForm(request.POST)
    if form.is_valid():
      Assessment = form.save()
  context = {
    'name': name,
    'submissions':submissions,
    'assessment': AssessmentForm()
  }
  return render(request, 'mentor.html', context)


@user_passes_test(is_mentor)
def Change_Sub(request,id):
  submissions = submission.objects.get(id=id)
  if request.method == 'POST':
    form = Grading(request.POST, instance=submissions)
    if form.is_valid():
      form.save()
      return redirect(mentor)
  context = {
    'form' : Grading()
  }
  return render(request, 'Change_Sub.html', context)

@user_passes_test(is_student)
def student(request):
  name = request.user.get_full_name()
  assessments = list(assessment.objects.all())
  if request.method == 'POST':
    form = SubmissionForm(request.POST, request.FILES, initial={'StudentName': request.user.get_full_name})
    if form.is_valid():
      submission = form.save()
  context = {
    'name': name,
    'assessment':assessments,
    'form' : SubmissionForm(initial={'StudentName': request.user.get_full_name})
  }
  return render(request, 'student.html', context)


