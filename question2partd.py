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
minor= d[d['course_type'] == 'minor']
students=minor[minor['total credits']>=10]
print(students)

