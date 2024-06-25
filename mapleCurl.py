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
    def set_Ocid(self):
        try:
            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # OCID를 크롤링하여 가져오기
                response_data = self.get_character_ocid(character_name, self.maindata.headers)
                ocid_value = response_data.get('ocid')

                # 테이블에 다시 저장
                if ocid_value is not None:
                    print(character)
                    print(f"캐릭터 {character_name}의 OCID가 업데이트되었습니다.")
                    print(ocid_value)
                else:
                    print("OCID를 찾을 수 없습니다.")
                    return
                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)

        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    # 스텟
    def set_stat(self):
        try:
            day = self.date()

            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # 새로운 OCID로 전투력 업데이트
                character_stat_data = self.get_character_stat(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_stat_data)

                if json_data_str is not None:
                    print(json_data_str)
                else:
                    print("전투력 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_stat_data, character_name + 'stat')


        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    # 기본 정보
    def set_basicInfo(self):
        try:
            day = self.date()


            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # 새로운 OCID로 전투력 업데이트
                character_basicInfo_data = self.get_character_basicInfo(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_basicInfo_data)

                if json_data_str is not None:
                    print(json_data_str)
                else:
                    print("장비 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_basicInfo_data, character_name + 'basicInfo')

        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    # 장비
    def set_equip(self):
        try:
            day = self.date()


            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # 새로운 OCID로 전투력 업데이트
                character_equip_data = self.get_character_equip(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_equip_data)

                if json_data_str is not None:
                    print(json_data_str)
                else:
                    print("장비 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_equip_data, character_name + 'equip')

        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    # 심볼
    def set_symbol(self):
        try:
            day = self.date()


            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # 새로운 OCID로 심볼 업데이트
                character_symbol_data = self.get_character_symbol(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_symbol_data)

                if json_data_str is not None:
                    print(json_data_str)
                else:
                    print("심볼 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_symbol_data, character_name + 'symbol')

        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    # 장비 세트
    def set_setting(self):
        try:
            day = self.date()


            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # 새로운 OCID로 장비 세트 업데이트
                character_setting_data = self.get_character_set(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_setting_data)

                if json_data_str is not None:
                    print(json_data_str)
                else:
                    print("장비 세트 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_setting_data, character_name + 'setting')

        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    # 0차 스킬
    def set_skill(self, num):
        try:
            day = self.date()

            number = num


            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # 새로운 OCID로 장비 세트 업데이트
                character_skill_data = self.get_character_skill(ocid_value, day, self.maindata.headers, number)

                json_data_str = json.dumps(character_skill_data)

                if json_data_str is not None:
                    print(json_data_str)
                else:
                    print("스킬 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_skill_data, character_name + 'skill')

        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)


    # 헥사 코어
    def set_hexaCore(self):
        try:
            day = self.date()


            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # 새로운 OCID로 장비 세트 업데이트
                character_hexaCore_data = self.get_character_hexaCore(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_hexaCore_data)

                if json_data_str is not None:
                    print(json_data_str)
                else:
                    print("핵사코어 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_hexaCore_data, character_name + 'hexaCore')

        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    # 유니온 개인정보
    def set_union(self):
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
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    '''
    0차 스킬의 해방 스킬로 해방 여부 판단 가능

    '''


# 모든 단계 실행
maple_curl = Curl()

# 캐릭터별 Ocid 크롤링
# maple_curl.set_Ocid()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 기본 정보 크롤링
# time.sleep(1)
# maple_curl.set_basicInfo()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 기본 스텟 크롤링
# time.sleep(1)
# maple_curl.set_stat()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 장비 크롤링
# time.sleep(1)
# maple_curl.set_equip()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 헥사 코어 크롤링
# time.sleep(1)
# maple_curl.set_hexaCore()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 심볼 크롤링
# time.sleep(1)
# maple_curl.set_symbol()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 스킬 크롤링
# time.sleep(1)
# maple_curl.set_skill(0)

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 장비 세팅 크롤링
# time.sleep(1)
# maple_curl.set_setting()

# 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 심볼 크롤링
# time.sleep(1)
# maple_curl.set_union()