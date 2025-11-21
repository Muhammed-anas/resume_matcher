from django.shortcuts import render
from .forms import ResumeMatchForm
from .ai_utils import ollama_analyze

def resume_matcher(request):
    form = ResumeMatchForm()      
    result = None                

    if request.method == "POST":
        form = ResumeMatchForm(request.POST)
        if form.is_valid():
            resume = form.cleaned_data["resume_text"]
            job = form.cleaned_data["job_description"]
            result = ollama_analyze(resume, job)

    return render(request, "home.html", {
        "form": form,
        "result": result
    })
