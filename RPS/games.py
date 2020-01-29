def game(attack, defense):
    if (attack == '가위' and defense == '바위') \
            or (attack == '보' and defense == '가위') \
            or (attack == '바위' and defense == '보'):
        return '패'
    elif attack == defense:
        return '무승부'
    else:
        return '승'
