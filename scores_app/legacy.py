# Deliberately ugly legacy code

def legacy_rank_1(students):
    result = []
    for s in students:
        if s.get("score") >= 90:
            result.append((s.get("name"), "gold"))
        elif s.get("score") >= 70:
            result.append((s.get("name"), "silver"))
        elif s.get("score") >= 50:
            result.append((s.get("name"), "bronze"))
        else:
            result.append((s.get("name"), "fail"))
    return result


def legacy_rank_2(students):
    result = []
    for s in students:
        if s.get("score") >= 90:
            result.append((s.get("name"), "gold"))
        elif s.get("score") >= 70:
            result.append((s.get("name"), "silver"))
        elif s.get("score") >= 50:
            result.append((s.get("name"), "bronze"))
        else:
            result.append((s.get("name"), "fail"))
    return result


def legacy_rank_3(students):
    result = []
    for s in students:
        if s.get("score") >= 90:
            result.append((s.get("name"), "gold"))
        elif s.get("score") >= 70:
            result.append((s.get("name"), "silver"))
        elif s.get("score") >= 50:
            result.append((s.get("name"), "bronze"))
        else:
            result.append((s.get("name"), "fail"))
    return result
