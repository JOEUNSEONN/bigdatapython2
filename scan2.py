import requests
from bs4 import BeautifulSoup
import random

# ======================== #
# 향수 랭킹 수집 (Fragrantica)
# ======================== #
url = 'https://www.fragrantica.com/perfume-rating/'  # 예시 URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 향수 리스트 수집 (사이트 구조에 맞게 선택자 수정 필요)
scents = soup.select('.cell2 a')
perfumes = [scent.get_text(strip=True) for scent in scents[:50]]  # 상위 50개 향수

# 추가 향수 (예비용)
extra_perfumes = [
    "코튼", "머스크", "화이트로즈", "가드니아", "블랙베리", "블랙체리", "아쿠아마린", "르네상스",
    "라벤더", "로즈마리", "라일락", "랑데뷰", "히아신스", "백합", "라임", "레더"
]
perfumes.extend(extra_perfumes)

# ======================== #
# 메뉴 출력
# ======================== #
print("=======================")
print("     향수 추천 시스템")
print("=======================")
print("1. 향수 Top 100")
print("2. 향수 Top 50")
print("3. 향수 Top 10")
print("4. AI 추천 향수")
print("5. 향수 이름 검색")
print("=======================")

n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}")

# ======================== #
# 메뉴 기능 처리
# ======================== #
if n == "1":
    print("\n📌 향수 Top 100")
    for i in range(min(100, len(perfumes))):
        print(f"{i+1}. {perfumes[i]}")

elif n == "2":
    print("\n📌 향수 Top 50")
    for i in range(min(50, len(perfumes))):
        print(f"{i+1}. {perfumes[i]}")

elif n == "3":
    print("\n📌 향수 Top 10")
    for i in range(min(10, len(perfumes))):
        print(f"{i+1}. {perfumes[i]}")

elif n == "4":
    print("\n🤖 AI 추천 향수")
    ai_perfume = random.choice(perfumes)
    print(f"✨ 오늘의 추천 향수는: {ai_perfume} 입니다.")

elif n == "5":
    print("\n🔍 향수 이름 검색")
    keyword = input("검색할 향수 이름을 입력하세요: ")
    results = [p for p in perfumes if keyword in p]
    if results:
        print("\n🔎 검색 결과:")
        for result in results:
            print(f"- {result}")
    else:
        print("😢 해당 향수를 찾을 수 없습니다.")

else:
    print("⚠️ 1~5까지의 숫자만 입력해주세요.")
