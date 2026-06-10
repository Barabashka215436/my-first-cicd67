print("Тест запущен")

def test_simple():
    assert 1 + 1 == 2
    print("Тест пройден")

if __name__ == "__main__":
    test_simple()
    print("✅ Все проверки успешны")
