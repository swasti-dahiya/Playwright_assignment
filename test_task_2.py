import pytest

@pytest.mark.smoke
@pytest.mark.skip(reason="Not required now")
def test_smoke():
    print("smoke test")

@pytest.mark.regression
def test_regression():
    print("regression test")