def read_file(file_name):
    yearbook = {}
    with open(file_name, 'r') as f:
        current_student = ""
        for line in f:
            if line.strip() == "":
                continue
            if ":" in line:
                current_student = line.strip().replace(":", "")
                yearbook[current_student] = {}
            else:
                name, signature = line.strip().split(",")
                yearbook[current_student][name.strip()] = int(signature.strip())
    return yearbook

def find_max_min_signatures(yearbook):
    max_signatures = []
    min_signatures = []
    max_count = 0
    min_count = float('inf')
    for student in yearbook:
        signature_count = sum(yearbook[student].values())
        if signature_count > max_count:
            max_count = signature_count
            max_signatures = [student]
        elif signature_count == max_count:
            max_signatures.append(student)
        if signature_count < min_count:
            min_count = signature_count
            min_signatures = [student]
        elif signature_count == min_count:
            min_signatures.append(student)
    return max_signatures, min_signatures

yearbook = read_file("yearbook.txt")
max_signatures, min_signatures = find_max_min_signatures(yearbook)
print("Students with most signatures:", max_signatures)
print("Students with least signatures:", min_signatures)

import os
if os.path.exists('yearbook.txt'):
    yearbook = read_file("yearbook.txt")
else:
    print("yearbook.txt not found in the current directory")
