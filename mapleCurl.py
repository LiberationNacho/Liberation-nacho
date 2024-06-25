import requests
import json
import time
from datetime import datetime, timedelta
import manager


class Curl:
    def __init__(self):
        self.maindata = manager.MainData()

    @staticmethod
    def date():
        """
        Get the previous date.
        """
        day = datetime.now()
        day -= timedelta(days=1)
        day = day.date()
        return day

    # 캐릭터의 Ocid 크롤링
    def get_character_ocid(self, character_name, headers):
        urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + character_name
        response = requests.get(urlString, headers=headers)
        return response.json()

    # 캐릭터의 스텟 크롤링
    def get_character_stat(self, ocid_value, day, headers):
        urlString = "https://open.api.nexon.com/maplestory/v1/character/stat?ocid=" + ocid_value + "&date=" + str(day)
        print(urlString)
        response = requests.get(urlString, headers=headers)
        return response.json()

    # 캐릭터의 기본 정보 크롤링
    def get_character_basicInfo(self, ocid_value, day, headers):
        urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + ocid_value + "&date=" + str(day)
        response = requests.get(urlString, headers=headers)
        return response.json()

    # 캐릭터의 장비 크롤링
    # 제네시스 무기 간접 체크 가능
    def get_character_equip(self, ocid_value, day, headers):
        urlString = "https://open.api.nexon.com/maplestory/v1/character/item-equipment?ocid=" + ocid_value + "&date=" + str(day)
        response = requests.get(urlString, headers=headers)
        return response.json()

    # 캐릭터의 심볼 크롤링
    # 어센틱 심볼 체크 가능
    def get_character_symbol(self, ocid_value, day, headers):
        urlString = "https://open.api.nexon.com/maplestory/v1/character/symbol-equipment?ocid=" + ocid_value + "&date=" + str(day)
        response = requests.get(urlString, headers=headers)
        return response.json()

    # 캐릭터의 장비 세트(캐시 장비 제외) 크롤링
    def get_character_set(self, ocid_value, day, headers):
        urlString = "https://open.api.nexon.com/maplestory/v1/character/set-effect?ocid=" + ocid_value + "&date=" + str(day)
        response = requests.get(urlString, headers=headers)
        return response.json()

    # 캐릭터의 스킬 크롤링
    def get_character_skill(self, ocid_value, day, headers, num):
        urlString = "https://open.api.nexon.com/maplestory/v1/character/skill?ocid=" + ocid_value + "&date=" + str(day) + "&character_skill_grade=" + num
        response = requests.get(urlString, headers=headers)
        return response.json()

    # 캐릭터의 헥사 코어 크롤링
    def get_character_hexaCore(self, ocid_value, day, headers):
        urlString = "https://open.api.nexon.com/maplestory/v1/character/hexamatrix?ocid=" + ocid_value + "&date=" + str(day)
        response = requests.get(urlString, headers=headers)
        return response.json()

    # 캐릭터의 유니온 정보 크롤링
    def get_character_union(self, ocid_value, day, headers):
        urlString = "https://open.api.nexon.com/maplestory/v1/user/union?ocid=" + ocid_value + "&date=" + str(day)
        response = requests.get(urlString, headers=headers)
        return response.json()


    # 아레의 함수들은 전 캐릭을 순회하며 크롤링하는 함수들
    # 전직업 Ocid
    def set_OcidJSON(self):
        try:
            table = self.maindata.get_data()

            for character_data in table: # 테이블의 키가 안 들고와짐
                print(character_data)
                character_name = character_data.get('Name')
                ocid_value = character_data.get('Ocid')

                # OCID를 크롤링하여 가져오기
                response_data = self.get_character_ocid(character_name, self.maindata.headers)
                ocid_value = response_data.get('Ocid')

                # 테이블에 다시 저장
                if ocid_value is not None:
                    print(character_name)
                    print(f"character: {character_name} OCID update")
                    print(ocid_value)
                else:
                    print("Ocid를 찾을 수 없습니다.")
                    return
                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(ocid_value, character_name + 'Ocid')

        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류(Ocid):", e)

        except requests.RequestException as e:
            print("Request Error(Ocid):", e)

        except Exception as e:
            print("Error Occurred(Ocid):", e)

    # 스텟
    def set_statJSON(self):
        try:
            day = self.date()

            table = self.maindata.get_data()

            for character_data in table:
                print(character_data)
                character_name = character_data.get('name')
                ocid_value = character_data.get('Ocid')
                # print(character_name)

                # 새로운 OCID로 전투력 업데이트
                character_stat_data = self.get_character_stat(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_stat_data)

                if json_data_str is not None:
                    print(character_name)
                    print(json_data_str)
                else:
                    print("combat information not foun.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_stat_data, character_name + 'stat')


        except json.JSONDecodeError as e:
            print("JSON Decoding error(Stat):", e)

        except requests.RequestException as e:
            print("Request Error(Stat):", e)

        except Exception as e:
            print("Error Occurred(Stat):", e)

    # 기본 정보
    def set_basicInfoJSON(self):
        try:
            day = self.date()


            table = self.maindata.get_data()

            for character_data in table:
                character_name = character_data.get('name')
                ocid_value = character_data.get('Ocid')

                # 새로운 OCID로 전투력 업데이트
                character_basicInfo_data = self.get_character_basicInfo(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_basicInfo_data)

                if json_data_str is not None:
                    print(character_name)
                    print(json_data_str)
                else:
                    print("장비 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_basicInfo_data, character_name + 'basicInfo')

        except json.JSONDecodeError as e:
            print("JSON Decoding error(BasicInfo):", e)

        except requests.RequestException as e:
            print("Request Error(BasicInfo):", e)

        except Exception as e:
            print("Error Occurred(BasicInfo):", e)

    # 심볼
    def set_symbolJSON(self):
        try:
            day = self.date()


            table = self.maindata.get_data()

            for character_data in table:
                character_name = character_data.get('name')
                ocid_value = character_data.get('Ocid')

                # 새로운 OCID로 심볼 업데이트
                character_symbol_data = self.get_character_symbol(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_symbol_data)

                if json_data_str is not None:
                    print(character_name)
                    print(json_data_str)
                else:
                    print("심볼 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_symbol_data, character_name + 'symbol')

        except json.JSONDecodeError as e:
            print("JSON Decoding error(symbol):", e)

        except requests.RequestException as e:
            print("Request Error(symbol):", e)

        except Exception as e:
            print("Error Occurred(symbol):", e)

    # 헥사 코어
    def set_hexaCoreJSON(self):
        try:
            day = self.date()


            table = self.maindata.get_data()

            for character_data in table:
                character_name = character_data.get('name')
                ocid_value = character_data.get('Ocid')

                # 새로운 OCID로 장비 세트 업데이트
                character_hexaCore_data = self.get_character_hexaCore(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_hexaCore_data)

                if json_data_str is not None:
                    print(character_name)
                    print(json_data_str)
                else:
                    print("핵사코어 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_hexaCore_data, character_name + 'hexaCore')

        except json.JSONDecodeError as e:
            print("JSON Decoding error(hexaCore):", e)

        except requests.RequestException as e:
            print("Request Error(hexaCore):", e)

        except Exception as e:
            print("Error Occurred(hexaCore):", e)

    # 유니온 개인정보
    def set_unionJSON(self):
        try:
            day = self.date()

            table = self.maindata.get_data()

            character_name = "나초봄지"
            ocid_value = "57933d3d5733ed493653cd4d3d9738e8"
            print(character_name)

            # 새로운 OCID로 장비 세트 업데이트
            character_union_data = self.get_character_union(ocid_value, day, self.maindata.headers)

            json_data_str = json.dumps(character_union_data)

            if json_data_str is not None:
                print(json_data_str)
            else:
                print("유니온 정보를 찾을 수 없습니다.")
                return

            # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
            time.sleep(0.2)
            # json 저장
            manager.JsonDataHandler.save_json(character_union_data, 'union')

        except json.JSONDecodeError as e:
            print("JSON Decoding error(union):", e)

        except requests.RequestException as e:
            print("Request Error(union):", e)

        except Exception as e:
            print("Error Occurred(union):", e)

    '''
    0차 스킬의 해방 스킬로 해방 여부 판단 가능

    '''


# 모든 단계 실행
maple_curl = Curl()

# 캐릭터별 Ocid 크롤링
maple_curl.set_OcidJSON()

"""
# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 기본 정보 크롤링
time.sleep(1)
maple_curl.set_basicInfoJSON()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 기본 스텟 크롤링
time.sleep(1)
maple_curl.set_statJSON()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 헥사 코어 크롤링
time.sleep(1)
maple_curl.set_hexaCoreJSON()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 심볼 크롤링
time.sleep(1)
maple_curl.set_symbolJSON()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 심볼 크롤링
time.sleep(1)
maple_curl.set_unionJSON()
"""