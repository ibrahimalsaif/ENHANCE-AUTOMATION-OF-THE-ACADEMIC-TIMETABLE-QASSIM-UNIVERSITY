from sqlalchemy import Column, String, Integer, Float, Boolean, Time, ARRAY, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

'''
Constructs a base class for declarative class definitions
'''

Base = declarative_base()

'''
The classes below are mapped tables in the database so that we can create the tables
also manage to do all the related operations like query, insert, update and delete
'''

'''
SpecialtyInCollege
'''


class SpecialtyInCollegeTable(Base):
    __tablename__ = "specialtyInCollege"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    specialty_in_college_id = relationship("StudentPlanTable", uselist=False, backref="specialtyInCollege")
    specialty_in_college_id1 = relationship("InstructorsTable", backref="specialtyInCollege")
    specialty_in_college_id2 = relationship("HallsTable", backref="specialtyInCollege")
    specialty_in_college_id3 = relationship("TimetableTable", backref="specialtyInCollege")


'''
Instructors
'''


class InstructorsTable(Base):
    __tablename__ = "instructors"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    specialty = Column(Integer(), ForeignKey('specialtyInCollege.id'), nullable=False)
    instructor_id = relationship("CoursesTable", backref="instructor")
    instructor_id1 = relationship("TimetableTable", backref="instructor")


'''
Courses
'''


class CoursesTable(Base):
    __tablename__ = "courses"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    credit = Column(Float(), nullable=False)
    instructor_id = Column(Integer(), ForeignKey('instructors.id'), nullable=False)
    pre_req = Column(String(255))
    co_req = Column(String(255))
    is_lab = Column(Boolean(), nullable=False)
    common = Column(ARRAY(String(120)))
    priority = Column(Integer(), nullable=False)
    course_id = relationship("StudentPlanCoursesTable", uselist=False, backref="course")
    course_id1 = relationship("TimetableTable", backref="course")


'''
StudentPlan
'''


class StudentPlanTable(Base):
    __tablename__ = "studentPlan"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    specialty = Column(Integer(), ForeignKey('specialtyInCollege.id'), nullable=False)
    student_plan_id = relationship("StudentPlanCoursesTable", backref="studentPlan")


'''
Halls
'''


class HallsTable(Base):
    __tablename__ = "halls"
    id = Column(Integer(), primary_key=True)
    specialty_id = Column(Integer(), ForeignKey('specialtyInCollege.id'), nullable=False)
    is_lab = Column(Boolean(), nullable=False)
    building = Column(String(255))
    hall_id = relationship("TimetableTable", backref="hall")


'''
StudentPlanCourses
'''


class StudentPlanCoursesTable(Base):
    __tablename__ = "studentPlanCourses"
    id = Column(Integer(), primary_key=True)
    student_plan_id = Column(Integer(), ForeignKey('studentPlan.id'), nullable=False)
    level = Column(Integer(), nullable=False)
    course_id = Column(Integer(), ForeignKey('courses.id'), nullable=False)


'''
WorkTime
'''


class WorkTimeTable(Base):
    __tablename__ = "worktime"
    id = Column(Integer(), primary_key=True)
    day = Column(Integer(), unique=True, nullable=False)
    start_time = Column(Time(), nullable=False)
    end_time = Column(Time(), nullable=False)
    break_time_start = Column(Time(), nullable=False)
    break_time_end = Column(Time(), nullable=False)


'''
TimeTable
'''

class TimetableTable(Base):
    __tablename__ = "timetable"
    id = Column(Integer(), primary_key=True)
    specialty_id = Column(Integer(), ForeignKey('specialtyInCollege.id'), nullable=False)
    course_id = Column(Integer(), ForeignKey('courses.id'), nullable=False)
    hall_id = Column(Integer(), ForeignKey('halls.id'), nullable=False)
    instructor_id = Column(Integer(), ForeignKey('instructors.id'), nullable=False)
    start_time = Column(Float(), nullable=False)
    end_time = Column(Float(), nullable=False)
    day = Column(Integer(), nullable=False)
    level = Column(Integer(), nullable=False)


'''
:create_engine:
This function produces an Engine object based on a URL
that maps to our database
:create_all:
This function is to create all the tables in the database, you only need to run it
the first time
'''
engine = create_engine('postgresql://username:password@localhost:port/database_name', echo=True)
# Base.metadata.create_all(bind=engine)

'''
Creating the session to start operating on the database
'''

Session = sessionmaker(bind=engine)
session = Session()
