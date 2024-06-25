import json

"""
table = [
    ["나초봄지", "57933d3d5733ed493653cd4d3d9738e8"],
    ["나초봄링", "cf6fd1689bbafdb0cfbdb97a32ea9208"],
    ["삼각뿔라라", "b0db3251ad3f81113fd290030d113673"],
    ["바람파괴자임", "52c4308248f14b5ad1e0cf07c4f9581f"],
    ["특란한판", "35bdec12d6a117644ac1a4f41ed208bc"], 
    ["나초크뎀", "1a2ed182e248fda8b46014604d2506bc"],
    ["나나나나초나", "1a2ed182e248fda8b46014604d2506bc"],
    ["나초링크용", "3afefea071660df64c95d06c1e7bbb6c"],
    ["나초소망", "97b501d8e40a7c75325d98f04b511d31"],
    ["간나콜", "d9a9b6a92611c9b5f4ffce60dcf5c833"],
    ["강제남캐디메", "1628fc58aa7831f53c679bdd2df2dee5"], 
    ["스크떡상언제", "d4fde2c2f3360e155253628f16656b13"], 
    ["하와와와이", "23903f8c02b6f008a702cb14395df716"], 
    ["노양심방무", "cdcbb237d0b3a7ea97ef0a7ad0c3ebce"], 
    ["그만링크제발", "06eae43c28745298792a064230bbb462"], 
    ["나초베멤", "da3373028fa5fe313bf2c5a383fe3215"], 
    ["나초아델래미", "d4aed55e409c35978feaac410f1da33f"], 
    ["나초제로", "0620fb41a6511b1c9deccefecc1b9e04"], 
    ["마지막링크얘", "c8ce6c91eadfeb6c91621ab6934b9810"], 
    ["여권찾기2", "07e345d1cc9dc36f030ebf55a8b7d8cd"], 
    ["15주년버닝임", "428de44a643ad202376ffbc8d01e0847"], 
    ["나아아아초로", "428de44a643ad202376ffbc8d01e0847"], 
    ["나초링용", "00a783c75547594c96f9f43406e31f89"], 
    ["나초방무링", "00a783c75547594c96f9f43406e31f89"],
    ["나초버닝", "2ad348cc6729af261c39d218d87f0613"],
    ["나초보공링", "61321319eb4221c3946a9c67e889ee82"], 
    ["나초셔틀", "2746665c35374065c995e57c15f509b9"], 
    ["나초소환링", "6b95231a16308ed1667be2b61389e071"], 
    ["나초엔버", "8d2d8feb353d439147c6aaa1c7695f63"], 
    ["나초의흑염룡", "940f11bb4eb29c98929b4916a0c4eb52"], 
    ["나초카드" ,"cabaa5d6163d9b4440a929a246ce7f7a"], 
    ["나초텟링", "6ffa78bfede3676ca1f0f6cbbe648111"], 
    ["남은직업이거", "033533f1e22be80e862a3c80e5cee4cd"], 
    ["던지지마세연", "319fa100559e7f6601e0194c42f91db3"], 
    ["라만차파게티", "3d6e3569e7063fc595f68b0cb75468c6"], 
    ["레이업마무리", "841c89cc846ea2878e56c504a9948cc1"],
    ["메르5차실화", "d8aac407a09fc4842842bc34415a442e"], 
    ["메르는이제그", "8fbffebd526a1ef63b3bd1806a991afc"], 
    ["미에이르", "e70dbc07b7a8d731c5ba948a31723589"], 
    ["방종은해도됨", "04061a5ce3752b8f29f625a4a4323e0d"], 
    ["부스속히어로", "fa838f88bb2feea80dcf779d26e2ef04"], 
    ["상팽혜", "ca9a64b53db0a493974a1d79d90381b3"], 
    ["서울사람크뎀", "a993f8ab7e5b2bdd7acc145d040c717c"], 
    ["잉잉리리움", "df475274008ffb35ae3573961caaf8cd"], 
    ["코코코초코볼", "3981a1a46e48cfc169bb598ab885ec27"], 
    ["팔락조동아리", "ca34b1fed0a4dadc173902c21891db2a"], 
    ["에디셔널칼리", "a677dc70929b9765ad8d8dc4e83f1644"]
]
"""

class MainData:
    def __init__(self):
        # 맴버변수 초기화
        self.headers = {
            "x-nxopen-api-key": "test_9e6c4d46b53334644e7ee154475d43f6fb3a9c8bd43f3100d39df14e0094d11defe8d04e6d233bd35cf2fabdeb93fb0d"
        }
        self.__data = []

        # JSON 파일 경로
        json_file_path = 'table.json'
        self.create_table_from_json(json_file_path)
        # print(self.__data)

    def get_data(self):
        return self.__data
    
    def save_table_to_json(self, filename):
        """
        주어진 테이블 데이터를 JSON 파일로 저장하는 함수

        :param filename: 저장할 JSON 파일명 (문자열)
        """

        n = filename
        # JSON 파일 경로 설정
        path = n + '.json'
        # path = 'home/static/home/json/' + n + '.json'
        # json_file_path = os.path.join(settings.BASE_DIR, 'home/static/home/json/'+ n +'.json')

        try:
            # JSON 데이터로 변환
            table_json = []
            for character in self.__data:
                # 전투력이 None이거나 값이 없는 경우 최소한 10으로 저장
                combat_power = character[2] if len(character) > 2 else 10
                # 각 캐릭터 정보를 딕셔너리 형태로 변환
                character_data = {
                    "캐릭터 이름": character[0],
                    "ocid": character[1],
                    "전투력": combat_power
                }
                table_json.append(character_data)

            # JSON 파일로 저장
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(table_json, f, ensure_ascii=False, indent=4)

            print(f"{path} 파일로 저장되었습니다.")

        except Exception as e:
            print("오류 발생:", e)


    def create_table_from_json(self, filename):
        """
        JSON 파일을 읽어서 테이블을 생성하는 함수

        :param json_file: JSON 파일 경로
        :return: 생성된 테이블 (리스트)
        """

        path = filename
        # JSON 파일 경로 설정
        # path = n + '.json'
        # path = 'home/static/home/json/' + n + '.json'
        # json_file_path = os.path.join(settings.BASE_DIR, 'home/static/home/json/'+ n +'.json')

        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.__data.clear()  # 기존 데이터를 지우고 새로 로드
                for entry in data:
                    character_name = entry.get('캐릭터 이름', '')
                    ocid = entry.get('ocid', '')
                    combat_power = entry.get('전투력', 0)
                    self.__data.append([character_name, ocid, combat_power])

            print(f"{path} 파일에서 데이터를 불러왔습니다.")
        
        except Exception as e:
            print("오류 발생:", e)

    def print_table(self):
        """
        테이블을 출력하는 함수
        """
        for character in self.__data:
            print(character)


class JsonDataHandler:
    @staticmethod
    def load_data(name):
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
        for entry in data:
            character_name = entry.get('캐릭터 이름', 'N/A')
            combat_power = entry.get('전투력', 0)
            table_data.append({'character_name': character_name, '전투력': combat_power})

        return table_data

    @staticmethod
    def save_data(data, name):
        n = name
        # JSON 파일 경로 설정
        path = n + '.json'
        # path = 'home/static/home/json/' + n + '.json'
        # json_file_path = os.path.join(settings.BASE_DIR, 'home/static/home/json/'+ n +'.json')

        # JSON 파일 쓰기
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

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
