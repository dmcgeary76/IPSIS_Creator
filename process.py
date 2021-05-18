import pandas as pd
import numpy as np
import zipfile
from datetime import date, datetime

doc_path = 'BrightspaceISD.xlsx'
aca_year = '2021'
ucode = 'BSD'
headers = ['type','action','code','name','start_date','end_date','is_active','department_code','template_code','semester_code','offering_code','custom_code']
temp_list = [['temp_elem','Brightspace Elementary Template'],['MS_Temp','MS Temp'],['HS_Temp','HS Temp']]
grades_list  = [['K','1','2','3','4','5'],['6','7','8'],['9','10','11','12']]


def update_dept(headers):
    dept = []
    dept.append(headers)
    dept.append(['department','UPDATE','elemc','Test Department','','','','','','','',''])
    df = pd.DataFrame(dept)
    df.to_csv('1-Department.csv', header=False, index=False, sep=',')


def create_district(doc_path, temp_list, grades_list, headers):
    course_index = []
    WS = pd.read_excel(doc_path)
    WS_np = np.array(WS)
    district_list = list(WS_np[0])
    district_data = []
    district_data.append('District')
    district_data.append('CREATE')
    district_data.append(aca_year + ucode + 'D_FY_' + str(district_list[1]).replace(' ','_'))
    district_data.append(str(district_list[1]))
    district_code = aca_year + ucode + 'D_FY_' + str(district_list[1]).replace(' ','_')
    district_data = district_data + ['','']
    district_data.append('1')
    district_data = district_data + ['','','','']
    district_list.append('6606')
    district = [headers, district_data]
    df = pd.DataFrame(district)
    df.to_csv('1-District.csv', header=False, index=False, sep=',')
    create_schools(district_code, doc_path, temp_list, grades_list, headers)
    course_index = create_schools(district_code, doc_path, temp_list, grades_list, headers)
    return course_index


def create_schools(district_code, doc_path, temp_list, grades_list, headers):
    schools_list = []
    course_index = []
    WS = pd.read_excel(doc_path)
    WS_np = np.array(WS)
    temp = []
    for item in WS_np:
        temp.append(list(item))
    temp.pop(0)
    temp.pop(0)
    temp.pop(0)
    for item in temp:
        if item[3] not in schools_list:
            schools_list.append([item[3],item[4]])
    schools = [[]]
    schools[0] = headers
    school_codes = []
    for school in schools_list:
        schools.append(['School','CREATE',aca_year + ucode + 'S-FY'+school[0].replace(' ','_'),school[0],'','',1,'','','','',district_code])
        school.append(aca_year + ucode + 'S-FY'+school[0].replace(' ','_'))
        df = pd.DataFrame(schools)
        df.to_csv('2-Schools.csv', header=False, index=False, sep=',')
    update_templates(temp_list, schools_list, grades_list, headers)
    course_index = update_templates(temp_list, schools_list, grades_list, headers)
    return course_index


def create_semester(aca_year, headers):
    semester = []
    semester.append(headers)
    semester.append(['semester','CREATE',aca_year + ucode + '_AY_Sem','AY ' + aca_year,'','','','','','','',''])
    df = pd.DataFrame(semester)
    df.to_csv('3-Semester.csv', header=False, index=False, sep=',')
    sem_code = aca_year + ucode + '_AY_Sem'
    return sem_code


def update_templates(temp_list, schools_list, grades_list, headers):
    templates = []
    course_index = []
    templates.append(headers)
    schools = []
    for school in schools_list:
        if school not in schools:
            schools.append(school)
    for school in schools:
        if school[1] == 'Elementary':
            templates.append(['course template','UPDATE',temp_list[0][0],temp_list[0][1],'','','',school[2],'','','',''])
        if school[1] == 'Middle':
            templates.append(['course template','UPDATE',temp_list[1][0],temp_list[1][1],'','','',school[2],'','','',''])
        if school[1] == 'High':
            templates.append(['course template','UPDATE',temp_list[2][0],temp_list[2][1],'','','',school[2],'','','',''])
    df = pd.DataFrame(templates)
    df.to_csv('4-Templates.csv', header=False, index=False, sep=',')
    create_offerings(temp_list, schools_list, grades_list, headers)
    course_index = create_offerings(temp_list, schools_list, grades_list, headers)
    return course_index



