class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        total_scores = []
        for student in self.students.values():
            total_scores.extend(student.scores)
        if len(total_scores) == 0:
            return 0
        return sum(total_scores) / len(total_scores)

    def display_student_performance(self):
        for name, student in self.students.items():
            average = student.calculate_average()
            passing = student.is_passing()
            status = "Passing" if passing else "Needs Improvement"
            print(f"Student: {name}, Average Score: {average:.2f}, Status: {status}")
        class_avg = self.calculate_class_average()
        print(f"\nClass Average Score: {class_avg:.2f}")


def main():
    tracker = PerformanceTracker()

    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            scores = []
            for subject in ["Math", "Science", "English"]:
                score = int(input(f"Enter score for {subject}: "))
                scores.append(score)
            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")

    tracker.display_student_performance()


if __name__ == "__main__":
    main()
