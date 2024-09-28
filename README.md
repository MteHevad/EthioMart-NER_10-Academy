# EthioMart Named Entity Recognition (NER) Project

This repository contains code for the EthioMart project to extract entities such as product names, prices, and locations from Amharic Telegram e-commerce channels using a fine-tuned NER model.

## Directory Structure
- `data/`: Contains raw and processed data.
- `notebooks/`: Jupyter notebooks for data ingestion, preprocessing, and model fine-tuning.
- `src/`: Python scripts for each task.
- `models/`: Fine-tuned models.
- `utils/`: Helper functions for tasks like scraping, tokenization, and interpretability.
- `reports/`: Contains reports such as interim submission and final project results.

## How to Run the Project
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the notebooks or scripts for ingestion, preprocessing, and fine-tuning.

## Requirements
- Python 3.x
- Hugging Face Transformers
- Pandas
- SHAP
- LIME
- Telethon (for Telegram API access)

## License
This project is licensed under the MIT License.
