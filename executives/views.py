from django.shortcuts import render, redirect
from .forms import EvaluationForm, DirectorateForm
from django.contrib import messages





def executives_page(request):

  return render(request, "executives/executives_page.html")


def evaluation_form(request):
  if request.method == 'POST':
    form = EvaluationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.info(request, 'Your form has been submitted successfully.')
      return redirect('application_submit')

  
  form = EvaluationForm()


  context = {
    "form" : form
  }
  return render(request, "executives/evaluation_form.html", context)


def directorate_form(request):
  if request.method == 'POST':
    form = DirectorateForm(request.POST)
    if form.is_valid():
      form.save()
      messages.info(request, 'Your form has been submitted successfully.')
      return redirect('application_submit')

  
  form = DirectorateForm()


  context = {
    "form" : form
  }
  return render(request, "executives/directorate_form.html", context)


def application_submit(request):
  
  return render(request, 'executives/application_submit.html')