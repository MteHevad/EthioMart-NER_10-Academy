def label_data(input_file, output_file):
    # Code to manually label data in CoNLL format
    with open(input_file, 'r') as f:
        data = f.readlines()

    with open(output_file, 'w') as f:
        for line in data:
            tokens = line.strip().split()
            for token in tokens:
                f.write(f"{token} O\n")  # Default label O, replace with B/I-Product, B/I-Price, etc.
            f.write("\n")

if __name__ == "__main__":
    label_data('data/processed/telegram_preprocessed.csv', 'data/processed/amharic_ner_conll.txt')
