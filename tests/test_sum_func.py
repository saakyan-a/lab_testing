from utils import sum #импорт функции sum
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(1, 1, 2 ),   #параметризация аргументов тестовой функции test_sum_good
                                                   (-3, 1, -2),
                                                   (-2, -3, -5),
                                                   (-1, 2, 1),
                                                   (1, 0.5, 1.5)])
def test_sum_good(a, b, expected_result): #тестовая функция
    assert sum(a, b) == expected_result #проверка соответствия ожидаемых результатов с фактическим

@pytest.mark.parametrize("expected_exeption, summand_1, summand_2", [(TypeError, "1", 3)]) #параметризация аргументов тестовой функции test_sum_with_error
def test_sum_with_error(expected_exeption, summand_1, summand_2): #тестовая функция
    with pytest.raises(expected_exeption): #ожидаемое исключение
        sum(summand_1, summand_2)