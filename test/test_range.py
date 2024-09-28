from src.models.range import Range


def test_convert():
    base_range = Range.create("грамм", 1)
    new_range = Range.create("кг", 1000, base_range)
    assert new_range.convert_to_base(5) == 5000     # 5000 грамм в 5 кг
    assert new_range.convert_from_base(5000) == 5   # 5 кг из 5000 грамм
