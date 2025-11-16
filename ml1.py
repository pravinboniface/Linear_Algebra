import pandas as pd;

def main():
    melbourne_file_path = r'C:\Users\Anitha\Downloads\melb_data.csv\melb_data.csv'
    # read the data and store data in DataFrame titled melbourne_data
    melbourne_data = pd.read_csv(melbourne_file_path) 
    # print a summary of the data in Melbourne data
    print(melbourne_data.describe())
    print(melbourne_data.columns)
    
    return

if __name__ == "__main__":
    main()