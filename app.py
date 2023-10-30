from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate, get_candidate_by_name, get_candidate_by_skill

app = Flask(__name__)

@app.route('/')
def all_candidates():
    candidates_array = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates_array=candidates_array)

@app.route('/candidate/<int:x>')
def one_candidate(x):
    candidate = get_candidate(x)
    return render_template('index.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def candidates_by_name(candidate_name):
    candidates_array = get_candidate_by_name(candidate_name)
    return render_template('search.html', candidate_name=candidates_array)

@app.route('/skill/<skill_name>')
def candidates_by_skill(skill_name):
    candidates_array = get_candidate_by_skill(skill_name)
    return render_template('skill.html', candidate_skill=candidates_array, skill = skill_name)





app.run()