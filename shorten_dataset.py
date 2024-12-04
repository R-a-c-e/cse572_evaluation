import pandas as pd

def extract_top_4000_rows(input_file, output_file, num_rows):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Extract the top 4000 rows
    df_top_4000 = df.head(num_rows)
    
    # Write these rows to a new CSV file
    df_top_4000.to_csv(output_file, index=False)

def main():
    
    input_file = 'data/HateSpeechTestData.csv'
    output_file = 'data/HateSpeechTestData_top4000.csv'  
    num_rows = 4000

    extract_top_4000_rows(input_file, output_file, num_rows)

if __name__ == "__main__":
    main()