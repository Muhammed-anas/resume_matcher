                                                           Resume Matcher

tech stack: Django, Html, Css
Api Tools used : ollamma, model:"llama3.2"
virtual env : UV (insted of pip for faster installing packages)


sync the package with uv : uv sync
run the model : cd backend && python manage.py runserver

Backend server:http://127.0.0.1:8000/
api server: http://localhost:11434/api/generate


This project is about comapring the two inputs to get the desired results,
Its focus on comparing resume text by a job seekers with an actual job descriptions.

Egs case:

        if resume_text is :"experienced Python developer with Django and Rest Api Skills..."
        job description is :"Looking for Python developer with experience in Django, Rest Apis and react,"


this is two input written by user, and it is written with help of Django forms by crispy forms



and egs result will be:
            "match_score": 0-100,
            "missing_skills": [missed skills],
            "summary": "brief summary"




1.AI approach i used, why i choose it ?

->
The approach is why iam used becuase of it's making large language models (LLMs) easy to run locally on personal machines

I used ollama api tool for my project beacuase it makes large language models (LLMs) accessible, private, and easy to run locally on personal computers.
the model i used for this project is "llama3.2" it is one of the best model by ollamma




2.one alternative approach 

->
Another alternative approach is used restframework for connecting the apps like linkedin, indeed with api, extract the job description data for job seekers,
it often useful for job seekers to match their skill to understand which skill are they lacking. 


3.one limitation

->

the main limitaion of my project is my model "llama3.2" (Meta AI) is designed for small projects, Highly competitive with similar-sized models, good for on-device and local tasks,it often give wrong answers like may fail when trying to call tools, sometimes getting stuck in a loop or failing to provide a text response for simple inputs.
i used this model it work low  ram system, But if you have high ram system use gemma 2 (Google),it  Designed for high performance and efficiency, with the 2B model surpassing many GPT-3.5 models.





4.improvement idea or next step enhancement

-> 
as i mention earlier, my first improvement will be updating the model, or used chatgpt with api key for better results.
next step enhancement will be updating ui with modern laguage like react and connecting both backend to frontend with restframework.
and also implement login and signup page.

last step will hosted the website , comapnies would often useful for matching the required skills and missed skills, eliminated lack skilled employee,
and can hiring very fastly with this website , it can help to save time 


        