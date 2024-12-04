import pandas as pd

def process_hate_speech(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Map 'analysis' column values to 0 and 1
    df['analysis'] = df['analysis'].apply(lambda x: 0 if 'Not Hate Speech' in x else 1)
    
    # Write the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

def main():
    # Define the input and output file paths
    input_file = 'predictions/openAI_HS_predictions.csv'
    output_file = 'predictions/openAI_HS_predictions_corrected.csv'
    
    # Call the function to process the CSV
    process_hate_speech(input_file, output_file)

if __name__ == "__main__":
    main()