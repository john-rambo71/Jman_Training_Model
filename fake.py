import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


trainers = [fake.name() for _ in range(50)]


session_names = [
    "React",
    "Node",
    "Python",
    "JavaScript",
    "SQL",
    "HTML",
    "CSS",
    "Java",
    "C#",
    "PHP",
    "Machine Learning",
    "Data Science",
    "Artificial Intelligence",
]


# Function to generate fake data
def generate_fake_data():
    trainer = random.choice(trainers)
    session = random.choice(session_names)
    start_time = fake.date_time_this_year()
    end_time = start_time + timedelta(minutes=random.randint(480, 4800))
    duration = (end_time - start_time).seconds // 60
    status = random.choice(["Completed", "Not Completed"])
    return [fake.uuid4(), trainer, session, start_time, end_time, duration, status]


rows = [generate_fake_data() for _ in range(100000)]

with open("fake_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        [
            "ID",
            "Trainer Name",
            "Session Name",
            "Start Time",
            "End Time",
            "Duration",
            "Status",
        ]
    )
    writer.writerows(rows)

print("Fake data generated and saved to fake_data.csv")
