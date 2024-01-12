def to_angle(h, m, s):
    h_angle = (h * 360 / 12 + m * 360 / 12 / 60 + s * 360 / 12 / 60 / 60) % 360
    m_angle = (m * 360 / 60 + s * 360 / 60 / 60) % 360
    s_angle = (s * 360 / 60) % 360

    return h_angle, m_angle, s_angle

def check(s1_angle, sn_angle, x1_angle, xn_angle):
    if s1_angle < x1_angle and xn_angle <= sn_angle:
        return True
    elif s1_angle == 354 and x1_angle > 354:
        return True

    return False

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    if (h1, m1, s1) in ((0, 0, 0), (12, 0, 0)):
        answer += 1

    while (h1, m1, s1) != (h2, m2, s2):
        hn, mn, sn = h1 + (m1 + (s1 + 1) // 60) // 60, (m1 + (s1 + 1) // 60) % 60, (s1 + 1) % 60

        h1_angle, m1_angle, s1_angle = to_angle(h1, m1, s1)
        hn_angle, mn_angle, sn_angle = to_angle(hn, mn, sn)

        is_h = check(s1_angle, sn_angle, h1_angle, hn_angle)
        is_m = check(s1_angle, sn_angle, m1_angle, mn_angle)

        if is_h and is_m and hn_angle == mn_angle:
            answer += 1
        elif is_h and is_m:
            answer += 2
        elif is_h or is_m:
            answer += 1

        h1, m1, s1 = hn, mn, sn

    return answer