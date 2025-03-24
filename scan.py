import requests
from bs4 import BeautifulSoup

# ======================== #
# 1️⃣ 향수 블렌딩 조합 크롤링 (구글 검색)
# ======================== #

google_url = "https://www.google.com/search?q=popular+perfume+mixing+combinations"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(google_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 검색 결과에서 제목 가져오기
titles = soup.select("h3")

print("\n📌 인기 있는 향수 블렌딩 조합:")
for i, title in enumerate(titles[:10], 1):  # 상위 10개 출력
    print(f"{i}. {title.get_text()}")

# ======================== #
# 2️⃣ 향수 랭킹 크롤링 (Fragrantica)
# ======================== #

fragrantica_url = "https://www.fragrantica.com/perfume-rating/"  # 예제 URL (실제 페이지 구조 확인 필요)
response = requests.get(fragrantica_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 인기 향 리스트 가져오기 (CSS 선택자는 사이트 구조에 맞게 수정 필요)
scents = soup.select(".cell2 a")  # Fragrantica의 향수 랭킹 리스트

print("\n📌 인기 향수 랭킹:")
for i, scent in enumerate(scents[:10], 1):  # 상위 10개 출력
    print(f"{i}. {scent.get_text(strip=True)}")
