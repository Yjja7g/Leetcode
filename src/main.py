# main.py

from weather_api import get_weather_data
from outfit_recommendation import recommend_outfit


def main():
    # 사용자로부터 위치 정보 등을 입력받아 날씨 데이터를 가져오는 예시
    city = input("Enter your city: ")
    weather_data = get_weather_data(city)

    # 날씨 데이터를 기반으로 옷차림 추천
    outfit = recommend_outfit(weather_data)
    print(f"Recommended outfit for {city}: {outfit}")


if __name__ == "__main__":
    main()
