from pandas import DataFrame
from ebest import ResponseValue

def print_table(data):
    if data is None:
        print("[!] 데이터가 없습니다.")
        return

    if isinstance(data, dict):
        print(f"Field Count = {len(data)}")
        for k, v in data.items():
            print(f"{k:<20} : {v}")
        print()

    elif isinstance(data, list):
        if len(data) == 0:
            print("[] (빈 리스트)")
            return

        if isinstance(data[0], dict):
            keys = list(data[0].keys())
            print(f"Row Count = {len(data)}")

            # 헤더 출력
            print(" | ".join(f"{k:<12}" for k in keys))
            print("-" * (15 * len(keys)))

            # 행 출력
            for row in data:
                print(" | ".join(f"{str(row[k]):<12}" for k in keys))
        else:
            print(f"Row Count = {len(data)}")
            for item in data:
                print(f"- {item}")

    elif isinstance(data, DataFrame):
        print(f"Row Count = {len(data)}")
        print(data.to_string(index=False))

    elif isinstance(data, ResponseValue):
        print(f"tr_cont = '{data.tr_cont}', tr_cont_key = '{data.tr_cont_key}'")
        for key in data.body:
            print(f"\n[{key}]")
            print_table(data.body[key])

    else:
        print(str(data))
