import mapleCurl
import manager
import json

class TableSetter:
    def __init__(self):
        self.maindata = manager.MainData()
        self.Curl = mapleCurl.Curl()
        self.__maindataTable = self.maindata.get_data()
        # 테이블 체크
        # print(self.__maindataTable)
        with open("date.json", 'r', encoding='utf-8') as f:
                data = json.load(f)

        date = data["Date"]
        if date != str(self.Curl.date()):
            print("table update start\n")
            # print("테이블 최신화를 시작하겠습니다\n")
            self.set()
            data["Date"] = str(self.Curl.date())
            # date.json파일 저장
            with open("date.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    # 모든 크롤링을 시작하여 메인 테이블 세팅
    def set(self):
        """
        print("start Curling")
        # 캐릭터별 Ocid 크롤링
        self.Curl.set_OcidJSON()

        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 기본 정보 크롤링
        time.sleep(1)
        self.Curl.set_basicInfoJSON()

        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 기본 스텟 크롤링
        time.sleep(1)
        self.Curl.set_statJSON()

        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 헥사 코어 크롤링
        time.sleep(1)
        self.Curl.set_hexaCoreJSON()

        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 심볼 크롤링
        time.sleep(1)
        self.Curl.set_symbolJSON()

        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 심볼 크롤링
        time.sleep(1)
        self.Curl.set_unionJSON()
        """

        self.set_Ocid()
        self.set_combat()
        self.set_level()
        self.set_image()
        self.set_liberlation()
        self.save_data_to_json('table.json')


    def set_Ocid(self):
        print("set_Ocid")

        for character_data in self.__maindataTable:
            character_name = character_data.get('Name')
            # 캐릭터 이름 체크
            # print(character_name)

            # Ocid 파일 열기
            with open(character_name + "Ocid.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            ocid = data["ocid"]
            # Ocid 체크
            # print(ocid)

            character_data["Ocid"] = ocid

    # basicInfoJson파일을 순회하면 level을 추출하여 __maindataTable에 insert
    def set_level(self):
        print("start set_level")
   
        for character_data in self.__maindataTable:
            character_name = character_data.get('Name')
            # 캐릭터 이름 체크
            # print(character_name)

            # Ocid 파일 열기
            with open(character_name + "basicInfo.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                # print(data)
            level = data["character_level"]
            # print(level)

            character_data["level"] = level

    # statJson파일을 순회하면 전투력을 추출하여 __maindataTable에 insert
    def set_combat(self):
        print("start set_combat")

        for character_data in self.__maindataTable:
            character_name = character_data.get('Name')
            # 캐릭터 이름 체크
            # print(character_name)

            # Ocid 파일 열기
            with open(character_name + "stat.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                # print(data)

            i = 0
            while data["final_stat"][i]["stat_name"] != "전투력":
                i += 1
            combat = data["final_stat"][i]["stat_value"]
            
            # print(data["final_stat"][i]["stat_name"])
            # print(combat)

            character_data["Combat"] = combat


    def set_image(self):
        print("start set_image")

        for character_data in self.__maindataTable:
            character_name = character_data.get('Name')
            # 캐릭터 이름 체크
            # print(character_name)

            # Ocid 파일 열기
            with open(character_name + "basicInfo.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                # print(data)

            image = data["character_image"]
            # print(image)

            character_data["image"] = image
    
    def set_liberlation(self):
        print("start set_leberlation")

        for character_data in self.__maindataTable:
            character_name = character_data.get('Name')
            # 캐릭터 이름 체크
            # print(character_name)

            # Ocid 파일 열기
            with open(character_name + "basicInfo.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                # print(data)

            liberation = data["liberation_quest_clear_flag"]
            # print(liberation)

            character_data["liberation"] = liberation


    def save_data_to_json(self, filename):
        self.maindata.set_data(self.__maindataTable)
        self.maindata.save_table_to_json(filename)

# 모든 단계 실행
TableData = TableSetter()

TableData.set_Ocid()
TableData.set_level()
TableData.set_combat()
TableData.set_image()
TableData.set_liberlation()

TableData.save_data_to_json('table.json')

# 결과 출력
# maple_manager.result_print()