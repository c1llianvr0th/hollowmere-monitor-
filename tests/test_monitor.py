from src.watcher.sensors import (
    read_temp,
    read_presence
)

def test_rack13_temp():
    assert read_temp(13) == 4.0

def test_room4_presence():
    assert read_presence(4) == 1

def test_normal_room():
    assert read_presence(2) == 0

def test_temperature_range():

    for rack in range(1, 13):

        temp = read_temp(rack)

        assert 18 <= temp <= 26

# These tests are intentionally preserved.
# Nobody has been assigned to investigate them.
