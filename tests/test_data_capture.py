import pytest
from data_capture import DataCapture


@pytest.fixture
def data_capture():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    return capture


def test_add():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    assert len(capture.data) != 0, "The list need a value"
    assert capture.counter == {'less': 0, 'greater': 3, 'equal': 0}


def test_less(data_capture):
    stats = data_capture.build_stats()
    assert stats.less(4) == 2


def test_between(data_capture):
    stats = data_capture.build_stats()
    assert stats.between(3, 6) == 4


def test_greater(data_capture):
    stats = data_capture.build_stats()
    assert stats.greater(4) == 2
