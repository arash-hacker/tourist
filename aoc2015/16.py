import re
import math
f=open("16.txt")
line_re = re.compile(r"^Sue (\d+): (.*)")


standard = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}   

def load_input(input):
    profiles = {}
    for line in input.splitlines():
        m = line_re.match(line)
        if m:
            number = int(m.group(1))
            profile = {}
            for item in m.group(2).split(", "):
                name, count = item.split(": ")
                profile[name] = int(count)
            profiles[number] = profile
        elif len(line) > 0:
            raise Exception("Unable to parse line '{}'".format(line))
    return profiles

def score_profile(profile, standard):
    score = 0
    for k, v in profile.items():
        if k in ('cats', 'trees'):
            if v <= standard[k]:
                score += 10.0
        elif k in ('pomeranians', 'goldfish'):
            if v >= standard[k]:
                score += 10.0
        else:
            score += math.pow(v - standard[k], 2)
    return score

profiles=load_input(f.read())



# print(profiles)
scores = []
for num in sorted(profiles.keys()):
    score = score_profile(profiles[num], standard)
    scores.append((score, num))
    # print ("{:03d}: {} ## {}".format(num, score, ", ".join(["{}: {}".format(k, v)
            # for k, v in profiles[num].items()])))
print( "Part 1")

scores.sort()
print(  len(set([k for k,v in  scores]) )  )
# for score, num in scores[:10]:
#     print ("{:03d}: {} ## {}".format(num, score, ", ".join(["{}: {}".format(k, v)
#         for k, v in profiles[num].items()])))