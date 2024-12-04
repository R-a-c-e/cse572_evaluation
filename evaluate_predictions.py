from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import re

def evaluate_classification_metrics(data, true_label_col='input_labels', predicted_label_col='output_labels'):
        true_labels = data[true_label_col]
        predicted_labels = data[predicted_label_col]

        # Calculate metrics
        accuracy = accuracy_score(true_labels, predicted_labels)
        precision = precision_score(true_labels, predicted_labels, average='binary')
        recall = recall_score(true_labels, predicted_labels, average='binary')
        f1 = f1_score(true_labels, predicted_labels, average='binary')

        # Store metrics in a dictionary
        metrics = {
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1 Score': f1
        }

        # Print metrics
        print("Evaluation Metrics:")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.2f}")

        return metrics

def clean_output(text):
    text = re.sub(r'\t+', ' ', text)  # Remove tab characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text

def check_data(data_frame, column_name):
    for index, row in data_frame.iterrows():
        if row[column_name] not in (1, 0):
            print(f"Found target value at index {index}: {row[column_name]}")

def main():
    # Set paths
    original_data_path = 'data/HateSpeechTestData_top4000.csv'
    predicted_data_path = 'predictions/openAI_HS_predictions_corrected.csv'
    
    # Get data in
    input = pd.read_csv(original_data_path)
    input = input[['text', 'labels']]
    output = pd.read_csv(predicted_data_path)

    # rename columns accordingly
    input=input.rename(columns={'labels':'input_labels'})
    output=output.rename(columns={'analysis':'output_labels'})

    #rint(input.head())
    #print(output.head())

    # merge in prep for eval
    evaluation_table = pd.merge(input, output, on='text')

    # evaluate
    eval_metrics = evaluate_classification_metrics(evaluation_table)
    # check_data(output, 'output_labels')




if __name__ == "__main__":
    main()