def total_complexity(s: str) -> int:
    # 1) 키보드 배치와 좌표 매핑
    row0 = "qwertyui"  # 9개
    row1 = "pasdfghjk" # 9개
    row2 = "lzxcvbnm"  # 8개

    pos = {}
    for r, row in enumerate([row0, row1, row2]):
        for c, ch in enumerate(row):
            pos[ch] = (r, c)

    # 2) 인접 쌍 거리 미리 계산
    n = len(s)
    # 안전을 위해 소문자로 가정(입력이 소문자라고 했으니)
    s = s.lower()

    def dist(a: str, b: str) -> int:
        ra, ca = pos[a]
        rb, cb = pos[b]
        return abs(ra - rb) + abs(ca - cb)

    # 3) 간선 i(=s[i], s[i+1])의 기여도: d_i * (i+1) * (n-i-1)
    ans = 0
    for i in range(n - 1):
        d = dist(s[i], s[i + 1])
        weight = (i + 1) * (n - i - 1)
        ans += d * weight
    return ans


# 예시 확인
# print(total_complexity("abcdc"))  # 23