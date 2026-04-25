def solution(id_pw, db):
    i, p = id_pw
    for di, dp in db:
        if i == di:
            if p == dp:
                return "login"
            else:
                return "wrong pw"
    return "fail"