def create_offerings(temp_list, schools_list, grades_list, headers):
    offerings = []
    course_index = []
    offerings.append(headers)
    temp = []
    sem_code = create_semester(aca_year, headers)
    for school in schools_list:
        if school not in temp:
            temp.append(school)
    for school in temp:
        holder = school[2]
        if school[1] == 'Elementary':
            for level in grades_list[0]:
                offerings.append(['course offering','CREATE',school[0].replace(' ','_') + '_' + level,school[0] + ' - Grade ' + level,'','','1','',temp_list[0][0],sem_code,'',holder])
        if school[1] == 'Middle':
            for level in grades_list[1]:
                offerings.append(['course offering','CREATE',school[0].replace(' ','_') + '_' + level,school[0] + ' - Grade ' + level,'','','1','',temp_list[1][0],sem_code,'',holder])
        if school[1] == "High":
            for level in grades_list[2]:
                offerings.append(['course offering','CREATE',school[0].replace(' ','_') + '_' + level,school[0] + ' - Grade ' + level,'','','1','',temp_list[2][0],sem_code,'',holder])
    df = pd.DataFrame(offerings)
    for offering in offerings[1:]:
        try:
            off_code = offering[3].split(' - ')[1].split(' ')[1]
            off_name = offering[3].split(' - ')[0]
            course_index.append([off_name, off_code, offering[2], offering[11]])
        except:
            print('offering has a value not in the list range.')
    df.to_csv('5-Offerings.csv', header=False, index=False, sep=',')
    return course_index

def create_users():
    users = []
    headers = ['type','action','username','org_defined_id','first_name','last_name','password','is_active','role_name','email','relationships','pref_first_name','pref_last_name']
    WS = pd.read_excel(doc_path)
    WS_np = np.array(WS)
    user_list = list(WS_np)
    user_list.pop(0)
    user_list.pop(0)
    user_list.pop(0)
    users.append(headers)
    for user in user_list:
        users.append(['user','CREATE',user[2],user[2],user[0],user[1],'demos123!','1',user[5],user[2],'','',''])
    df = pd.DataFrame(users)
    df.to_csv('6-Users.csv', header=False, index=False, sep=',')
    return user_list


def create_enrollments(users, course_index):
    enrollments = []
    headers = ['type','action','child_code','role_name','parent_code']
    enrollments.append(headers)
    for user in users:
        user_grades = str(user[6]).split(',')
        for grade in user_grades:
            for course in course_index:
                print('course is: ' + course[1] + ' and ' 'grade is ' + grade)
                if course[1] == grade:
                    enrollments.append(['enrollment','CREATE',user[2],user[8],course[2]])
    df = pd.DataFrame(enrollments)
    df.to_csv('7-Enrollments.csv', header=False, index=False, sep=',')


def main():
    course_index = []
    users = []
    update_dept(headers)
    create_semester(aca_year, headers)
    create_district(doc_path, temp_list, grades_list, headers)
    course_index = create_district(doc_path, temp_list, grades_list, headers)
    create_users()
    users = create_users()
    create_enrollments(users, course_index)
    this_day = str(date.today())
    now = datetime.now()
    ct = str(now.strftime("%H:%M:%S").replace(':',''))
    zft = this_day + '-' + ct + '_' + ucode +'_IPSIS.zip'
    zf = zipfile.ZipFile(zft, mode='w')
    try:
        zf.write('manifest.json')
        zf.write('1-Department.csv')
        zf.write('1-District.csv')
        zf.write('2-Schools.csv')
        zf.write('3-Semester.csv')
        zf.write('4-Templates.csv')
        zf.write('5-Offerings.csv')
        zf.write('6-Users.csv')
        zf.write('7-Enrollments.csv')
    finally:
        zf.close()
