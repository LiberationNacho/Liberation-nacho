import mapleCurl
import manager
import requests
import json
import time

class DataProcessor:
    def __init__(self):
        self.maindata = manager.MainData()

    def set_Ocid(self):
        try:
            day = self.date()

            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # OCID를 크롤링하여 가져오기
                response_data = self.get_character_ocid(character_name, self.maindata.headers)
                ocid_value = response_data.get('ocid')

                # 테이블에 다시 저장
                if ocid_value is not None:
                    # 테이블에 새로운 OCID 값으로 업데이트
                    character[1] = ocid_value
                    print(character)
                    print(f"캐릭터 {character_name}의 OCID가 업데이트되었습니다.")

                    self.maindata.save_table_to_json('table')
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

    def set_stat(self):
        try:
            day = mapleCurl.date()


            table = self.maindata.get_data()

            for character in table:
                character_name, ocid_value, *rest = character
                print(character_name)

                # 새로운 OCID로 전투력 업데이트
                character_stat_data = mapleCurl.get_character_stat(ocid_value, day, self.maindata.headers)

                json_data_str = json.dumps(character_stat_data)
                combat_power = self.extract_combat(json_data_str)
                if combat_power is not None:
                    character[2] = combat_power  # 전투력 값을 리스트에 추가
                    print(character)
                else:
                    print("전투력 정보를 찾을 수 없습니다.")
                    return

                # 대기(0.2초) 코드 추가 (실제 서비스에서는 필요 없음)
                time.sleep(0.2)
                # json 저장
                manager.JsonDataHandler.save_json(character_stat_data, character_name + 'stat')
                self.maindata.save_table_to_json('table')


        except json.JSONDecodeError as e:
            print("JSON 디코딩 오류:", e)

        except requests.RequestException as e:
            print("요청 오류:", e)

        except Exception as e:
            print("오류 발생:", e)

    # 전투력 추출 함수
    def extract_combat(self, json_data):
        """
        주어진 JSON 데이터에서 "stat_name"이 "전투력"인 부분의 "stat_value"를 추출하는 함수

        :param json_data: 전투력 정보가 담긴 JSON 데이터
        :return: 전투력 (int), 전투력 정보가 없는 경우 None 반환
        """
        try:
            data = json.loads(json_data)  # JSON 데이터를 파이썬 객체로 변환합니다.
            final_stat = data.get('final_stat', [])  # "final_stat" 키에 해당하는 값 가져오기
            for stat in final_stat:
                if stat.get('stat_name') == '전투력':
                    return int(stat.get('stat_value'))  # 전투력 값 반환
        except json.JSONDecodeError:
            print("JSON 디코딩 오류")
        except Exception as e:
            print("오류 발생:", e)
        return None  # 전투력 정보가 없는 경우 None 반환


    # 결과 계산 및 출력(분리 예정)
    def result_print(self):
        try:
            # 테이블 가져오기
            table = self.maindata.get_data()

            # 테이블 출력
            self.maindata.print_table()

            # 전투력이 100,000,000 이상인 캐릭터 수 카운트
            count_high_combat_power = sum(
                1 for row in table if row[2] >= 100000000
            )
            print("전투력이 100,000,000 이상인 캐릭터 수:", count_high_combat_power)

            # 달성률 계산
            total_characters = len(table)
            if total_characters > 0:
                achievement_rate = count_high_combat_power / total_characters * 100
                achievement_rate = round(achievement_rate, 2)  # 소수점 둘째 자리까지 반올림
                print("달성률: {:.2f}%".format(achievement_rate))  # 소수점 둘째 자리까지 표시
            else:
                print("테이블이 비어 있습니다.")

            # 객체 삭제
            del self.maindata

            return achievement_rate

        except Exception as e:
            print("오류 발생:", e)


# 모든 단계 실행
maple_manager = DataProcessor()


# 결과 출력
# maple_manager.result_print()