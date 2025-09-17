# 2353_design_a_food_rating_system.py
# -----------------------------------------------------
# ✅ 제목: Design a Food Rating System (LeetCode 2353)
# ✅ 문제 설명(요약):
# - 음식 이름 foods[i], 종류 cuisines[i], 평점 ratings[i]가 주어진다.
# - 연산:
#   1) changeRating(food, newRating): 해당 음식 평점 갱신
#   2) highestRated(cuisine): 그 종류에서 최고 평점, 동률이면 사전순 가장 앞선 음식 이름 반환
#
# ✅ 입력 형식(요지):
# - 생성자: FoodRatings(foods: List[str], cuisines: List[str], ratings: List[int])
# - 메서드:
#   - changeRating(food: str, newRating: int) -> None
#   - highestRated(cuisine: str) -> str
#
# ✅ 규칙 요약:
# 1) 음식 이름은 유일
# 2) highestRated는 최신 평점을 즉시 반영
# 3) 동률 시 이름 오름차순
# 4) 효율: 다수의 갱신과 조회를 빠르게 처리
#
# ✅ 입출력 예시(1개):
# - 초기: foods=["kimchi","miso","sushi","moussaka","ramen","bulgogi"]
#         cuisines=["korean","japanese","japanese","greek","japanese","korean"]
#         ratings=[9,12,8,15,14,7]
# - highestRated("korean") -> "kimchi"
# - highestRated("japanese") -> "ramen"
# - changeRating("sushi", 16)
# - highestRated("japanese") -> "sushi"
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
import heapq as hq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.food_info = {}                             # food → (cuisine, rating)
        self.cuisine_heap = {}                          # cuisine → [(-rating, food)]

        for f, c, r in zip(foods, cuisines, ratings):   # 초기 맵/힙 구성
            self.food_info[f] = (c, r)
            if c not in self.cuisine_heap:
                self.cuisine_heap[c] = []
            hq.heappush(self.cuisine_heap[c], (-r, f))  # 최대힙 역할(음수 평점)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]               # 현재 종류 확인
        self.food_info[food] = (cuisine, newRating)     # 최신 평점 갱신
        hq.heappush(self.cuisine_heap[cuisine], (-newRating, food))  # 새 기록 push(지연 삭제)

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]
        while heap:                                     # lazy deletion
            r, f = heap[0]
            if self.food_info[f][1] == -r:              # 최신 평점과 일치하면 정답
                return f
            hq.heappop(heap)                            # 오래된 기록 폐기


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - dict + heap + 지연 삭제 패턴으로 동작 확인.
# - 예제 입력 기준 기대 출력과 일치.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 초기엔 changeRating에서 힙 갱신 누락 → highestRated가 이전 기록을 반환.
# - 수정: changeRating에서 새 (-newRating, food) push 추가.
# - highestRated에서 top이 최신 평점과 다르면 pop하는 lazy deletion 유지.
#
# 📚 사용된/필수 개념(최소):
# - 해시맵: food → (cuisine, rating) 현재 상태 O(1) 조회
# - 종류별 힙: (-rating, name)로 최대 평점 + 이름 오름차순
# - 지연 삭제(lazy deletion): 임의 원소 삭제 대신 조회 시 검증/폐기
# - 시간복잡도: 초기화 O(n log n), changeRating O(log n), highestRated 암ortized O(log n)
#
# 4. (선택) 다른 효율적인 풀이 또는 알고리즘 제안
# - 정렬 세트(BST) 사용: cuisine별 SortedList에 ( -rating, name ) 유지 → 삽입/삭제/최댓값 O(log n)
#   단, 외부 라이브러리 필요. 표준 라이브러리만으로는 힙+지연 삭제가 가장 실용적.
