import json
import re
import requests

def ollama_analyze(resume_text, job_description):

    prompt = f"""
You MUST return only JSON.
show the missing skills from job_desription comparing to resume_text, give about the summary
JSON FORMAT:
{{
  "match_score": 0,
  "missing_skills": [],
  "summary": ""
}}

RESUME: {resume_text}
JOB: {job_description}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )
    except Exception as e:
        return {
            "match_score": 0,
            "missing_skills": [],
            "summary": f"Ollama connection error: {e}"
        }


    try:
        raw = response.json().get("response", "")
    except:
        return {
            "match_score": 0,
            "missing_skills": [],
            "summary": "Ollama returned invalid response"
        }

    if not raw.strip():
        return {
            "match_score": 0,
            "missing_skills": [],
            "summary": "Empty response from model"
        }

 
    json_match = re.search(r"\{(?:[^{}]|(?:\{[^{}]*\}))*\}", raw, re.DOTALL)
    if not json_match:
        return {
            "match_score": 0,
            "missing_skills": [],
            "summary": "Model did not return JSON: " + raw[:120]
        }

    json_text = json_match.group(0)

 
    try:
        return json.loads(json_text)
    except:
        return {
            "match_score": 0,
            "missing_skills": [],
            "summary": "JSON parsing failed: " + json_text[:120]
        }
