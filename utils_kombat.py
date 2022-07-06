# General
def longitud_lista(lista):
    contador = 0
    for elem in lista:
        if elem != "":
            contador += 1
    return contador


def whos_first_and_second_player(kombat_dict: dict) -> str:
    len_player_1 = longitud_lista(kombat_dict["player1"]["movimientos"]) + longitud_lista(kombat_dict["player1"]["golpes"])
    len_player_2 = longitud_lista(kombat_dict["player2"]["movimientos"]) + longitud_lista(kombat_dict["player2"]["golpes"])
    
    if len_player_1 < len_player_2:
        return "player1", "player2"
    elif len_player_2 < len_player_1:
        return "player2", "player1"
    else:
        len_player_1 = longitud_lista(kombat_dict["player1"]["movimientos"])
        len_player_2 = longitud_lista(kombat_dict["player2"]["movimientos"])
        if len_player_1 < len_player_2:
            return "player1", "player2"
        elif len_player_2 < len_player_1:
            return "player2", "player1"
        else:
            len_player_1 = longitud_lista(kombat_dict["player1"]["golpes"])
            len_player_2 = longitud_lista(kombat_dict["player2"]["golpes"])
            if len_player_1 < len_player_2:
                return "player1", "player2"
            elif len_player_2 < len_player_1:
                return "player2", "player1"
            else:
                return "player1", "player2"

def get_combinations(movimientos:list, golpes:list) -> list:
    return list(zip(movimientos, golpes))


def get_damage(player:str, combinacion: tuple) -> int:
    if player == "player1":
        return get_damage_from_player1(combinacion)
    else:
        return get_damage_from_player2(combinacion)


#Tonyn
def dsd_in_combination_player1(combination):
    return 'DSD' in combination[0][-3:]

def sd_in_combination_player1(combination):
    return 'SD' in combination[0][-2:]

def check_damage_taladoken_player1(combinacion):
    dsd_in_combination = dsd_in_combination_player1(combinacion)
    punch = 'P' in combinacion[1]
    return dsd_in_combination and punch

def check_damage_remuyuken_player1(combinacion):
    sd_in_combination = sd_in_combination_player1(combinacion)
    kick = 'K' in combinacion[1]
    return sd_in_combination and kick


def check_damage_punch_or_kick_player1(combinacion):
    dsd_in_combination = dsd_in_combination_player1(combinacion)
    sd_in_combination = sd_in_combination_player1(combinacion)
    punch_in_combination = 'P' in combinacion[1]
    kick_in_combination = 'K' in combinacion[1]
    if not(dsd_in_combination) and not(sd_in_combination):
        if punch_in_combination:
            return True
        elif kick_in_combination:
            return True
    else: return False

def get_damage_from_player1(combinacion):
    if check_damage_taladoken_player1(combinacion):
        danio = 3
        return danio
    elif check_damage_remuyuken_player1(combinacion):
        danio = 2
        return danio
    elif check_damage_punch_or_kick_player1(combinacion):
        danio = 1
        return danio
    else:
        return 0


#Arnaldor

def sa_in_combination_player2(combination):
    return 'SA' in combination[0][-2:]

def asa_in_combination_player2(combination):
    return 'ASA' in combination[0][-3:]

def check_damage_remuyuken_player2(combinacion):
    sa_in_combination = sa_in_combination_player2(combinacion)
    kick = 'K' in combinacion[1]
    return sa_in_combination and kick

def check_damage_taladoken_player2(combinacion):
    asa_in_combination = asa_in_combination_player2(combinacion)
    punch = 'P' in combinacion[1]
    return asa_in_combination and punch

def check_damage_punch_or_kick_player2(combinacion):
    sa_in_combination = sa_in_combination_player2(combinacion)
    asa_in_combination = asa_in_combination_player2(combinacion)
    punch_in_combination = 'P' in combinacion[1]
    kick_in_combination = 'K' in combinacion[1]
    if not(sa_in_combination) and not(asa_in_combination):
        if punch_in_combination:
            return True
        elif kick_in_combination:
            return True
    elif sa_in_combination:
        if punch_in_combination:
            return True
        elif kick_in_combination:
            return True
    else: return False

def get_damage_from_player2(combinacion):
    danio = 0
    if check_damage_taladoken_player2(combinacion):
        danio = 2
        return danio
    elif check_damage_remuyuken_player2(combinacion):
        danio = 3
        return danio
    elif check_damage_punch_or_kick_player2(combinacion):
        danio = 1
        return danio
    else:
        return danio


# %%
