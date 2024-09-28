from transformers import AutoModelForTokenClassification, AutoTokenizer

def evaluate_model(model_name, test_data):
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # Add evaluation logic (precision, recall, F1-score)
    pass
