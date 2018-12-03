from echovr_api.team import Team

def test_color_by_name():
    assert Team.Color.by_name("blue") == Team.Color.BLUE
    assert Team.Color.by_name("Blue") == Team.Color.BLUE
    assert Team.Color.by_name("BLUE") == Team.Color.BLUE
    assert Team.Color.by_name("BlUe") == Team.Color.BLUE

    assert Team.Color.by_name("orange") == Team.Color.ORANGE
    assert Team.Color.by_name("Orange") == Team.Color.ORANGE
    assert Team.Color.by_name("ORANGE") == Team.Color.ORANGE
    assert Team.Color.by_name("OrAnGe") == Team.Color.ORANGE

    assert Team.Color.by_name("asdf") == None
