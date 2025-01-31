# 백준 2309번: 일곱 난쟁이
# 문제 설명:
# 아홉 명의 난쟁이 중 키의 합이 100이 되는 일곱 명을 찾아 오름차순으로 출력하는 문제.
# 가능한 정답이 하나만 존재함이 보장된다.

# 입력 형식:
# 아홉 개의 줄에 걸쳐 각 난쟁이의 키(자연수)가 주어진다. (1 ≤ 키 ≤ 99)

# 출력 형식:
# 키의 합이 100이 되는 일곱 난쟁이의 키를 오름차순으로 한 줄에 하나씩 출력한다.

# 예제 입력 1:
# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13
# 예제 출력 1:
# 7
# 8
# 10
# 13
# 19
# 20
# 23


# 🛑 [❌ 사용자가 작성한 코드] (틀린 코드)
"""
array = [int(input()) for _ in range(9)]
total_sum = sum(dwarfs)
    
# 일곱 난쟁이를 찾기 위한 9명 중 2명을 제외하는 루프
for i in range(9):
    for j in range(i + 1, 9):
        if total_sum - dwarfs[i] - dwarfs[j] == 100:
            # 제외할 두 난쟁이를 찾으면 리스트에서 제거
            excluded_dwarfs = [dwarfs[k] for k in range(9) if k != i and k != j]
            sorted(excluded_dwarfs)  # ❌ 리스트 정렬이 적용되지 않음
            break
for i in range(7):
    print(excluded_dwarfs[i])
"""

# 📌 [❌ 사용자의 코드에서 틀린 점]
# 1. **변수명 오류 (`dwarfs` → `array`)**
#    - `dwarfs` 변수명이 존재하지 않음. `array`로 선언된 변수를 사용해야 함.
# 2. **리스트 정렬이 적용되지 않음**
#    - `sorted(excluded_dwarfs)`는 정렬된 리스트를 반환하지만 원본 리스트를 변경하지 않음.
#    - **수정 방법:** `excluded_dwarfs = sorted(excluded_dwarfs)`
# 3. **이중 루프 탈출이 보장되지 않음**
#    - 내부 `break`가 실행되면 `j` 루프만 종료되고, `i` 루프는 계속 진행됨.
#    - **수정 방법:** `found = True` 플래그를 추가하여 이중 루프 완전히 종료.

---

# ✅ [✔ 모범 답안: 올바르게 수정된 코드]
# - 아홉 난쟁이 중 두 명을 제외하여 키의 합이 100이 되는 일곱 명을 찾음.
# - `sorted()`를 사용하여 정렬 후 출력.

import sys

# 난쟁이 키 입력 받기
array = [int(sys.stdin.readline().strip()) for _ in range(9)]
total_sum = sum(array)

found = False  # 정답을 찾았는지 여부

# 아홉 명 중 두 명을 제외하는 이중 루프
for i in range(9):
    for j in range(i + 1, 9):
        if total_sum - array[i] - array[j] == 100:
            # 일곱 난쟁이만 남기는 리스트 생성
            excluded_dwarfs = sorted([array[k] for k in range(9) if k != i and k != j])
            
            # 정답 출력
            for dwarf in excluded_dwarfs:
                print(dwarf)
            
            found = True
            break  # 내부 루프 탈출
    if found:
        break  # 외부 루프도 탈출
