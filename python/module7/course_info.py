# program that let users see requested course information

course_room_info = {
    "CSC101":"3004",
    "CSC102":"4501",
    "CSC103":"6755",
    "NET110":"1244",
    "COM241":"1411"
}

course_instructors_info = {
    "CSC101":"Haynes",
    "CSC102":"Alvarado",
    "CSC103":"Rich",
    "NET110":"Burke",
    "COM241":"Lee"
}

course_time_info = {
    "CSC101":"8:00 a.m.",
    "CSC102":"9:00 a.m.",
    "CSC103":"10:00 a.m.",
    "NET110":"11:00 a.m.",
    "COM241":"1:00 p.m."
}


course_input = input('Enter the course number\n')

if (course_input in course_room_info):
    print('Your requested course is in room',course_room_info[course_input])
    print('Your requested course is instructed by',course_instructors_info[course_input])
    print('Your requested course is at time',course_time_info[course_input])
else:
    print('Invalid course number')