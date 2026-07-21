# tests/test_grades.py — Student Grade Calculator Tests

import pytest
from grades import (
    calculate_letter_grade,
    calculate_average,
    calculate_gpa,
    get_student_summary,
)


# ── calculate_letter_grade ─────────────────────────────────────────────────

def test_calculate_letter_grade_A():
    assert calculate_letter_grade(95) == "A"

def test_calculate_letter_grade_B():
    assert calculate_letter_grade(85) == "B"

def test_calculate_letter_grade_F():
    assert calculate_letter_grade(50) == "F"

def test_calculate_letter_grade_boundary_exactly_90():
    assert calculate_letter_grade(90) == "A"

def test_calculate_letter_grade_invalid_above_100():
    with pytest.raises(ValueError):
        calculate_letter_grade(110)

def test_calculate_letter_grade_invalid_negative():
    with pytest.raises(ValueError):
        calculate_letter_grade(-5)


# ── calculate_average ──────────────────────────────────────────────────────

def test_calculate_average_returns_correct_value():
    assert calculate_average([80, 90, 70]) == 80.0

def test_calculate_average_single_score():
    assert calculate_average([100]) == 100.0

def test_calculate_average_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_average([])


# ── calculate_gpa ──────────────────────────────────────────────────────────

def test_calculate_gpa_all_A():
    assert calculate_gpa(["A", "A", "A"]) == 4.0

def test_calculate_gpa_mixed_grades():
    assert calculate_gpa(["A", "B", "C"]) == 3.0

def test_calculate_gpa_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_gpa([])

def test_calculate_gpa_invalid_grade_raises():
    with pytest.raises(ValueError):
        calculate_gpa(["A", "X", "B"])


# ── get_student_summary ────────────────────────────────────────────────────

def test_get_student_summary_contains_name():
    result = get_student_summary("Alice", [90, 85, 92])
    assert "Alice" in result

def test_get_student_summary_blank_name_raises():
    with pytest.raises(ValueError):
        get_student_summary("  ", [90, 85])

def test_get_student_summary_empty_scores_raises():
    with pytest.raises(ValueError):
        get_student_summary("Bob", [])
