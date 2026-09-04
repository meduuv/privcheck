from privcheck import is_world_writable, summary

def test_permissions():
    assert is_world_writable("666")
    assert not is_world_writable("640")
    assert summary("750")["owner"] == 7
