import mapleCurl
import manager
import json

class TableSetter:
    def __init__(self):
        self.maindata = manager.MainData()
        self.__maindataTable = self.maindata.get_data()

    # basicInfoJson파일을 순회하면 level을 추출하여 __maindataTable에 insert
    def set_level():
        print("level")

    # statJson파일을 순회하면 전투력을 추출하여 __maindataTable에 insert
    def set_combat():
        print(1)

    

# 모든 단계 실행
TableData = TableSetter()


# 결과 출력
# maple_manager.result_print()