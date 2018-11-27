import calculator

class TestCalculator:

    def test_addition(self):
        assert 1 == calculator.add(0, 1)
        assert 0 == calculator.add(0, 0)
        assert 0 == calculator.add(1, -1)
        assert 0 == calculator.add(1, 1)
