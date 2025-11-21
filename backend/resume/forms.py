from django import forms


class ResumeMatchForm(forms.Form):
    resume_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows':5, 'placeholder':'Paste resume text)'}),
        label='Resume text'
    )
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows':5, 'placeholder':'job description)'}),
        label='Job description'
    )

