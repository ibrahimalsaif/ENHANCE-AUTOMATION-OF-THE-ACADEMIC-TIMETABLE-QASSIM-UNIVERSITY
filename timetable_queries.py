from models import CoursesTable, InstructorsTable, TimetableTable, session

def CS():
    
    level1_data = session.query(TimetableTable).filter_by(specialty_id=1, level=1).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level1 = []
    for data in level1_data:
        level1.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })

    level2_data = session.query(TimetableTable).filter_by(specialty_id=1, level=2).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level2 = []
    for data in level2_data:
        level2.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })

    level3_data = session.query(TimetableTable).filter_by(specialty_id=1, level=3).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level3 = []
    for data in level3_data:
        level3.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level4_data = session.query(TimetableTable).filter_by(specialty_id=1, level=4).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level4 = []
    for data in level4_data:
        level4.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level5_data = session.query(TimetableTable).filter_by(specialty_id=1, level=5).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level5 = []
    for data in level5_data:
        level5.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level6_data = session.query(TimetableTable).filter_by(specialty_id=1, level=6).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level6 = []
    for data in level6_data:
        level6.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level7_data = session.query(TimetableTable).filter_by(specialty_id=1, level=7).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level7 = []
    for data in level7_data:
        level7.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level8_data = session.query(TimetableTable).filter_by(specialty_id=1, level=8).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level8 = []
    for data in level8_data:
        level8.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    return level1,level2,level3,level4,level5,level6,level7,level8

def COE():
    
    level1_data = session.query(TimetableTable).filter_by(specialty_id=2, level=1).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level1 = []
    for data in level1_data:
        level1.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })

    level2_data = session.query(TimetableTable).filter_by(specialty_id=2, level=2).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level2 = []
    for data in level2_data:
        level2.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })

    level3_data = session.query(TimetableTable).filter_by(specialty_id=2, level=3).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level3 = []
    for data in level3_data:
        level3.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level4_data = session.query(TimetableTable).filter_by(specialty_id=2, level=4).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level4 = []
    for data in level4_data:
        level4.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level5_data = session.query(TimetableTable).filter_by(specialty_id=2, level=5).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level5 = []
    for data in level5_data:
        level5.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level6_data = session.query(TimetableTable).filter_by(specialty_id=2, level=6).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level6 = []
    for data in level6_data:
        level6.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level7_data = session.query(TimetableTable).filter_by(specialty_id=2, level=7).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level7 = []
    for data in level7_data:
        level7.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level8_data = session.query(TimetableTable).filter_by(specialty_id=2, level=8).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level8 = []
    for data in level8_data:
        level8.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    return level1,level2,level3,level4,level5,level6,level7,level8

def IT():
    
    level1_data = session.query(TimetableTable).filter_by(specialty_id=3, level=1).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level1 = []
    for data in level1_data:
        level1.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })

    level2_data = session.query(TimetableTable).filter_by(specialty_id=3, level=2).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level2 = []
    for data in level2_data:
        level2.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })

    level3_data = session.query(TimetableTable).filter_by(specialty_id=3, level=3).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level3 = []
    for data in level3_data:
        level3.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level4_data = session.query(TimetableTable).filter_by(specialty_id=3, level=4).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level4 = []
    for data in level4_data:
        level4.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level5_data = session.query(TimetableTable).filter_by(specialty_id=3, level=5).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level5 = []
    for data in level5_data:
        level5.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level6_data = session.query(TimetableTable).filter_by(specialty_id=3, level=6).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level6 = []
    for data in level6_data:
        level6.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level7_data = session.query(TimetableTable).filter_by(specialty_id=3, level=7).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level7 = []
    for data in level7_data:
        level7.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    
    level8_data = session.query(TimetableTable).filter_by(specialty_id=3, level=8).join(InstructorsTable).filter(
        TimetableTable.instructor_id == InstructorsTable.id).join(CoursesTable).filter(
        TimetableTable.course_id == CoursesTable.id).all()
    level8 = []
    for data in level8_data:
        level8.append({
            "table_name": 'CS',
            "course_id": data.course.name,
            "hall_id": data.hall_id,
            "instructor": data.instructor.name,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "day": data.day,
            "level": data.level
        })
    return level1,level2,level3,level4,level5,level6,level7,level8