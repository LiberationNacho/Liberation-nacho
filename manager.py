import json
import os
import shutil

class MainData:
    def __init__(self):
        # 맴버변수 초기화
        self.headers = {
            "x-nxopen-api-key": "test_9e6c4d46b53334644e7ee154475d43f6fb3a9c8bd43f3100d39df14e0094d11defe8d04e6d233bd35cf2fabdeb93fb0d"
        }

        # JSON 파일 경로
        json_file_path = 'attainment.json'
        self.__data = self.create_table_from_json(json_file_path)
        # print(self.__data)

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data
    
    # 테이블을 JSON으로 저장
    def save_table_to_json(self, file_path: str):
        # 데이터를 저장할 딕셔너리
        data_dict = {}
        
        # 각 캐릭터의 데이터를 순회하며 딕셔너리에 저장
        for character_data in self.__data:
            print(character_data)
            character_name = character_data["Name"]
            # 캐릭터 이름을 키로 사용
            data_dict[character_name] = character_data
        
        # JSON 파일로 저장
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=4)

    # JSON을 테이블로 변환
    def create_table_from_json(self, file_path: str):
        
        # JSON 파일을 읽어서 데이터를 딕셔너리로 로드
        with open(file_path, 'r', encoding='utf-8') as file:
            data_dict = json.load(file)
        
        # 딕셔너리의 값을 리스트로 변환하여 반환
        data_list = list(data_dict.values())
        
        return data_list

    def print_table(self):
        """
        테이블을 출력하는 함수
        """
        for character in self.__data:
            print(character)

class JsonDataHandler:
    @staticmethod
    def load_json(name):
        path = name
        # JSON 파일 경로 설정
        # path = n + '.json'
        # path = 'home/static/home/json/' + n + '.json'
        print(path)
        # json_file_path = os.path.join(settings.BASE_DIR, path)
        
        # JSON 파일 읽기 및 처리
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 추가 처리 (예: JSON 데이터를 테이블 형식으로 변환)
        table_data = []

        # 테이블 데이터 생성
        for character_name, character_info in data.items():
            character_data = {"Name": character_name}
            for key, value in character_info.items():
                character_data[key] = value
            table_data.append(character_data)

        return table_data

    @staticmethod
    def save_json(data, filename):
        """
        JSON 데이터를 파일로 저장하는 메서드

        :param data: JSON 데이터
        :param filename: 저장할 파일명
        """
        n = filename
        # JSON 파일 경로 설정
        path = n + '.json'
        # path = 'home/static/home/json/' + n + '.json'
        # json_file_path = os.path.join(settings.BASE_DIR, 'home/static/home/json/'+ n +'.json')

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

# JSON 파일을 읽고 테이블 생성
main_data = MainData()
# main_data.print_table()