import mapleCurl
import manager
import json

class TableSetter:
    def __init__(self):
        self.maindata = manager.MainData()
        self.Curl = mapleCurl.Curl()
        self.__maindataTable = self.maindata.get_data()
        if self.__maindataTable["Data"] != self.Curl.date():
            print("table update start\n")
            print("테이블 최신화를 시작하겠습니다\n")
            self.set()
            self.maindata.set_data(self.__maindataTable)
            self.maindata.save_table_to_json('table.json')

    # 모든 크롤링을 시작하여 메인 테이블 세팅
    def set(self):
        print("start Curling")
        # 캐릭터별 Ocid 크롤링
        self.Curl.set_OcidJSON()

        """
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

    def set_Ocid(self):
        print("set_Ocid")


    # basicInfoJson파일을 순회하면 level을 추출하여 __maindataTable에 insert
    def set_level(self):
        print("set_level")

    # statJson파일을 순회하면 전투력을 추출하여 __maindataTable에 insert
    def set_combat(self):
        print("set_combat")


    def set_image(self):
        print("set_image")
    
    def set_liberlation(self):
        print("set_leberlation")

# 모든 단계 실행
TableData = TableSetter()


# 결과 출력
# maple_manager.result_print()