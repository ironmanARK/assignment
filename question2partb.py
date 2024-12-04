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
students=d.groupby('roll_number')['total credits'].sum()
print(students)
course=d[(d['course_type']=='core') | (d['course_type']=='flexible_elective') | (d['course_type']=='hasmed_elective') | (d['course_type']=='department_elective')] 
tc=(course.groupby('roll_number')['credit'].sum())
cpi=(course.groupby('roll_number')['total credits'].sum())/tc
print(cpi)