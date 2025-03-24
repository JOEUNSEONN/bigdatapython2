import requests
from bs4 import BeautifulSoup

# ======================== #
# 1️⃣ 코튼 계열 향수 랭킹 크롤링 (Fragrantica)
# ======================== #

# Fragrantica의 코튼 향 관련 페이지 (예제 URL, 실제 검색 기반으로 변경 가능)
cotton_url = "https://www.fragrantica.com/search/?query=cotton"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(cotton_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 향수 리스트 가져오기 (CSS 선택자는 사이트 구조에 맞게 수정 필요)
perfumes = soup.select(".card-title")  # 향수 이름
brands = soup.select(".card-subtitle")  # 브랜드 이름

print("\n📌 코튼 계열 인기 향수 TOP 10:")
for i in range(min(10, len(perfumes))):  # 최대 10개 출력
    perfume_name = perfumes[i].get_text(strip=True)
    brand_name = brands[i].get_text(strip=True)
    print(f"{i+1}. {brand_name} - {perfume_name}")
