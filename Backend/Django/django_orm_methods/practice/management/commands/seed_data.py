# Import Ramdom Library 
import random
# To work with date and time - DOB, Registration Date
import datetime

# To seed-data, we need to make the file in the respective folder:
# practice/management/commands/seed_data.py

# We need include this line to inform the Django server that seed_data file is located in this path
from django.core.management.base import BaseCommand
# Importing the models: All 3 models
from practice.models import Student, Branch, Course
# Faker is used to generate the fake data for practice or testing purpose
from faker import Faker

class Command(BaseCommand):
    help = 'Seeds the database with Indian student data, branches, and courses'

    def handle(self, *args, **kwargs):
        # Specifying that Faker needs to generate Indian Origin data
        fake = Faker('en_IN')

        # Clear existing data to avoid duplicates when re-running
        # If any old data exists, it will be removed before adding the fake data
        Student.objects.all().delete()
        Course.objects.all().delete()
        Branch.objects.all().delete()

        self.stdout.write("Old data cleared. Seeding new data...")

        # 1. Create Branches
        # I need 6 branches: CSE, ISE, ECE, EEE, AIML & IoT
        branches_data = [
            {'short': 'CSE', 'long': 'Computer Science & Engineering'},
            {'short': 'ISE', 'long': 'Information Science & Engineering'},
            {'short': 'ECE', 'long': 'Electronics & Communication Engineering'},
            {'short': 'EEE', 'long': 'Electrical & Electronics Engineering'},
            {'short': 'AIML', 'long': 'Artificial Intelligence & Machine Learning'},
            {'short': 'IoT', 'long': 'Internet of Things'},
        ]
        branches = []
        for b_data in branches_data:
            # Get the short_name &  long_name from the branches_data dictionary and insert branches one by one
            branch = Branch.objects.create(short_name=b_data['short'], long_name=b_data['long'])
            branches.append(branch)
            # Once the branch is created, just print it for confirmation
            self.stdout.write(self.style.SUCCESS(f"Created branch: {b_data['short']} - {b_data['long']}"))

        # 2. Create Courses
        # Same approach as that of Branch table
        # 5 course and its details are predefined
        courses_data = [
            {'short': 'Java FSWD', 'long': 'Java Full Stack Web Development', 'duration': 6, 'fees': 45000.00},
            {'short': 'Python FSWD', 'long': 'Python Full Stack Web Development', 'duration': 6, 'fees': 40000.00},
            {'short': 'AWS', 'long': 'Amazon Web Services Cloud Computing', 'duration': 3, 'fees': 25000.00},
            {'short': 'AIML', 'long': 'Artificial Intelligence & Machine Learning', 'duration': 8, 'fees': 55000.00},
            {'short': 'DevOps', 'long': 'DevOps Engineering', 'duration': 4, 'fees': 35000.00},
        ]
        courses = []
        for c_data in courses_data:
            course = Course.objects.create(
                short_name=c_data['short'],
                long_name=c_data['long'],
                duration=c_data['duration'],
                fees=c_data['fees']
            )
            courses.append(course)
            self.stdout.write(self.style.SUCCESS(f"Created course: {c_data['short']}"))

        # 3. Create 50 Students
        # I want the students to be distributed to 4 even semesters (2 - 8)
        sem_choices = [2, 4, 6, 8]
        
        for i in range(50):
            # Decide gender first
            # Male & Female
            gender = random.choice(['M', 'F'])
            # Based on the name, the gender will be assigned
            if gender == 'M':
                name = fake.name_male()
            else:
                name = fake.name_female()

            # I want the Faker to generate: email, phone, 
            # (Allocate the branch & sem from the given options using random library)
            email = fake.unique.email()
            phone = fake.phone_number()
            branch = random.choice(branches)
            sem = random.choice(sem_choices)
            
            # Random dob between 2001 and 2004
            year = random.randint(2001, 2004)
            month = random.randint(1, 12)
            day = random.randint(1, 28) # Keep it safe to avoid invalid dates like Feb 30
            # First get the random year out of 2001 to 2004, Jan to Dec, 1 to 28
            
            # Finalize the DOB with combination of all data: Day, Month & Year
            dob = datetime.date(year, month, day)
            
            # Random registration date between 20-April-2026 to 25-April-2026
            reg_day = random.randint(20, 25)
            registration_date = datetime.date(2026, 4, reg_day)
            
            student = Student.objects.create(
                name=name,
                email=email,
                phone=phone,
                dob=dob,
                gender=gender,
                sem=sem,
                registration_date=registration_date,
                branch=branch
            )
            
            # Assign each student to different courses randomly
            # Randomly assign 1-3 courses to each student
            assigned_courses = random.sample(courses, k=random.randint(1, 3))
            student.courses.add(*assigned_courses)
            
            self.stdout.write(f"Created student {i+1}: {name} ({gender}) - DOB: {dob} - Sem: {sem}")

        self.stdout.write(self.style.SUCCESS('Successfully seeded 50 students with new fields!'))