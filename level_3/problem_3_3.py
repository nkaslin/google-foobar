def solution(x, y):
    x, y = int(x), int(y)
    if y < x:
        x, y = y, x
    res = 0
    while x > 1:
        res += y / x
        y %= x
        x, y = y, x
    if x == 1:
        return str(res + y - 1)
    return "impossible"


if __name__ == "__main__":
    assert solution("8", "3") == "4"
    assert solution("4", "2") == "impossible"
    assert solution("1" + "0" * 49 + "1",
                    "2") == "50000000000000000000000000000000000000000000000001"
