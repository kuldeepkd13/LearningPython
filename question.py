employees = [
    {"name":"John" , "skills": ["Python" , "Database"] , "current_project":None},
    {"name":"Emma" , "skills": ["Java" , "Teasting"] , "current_project":None},
    {"name":"Kelly" , "skills": ["Python" , "Java"] , "current_project":None}
]

projects = [
    {"name" :  "Project A" , "required_skills": ["Python" , "Database"] },
    {"name" :  "Project B" , "required_skills": ["Java" , "Teasting"]  },
    {"name" :  "Project C" , "required_skills": ["Python" , "Java"] }
]

def allocated_project(emps , projects):
    li = []
    for employee in emps:
        for project in projects:
            if employee['skills']== project['required_skills']:
                dic = {
                    "employee":employee['name'],
                    "project":project['name']
                }
                li.append(dic)
    return li


result = allocated_project(employees,projects)
print(result)