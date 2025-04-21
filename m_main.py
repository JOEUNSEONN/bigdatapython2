import requests
from bs4 import BeautifulSoup
import random

def get_perfume_list():
    url = 'https://www.fragrantica.com/perfume-rating/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    scents = soup.select('.cell2 a')
    perfumes = [scent.get_text(strip=True) for scent in scents[:50]]

    extra = ["코튼", "머스크", "화이트로즈", "가드니아", "블랙베리", "블랙체리", "아쿠아마린",
             "르네상스", "라벤더", "로즈마리", "라일락", "랑데뷰", "히아신스", "백합", "라임", "레더"]
    perfumes.extend(extra)
    return perfumes

def m100(perfumes):
    print("\n📌 향수 Top 100")
    for i in range(min(100, len(perfumes))):
        print(f"{i+1}. {perfumes[i]}")

def m50(perfumes):
    print("\n📌 향수 Top 50")
    for i in range(min(50, len(perfumes))):
        print(f"{i+1}. {perfumes[i]}")

def m10(perfumes):
    print("\n📌 향수 Top 10")
    for i in range(min(10, len(perfumes))):
        print(f"{i+1}. {perfumes[i]}")

def m_random(perfumes):
    print("\n🤖 AI 추천 향수")
    choice = random.choice(perfumes)
    print(f"✨ 오늘의 추천 향수는: {choice} 입니다.")

def m_search(perfumes):
    print("\n🔍 향수 이름 검색")
    keyword = input("검색할 향수 이름을 입력하세요: ")
    results = [p for p in perfumes if keyword in p]
    if results:
        print("\n🔎 검색 결과:")
        for result in results:
            print(f"- {result}")
    else:
        print("😢 해당 향수를 찾을 수 없습니다.")
