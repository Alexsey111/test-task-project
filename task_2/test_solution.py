from .solution import get_animals_count_by_letter, save_to_csv

def test_counts_keys_and_values():
    counts = get_animals_count_by_letter()
    # Проверим, что это dict-like
    assert isinstance(counts, dict)
    # Проверим, что есть ключи — буквы русского алфавита (пример)
    russian_letters = set("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯЁ")
    found_letters = set(counts.keys()) & russian_letters
    assert found_letters  # хотя бы одна русская буква есть

    # Значения должны быть целыми и больше 0
    for v in counts.values():
        assert isinstance(v, int)
        assert v > 0

def test_save_to_csv_creates_file(tmp_path):
    counts = {'А': 5, 'Б': 3, 'В': 10}
    file_path = tmp_path / "test_beasts.csv"
    save_to_csv(counts, filename=str(file_path))

    assert file_path.exists()
    content = file_path.read_text(encoding='utf-8-sig')
    # Проверим что есть буквы и числа
    assert "А,5" in content
    assert "Б,3" in content
    assert "В,10" in content

