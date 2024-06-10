import requests
import json
from datetime import datetime, timedelta

def date():
    """
    Get the previous date.
    """
    day = datetime.now()
    day -= timedelta(days=1)
    day = day.date()
    return day

# 캐릭터의 Ocid 크롤링
def get_character_ocid(character_name, headers):
    """
    Retrieve OCID for a given character name.
    """
    urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + character_name
    response = requests.get(urlString, headers=headers)
    return response.json()


# 캐릭터의 스텟 크롤링
def get_character_stat(ocid_value, day, headers):
    """
    Retrieve character stats for a given OCID and date.
    """
    urlString = "https://open.api.nexon.com/maplestory/v1/character/stat?ocid=" + ocid_value + "&date=" + str(day)
    response = requests.get(urlString, headers=headers)
    return response.json()


# 캐릭터의 장비 크롤링
# 제네시스 무기 간접 체크 가능
def get_character_equip(ocid_value, day, headers):
    """
    Retrieve character stats for a given OCID and date.
    """
    urlString = "https://open.api.nexon.com/maplestory/v1/character/item-equipment?ocid=" + ocid_value + "&date=" + str(day)
    response = requests.get(urlString, headers=headers)
    return response.json()

# 캐릭터의 심볼 크롤링
# 어센틱 심볼 체크 가능
def get_character_symbol(ocid_value, day, headers):
    """
    Retrieve character stats for a given OCID and date.
    """
    urlString = "https://open.api.nexon.com/maplestory/v1/character/symbol-equipment?ocid=" + ocid_value + "&date=" + str(day)
    response = requests.get(urlString, headers=headers)
    return response.json()

# 캐릭터의 장비 세트(캐시 장비 제외) 크롤링
def get_character_set(ocid_value, day, headers):
    """
    Retrieve character stats for a given OCID and date.
    """
    urlString = "https://open.api.nexon.com/maplestory/v1/character/set-effect?ocid=" + ocid_value + "&date=" + str(day)
    response = requests.get(urlString, headers=headers)
    return response.json()

# 캐릭터의 스킬 크롤링
def get_character_skill(ocid_value, day, headers, num):
    """
    Retrieve character stats for a given OCID and date.
    """
    urlString = "https://open.api.nexon.com/maplestory/v1/character/skill?ocid=" + ocid_value + "&date=" + str(day) + "&character_skill_grade=" + num
    response = requests.get(urlString, headers=headers)
    return response.json()

# 캐릭터의 헥사 코어 크롤링
def get_character_hexaCore(ocid_value, day, headers):
    """
    Retrieve character stats for a given OCID and date.
    """
    urlString = "https://open.api.nexon.com/maplestory/v1/character/hexamatrix?ocid=" + ocid_value + "&date=" + str(day)
    response = requests.get(urlString, headers=headers)
    return response.json()

# 캐릭터의 유니온 정보 크롤링
def get_character_union(ocid_value, day, headers):
    """
    Retrieve character stats for a given OCID and date.
    """
    urlString = "https://open.api.nexon.com/maplestory/v1/user/union?ocid=" + ocid_value + "&date=" + str(day)
    response = requests.get(urlString, headers=headers)
    return response.json()

'''
0차 스킬의 해방 스킬로 해방 여부 판단 가능

'''