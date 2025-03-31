import requests
from bs4 import BeautifulSoup
import random
import time

# ======================== #
# 1️⃣ 향수 랭킹 크롤링 (Fragrantica)
# ======================== #

headers = {"User-Agent": "Mozilla/5.0"}
fragrantica_url = "https://www.fragrantica.com/perfume-rating/"  # 예제 URL
response = requests.get(fragrantica_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 인기 향 리스트 가져오기 (CSS 선택자는 사이트 구조에 맞게 수정 필요)
scents = soup.select(".cell2 a")  # Fragrantica의 향수 랭킹 리스트

perfumes = [scent.get_text(strip=True) for scent in scents[:10]]  # 상위 10개 추출

# 추가적인 향수 목록
extra_perfumes = [
    "코튼", "머스크", "화이트로즈", "가드니아", "블랙베리", "블랙체리", "아쿠아마린", "르네상스", 
    "라벤더", "로즈마리", "라일락", "랑데뷰", "히아신스", "백합", "라임", "레더"
]
perfumes.extend(extra_perfumes)

print("\n📌 인기 향수 랭킹:")
for i, perfume in enumerate(perfumes, 1):
    print(f"{i}. {perfume}")

# ======================== #
# 2️⃣ 랜덤 향수 추천 시스템
# ======================== #

print("AI야 향수를 추천해줘!")
print("""
알겠습니다.
제가 열심히 분석해서
고객님께 향수를 추천합니다
      """)

# AI가 추천하는 코드
ai_perfume = random.choice(perfumes)
dd = ["두", "두", "두", "두둥"]
for d in dd:
    print(d)
    time.sleep(1)

print(f"제가 추천한 향수는 {ai_perfume}입니다.")
