# utils/tokenizer_utils.py

def tokenize_text(text):
    """Tokenize the input text."""
    return text.split()  # Simple tokenization by whitespace

def align_with_conll_format(tokens, labels):
    """Align tokenized input with CoNLL format."""
    conll_format = []
    for token, label in zip(tokens, labels):
        conll_format.append(f"{token}\t{label}")
    return conll_format

# Example function to save CoNLL format data to a file
def save_to_conll_file(conll_data, file_path):
    """Save the aligned data in CoNLL format to a file."""
    with open(file_path, 'w') as f:
        for line in conll_data:
            f.write(line + '\n')
