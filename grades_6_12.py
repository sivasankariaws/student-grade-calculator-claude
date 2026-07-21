# grades.py — Student Grade Calculator
# Core grading logic for the online learning platform.

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
    """Convert a numeric score to a letter grade.

    Args:
        score: Numeric score between 0 and 100.

    Returns:
        Letter grade as a string: A, B, C, D, or F.

    Raises:
        ValueError: If score is outside the range 0 to 100.
    """
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
    """Calculate the average of a list of scores.

    Args:
        scores: List of numeric scores.

    Returns:
        Average score as a float.

    Raises:
        ValueError: If scores list is empty.
    """
    if not scores:
        raise ValueError("scores list cannot be empty")
    return sum(scores) / len(scores)


def calculate_gpa(letter_grades: list[str]) -> float:
    """Calculate GPA from a list of letter grades.

    Args:
        letter_grades: List of letter grades (A, B, C, D, or F).

    Returns:
        GPA as a float rounded to 2 decimal places.

    Raises:
        ValueError: If letter_grades is empty or contains invalid grades.
    """
    if not letter_grades:
        raise ValueError("letter_grades list cannot be empty")
    for grade in letter_grades:
        if grade not in GPA_POINTS:
            raise ValueError(f"Invalid grade '{grade}'. Must be A, B, C, D, or F.")
    total_points = sum(GPA_POINTS[grade] for grade in letter_grades)
    return round(total_points / len(letter_grades), 2)


def get_student_summary(student_name: str, scores: list[float]) -> str:
    """Generate a formatted academic summary for a student.

    Args:
        student_name: Full name of the student.
        scores: List of numeric scores for the student.

    Returns:
        A formatted multi-line summary string.

    Raises:
        ValueError: If scores list is empty or student_name is blank.
    """
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
        f"  Scores:  {scores}\n"
        f"  Average: {average:.1f}\n"
        f"  Grade:   {letter}\n"
        f"  GPA:     {gpa}"
    )
