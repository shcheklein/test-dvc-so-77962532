import os
import pandas as pd
import yaml


def main():
    with open("params.yaml") as yaml_file:
        config = yaml.safe_load(yaml_file)

    numbers = []
    squares = []
    for i in range(config['size']):
        numbers.append(i)
        squares.append(i**2)
    df = pd.DataFrame({"number": numbers, "square": squares})
    os.makedirs('artifacts/data_ingestion', exist_ok=True)
    df.to_csv('artifacts/data_ingestion/test_data.csv', index=False)



if __name__ == "__main__":
    main()
