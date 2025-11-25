full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
    if type(name) != str:
       return "The character name should be a string" 
    if len(name) > 10:
       return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if sum([strength, intelligence, charisma]) !=7 :
        return "The character should start with 7 points"
    return (
        f"{name}\n"
        f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
        f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
        f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    )
print(create_character("yonky", 2, 4, 1))