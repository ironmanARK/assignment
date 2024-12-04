import pandas as pd
d=pd.read_csv('C:\\Users\\gaksh\\Downloads\\student_records.csv')
d.drop_duplicates()
grade_to_point={
    'AP':10,
    'AA':10,
    'AB':9,
    'BB':8,
    'BC':7,
    'CC':6,
    'CD':5,
    'DD':4,
    'DE':3,
    'EE':2,
    'EF':1,
}
d['grades to point']=d['grade'].map(grade_to_point)
d['total credits']=d['credit']*d['grades to point']
core_courses=d[d['course_type'] == 'core'].groupby('roll_number')['total credits'].sum()
department_electives = d[d['course_type'] == 'department_elective'].groupby('roll_number')['total credits'].sum()
flexible_electives = d[d['course_type'] == 'flexible_elective'].groupby('roll_number')['total credits'].sum()
hasmed_electives = d[d['course_type'] == 'hasmed_elective'].groupby('roll_number')['total credits'].sum()
graduation=core_courses[core_courses>=20].index.intersection(department_electives[department_electives>=15].index).intersection(
flexible_electives[flexible_electives>=10].index).intersection(hasmed_electives[hasmed_electives>=5].index)
print(graduation)

