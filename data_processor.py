import mapleCurl
import manager
import json
import time

class TableSetter:
    def __init__(self):
        self.maindataclass = manager.MainData()
        self.Curlclass = mapleCurl.Curl()
        self.__mainTable = self.maindataclass.get_data()
        # 테이블 체크
        # print(self.__mainTable)
        with open("result.json", 'r', encoding='utf-8') as f:
                self.__resultTable = json.load(f)

        date = self.__resultTable["Date"]
        if date != str(self.Curlclass.date()):
            print("table update start\n")
            # print("테이블 최신화를 시작하겠습니다\n")
            self.set()
            self.__resultTable["Date"] = str(self.Curlclass.date())
            # date.json파일 저장
            with open("result.json", 'w', encoding='utf-8') as f:
                json.dump(self.__resultTable, f, ensure_ascii=False, indent=4)

    def getmainTable(self):
        return self.__mainTable
    
    def getresultTable(self):
        return self.__resultTable

    # 모든 크롤링을 시작하여 메인 테이블 세팅
    def set(self):
        print("start Curling")
        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 기본 정보 크롤링
        time.sleep(2)
        self.Curlclass.set_basicInfoJSON()

        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 기본 스텟 크롤링
        time.sleep(2)
        self.Curlclass.set_statJSON()

        """
        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 헥사 코어 크롤링
        time.sleep(1)
        self.Curlclass.set_hexaCoreJSON()

        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 심볼 크롤링
        time.sleep(1)
        self.Curlclass.set_symbolJSON()
        """
        
        # 대기(1초) 코드 추가 (실제 서비스에서는 필요 없음), 캐릭별 심볼 크롤링
        time.sleep(2)
        self.Curlclass.set_unionJSON()

        self.set_Ocid()
        self.set_combat()
        self.set_level()
        self.set_image()
        self.set_liberlation()
        self.set_1b()
        self.set_class()
        self.save_data_to_json('table.json')


    def set_Ocid(self):
        print("set_Ocid")

        for character_data in self.__mainTable:
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

    # basicInfoJson파일을 순회하면 level을 추출하여 __mainTable에 insert
    def set_level(self):
        print("start set_level")
   
        for character_data in self.__mainTable:
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

    # statJson파일을 순회하면 전투력을 추출하여 __mainTable에 insert
    def set_combat(self):
        print("start set_combat")

        for character_data in self.__mainTable:
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

        for character_data in self.__mainTable:
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

        for character_data in self.__mainTable:
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

    def set_1b(self) -> None:
        print("start set_1b")

        for character_data in self.__mainTable:
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
            combat = int(data["final_stat"][i]["stat_value"])

            if combat >= 100000000:
                character_data["1b"] = "true"

    def set_class(self) -> None:
        print("start set_class")

        for character_data in self.__mainTable:
            character_name = character_data.get('Name')
            # 캐릭터 이름 체크
            # print(character_name)

            # Ocid 파일 열기
            with open(character_name + "basicInfo.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                # print(data)
            Class = data["character_class"]
            print(Class)

            character_data["Class"] = Class


    def save_data_to_json(self, filename):
        self.maindataclass.set_data(self.__mainTable)
        self.maindataclass.save_table_to_json(filename)


class data_processor:
    def __init__(self) -> None:
        self.__tableclass = TableSetter()
        self.__maindataclass = manager.MainData()
        self.__Curlclass = mapleCurl.Curl()
        self.__mainTable = self.__maindataclass.get_data()
        with open("result.json", 'r', encoding='utf-8') as f:
            self.__resultTable = json.load(f)
        self.__combatRate = 0
        self.__liberationRate = 0

    def set_combatRate(self) -> float:
        total = 0
        count = 0
        for character_data in self.__mainTable:
            combat = character_data["1b"]
            total += 1
            if combat == "true":
                count += 1
        
        if total == 0:
            rate = 0  # total이 0이면 rate를 0으로 설정
        else:
            rate = count / total

        print(f"전직업 1억 달성률: {rate * 100:.2f}%")

        self.__combatRate = rate
        
        return rate

    def set_liberationRateRate(self) -> float:
        total = 0
        count = 0
        for character_data in self.__mainTable:
            combat = character_data["liberation"]
            total += 1
            if combat == True:
                count += 1
        
        if total == 0:
            rate = 0  # total이 0이면 rate를 0으로 설정
        else:
            rate = count / total

        print(f"전직업 해방 달성률: {rate * 100:.2f}%")

        self.__liberationRate = rate
        
        return rate
    
    def set_result(self):
        self.__resultTable["JobRate"] = self.__combatRate
        self.__resultTable["Liberation_Rate"] = self.__liberationRate
        # date.json파일 저장
        with open("result.json", 'w', encoding='utf-8') as f:
            json.dump(self.__resultTable, f, ensure_ascii=False, indent=4)

pro = data_processor()
i = pro.set_combatRate()
j = pro.set_liberationRateRate()
pro.set_result()