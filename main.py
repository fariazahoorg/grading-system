import pandas as pd
class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
        self.status = ""   # important
    def check_status(self):
        average = (self.math_score + self.science_score) / 2
        if average >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"
df = pd.read_csv("raw grades.csv")
df = df.fillna(0)
students_list = []
for index, row in df.iterrows():
    student = Student(
        row["Student_Name"],
        row["Math Score"],
        row["Science Score"]
    )
    student.check_status()
    students_list.append({
        "Student_Name": student.name,
        "Math Score": student.math_score,
        "Science Score": student.science_score,
        "Status": student.status
    })
final_df = pd.DataFrame(students_list)
final_df["School_Year"] = "2023-2024"
final_df.to_csv("final_grades.csv", index=False)
print("Final grades file created successfully!")
