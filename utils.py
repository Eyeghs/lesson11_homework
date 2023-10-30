import json

def load_candidates_from_json(path):
    # Открыть файл в режиме чтения
    with open(path, 'r') as json_file:
        # Загрузить данные из JSON файла
        data = json.load(json_file)
    return data

def get_candidate(candidate_id):
    candidates_array = load_candidates_from_json('candidates.json')
    for candidate in candidates_array:
        if candidate['id'] == candidate_id:
            return candidate

def get_candidate_by_name(candidate_name):
    candidates_array = load_candidates_from_json('candidates.json')
    candidates_by_name = []
    for candidate in candidates_array:
        if candidate['name'] == candidate_name:
            candidates_by_name.append(candidate)
    return candidates_by_name

def get_candidate_by_skill(skill_name):
    candidates_array = load_candidates_from_json('candidates.json')
    candidates_by_skills = []
    for candidate in candidates_array:
        if skill_name in candidate['skills'] or skill_name.title() in candidate['skills']:
            candidates_by_skills.append(candidate)
    return candidates_by_skills


