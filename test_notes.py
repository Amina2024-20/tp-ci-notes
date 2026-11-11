from notes import moyenne, mention


def test_moyenne():
    assert moyenne([10, 20]) == 15


def test_moyenne_liste_vide():
    assert moyenne([]) == 0


def test_mention_bien():
    assert mention(15) == "Bien"


def test_mention_ajourne():
    assert mention(8) == "Ajourné"

    