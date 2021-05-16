import re


def step_1(new_id):
    return new_id.lower()


def step_2(new_id):
    return ''.join(re.findall('\w|\.|_|-', new_id))


def step_3(new_id):
    while True:
        if re.search('\.\.', new_id):
            new_id = re.sub('\.\.', '.', new_id)
        else:
            break
    return new_id


def step_4(new_id):
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    if new_id.startswith('.'):
        new_id = new_id[1:]
    return new_id


def step_5(new_id):
    if new_id == "":
        new_id = "a"
    return new_id


def step_6(new_id):
    new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    return new_id


def step_7(new_id):
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id


def solution(new_id):
    answer = step_1(new_id)
    answer = step_2(answer)
    answer = step_3(answer)
    answer = step_4(answer)
    answer = step_5(answer)
    answer = step_6(answer)
    answer = step_7(answer)
    return answer
