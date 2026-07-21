# grades.py — Student Grade Calculator
# THIS IS THE "BAD PR" VERSION used in the demo
# It contains intentional violations of CLAUDE.md standards
# so that the GitHub Actions CI workflow triggers a BLOCKED review

GRADE_THRESHOLDS = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
}

GPA_POINTS = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0,
}


def calculate_letter_grade(score: float) -> str:
    """Convert a numeric score to a letter grade."""
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    if score >= GRADE_THRESHOLDS["A"]:
        return "A"
    elif score >= GRADE_THRESHOLDS["B"]:
        return "B"
    elif score >= GRADE_THRESHOLDS["C"]:
        return "C"
    elif score >= GRADE_THRESHOLDS["D"]:
        return "D"
    else:
        return "F"


def calculate_average(scores: list[float]) -> float:
    """Calculate the average of a list of scores."""
    if not scores:
        raise ValueError("scores list cannot be empty")
    return sum(scores) / len(scores)


def calculate_gpa(letter_grades: list[str]) -> float:
    """Calculate GPA from a list of letter grades."""
    if not letter_grades:
        raise ValueError("letter_grades list cannot be empty")
    for grade in letter_grades:
        if grade not in GPA_POINTS:
            raise ValueError(f"Invalid grade '{grade}'.")
    total_points = sum(GPA_POINTS[grade] for grade in letter_grades)
    return round(total_points / len(letter_grades), 2)


def get_student_summary(student_name: str, scores: list[float]) -> str:
    """Generate a formatted academic summary for a student."""
    if not student_name.strip():
        raise ValueError("student_name cannot be blank")
    if not scores:
        raise ValueError("scores list cannot be empty")
    average = calculate_average(scores)
    letter = calculate_letter_grade(average)
    gpa = calculate_gpa([calculate_letter_grade(s) for s in scores])
    return (
        f"Student Report\n"
        f"  Name:    {student_name}\n"
        f"  Average: {average:.1f}\n"
        f"  Grade:   {letter}\n"
        f"  GPA:     {gpa}"
    )


# ── VIOLATION 1: No type hints ─────────────────────────────────────────────
# VIOLATION 2: No docstring
# VIOLATION 3: No tests written for this new function
def get_top_students(students, threshold):
    results = []
    for name, scores in students.items():
        avg = calculate_average(scores)
        if avg >= threshold:
            results.append((name, avg))
    results.sort(key=lambda x: x[1], reverse=True)
    return results


# ── VIOLATION 4: Function is too long (over 20 lines) ─────────────────────
def generate_class_report(class_name: str, students: dict) -> str:
    """Generate a full class performance report."""
    if not class_name:
        raise ValueError("class_name cannot be blank")
    if not students:
        raise ValueError("students dict cannot be empty")
    lines = []
    lines.append("=" * 50)
    lines.append(f"CLASS REPORT: {class_name}")
    lines.append("=" * 50)
    all_averages = []
    for student_name, scores in students.items():
        avg = calculate_average(scores)
        all_averages.append(avg)
        grade = calculate_letter_grade(avg)
        gpa = calculate_gpa([calculate_letter_grade(s) for s in scores])
        lines.append(f"Student: {student_name}")
        lines.append(f"  Average: {avg:.1f}")
        lines.append(f"  Grade:   {grade}")
        lines.append(f"  GPA:     {gpa}")
        lines.append("")
    class_avg = calculate_average(all_averages)
    class_grade = calculate_letter_grade(class_avg)
    lines.append("-" * 50)
    lines.append(f"Class Average: {class_avg:.1f} ({class_grade})")
    lines.append(f"Total Students: {len(students)}")
    lines.append("=" * 50)
    return "\n".join(lines)
