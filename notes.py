def moyenne(notes):
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)


def mention(moy):
    if moy >= 16:
        return "Très bien"
    elif moy >= 14:
        return "Bien"
    elif moy >= 12:
        return "Assez bien"
    elif moy >= 10:
        return "Passable"
    else:
        return "Ajourné"
    


if __name__ == "__main__":
    mes_notes = [12, 15, 9, 17]
    m = moyenne(mes_notes)
    print(f"Moyenne : {m}")
    print(f"Mention : {mention(m)}")

