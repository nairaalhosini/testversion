from scores_app.processor import calculate_math_score, build_grade


def test_calculate_math_score_basic():
    assert calculate_math_score({"math": 80, "bonus": 5}) == 85


def test_build_grade():
    s = {"math": 90, "science": 90, "history": 90, "bonus": 0}
    assert build_grade(s) == "A"
