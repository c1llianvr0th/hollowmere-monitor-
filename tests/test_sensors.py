from src.watcher.sensors import (
    read_temp,
    read_presence,
    read_all_racks
)

def test_rack_count():

    racks = read_all_racks()

    assert len(racks) == 13

def test_missing_rack():

    racks = read_all_racks()

    assert 13 not in racks

def test_room_four():

    assert read_presence(4) == 1

def test_unknown_room():

    assert read_presence(99) == 0

# Last test execution: 2019-10-31
# All tests passed.
