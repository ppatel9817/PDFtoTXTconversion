#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pdfplumber
import os
from tqdm import tqdm
import spacy


'''
The code is a Python script designed to extract text from PDF files and save the extracted text as `.txt` files. Here's a breakdown of what each part of the script does:

1. **Define Directories**:
   - `pdf_root_directory`: Specifies the root directory where the PDF files are stored.
   - `text_root_directory`: Specifies the directory where the text files should be saved after extraction.

2. **Create the Text Output Directory**:
   - The `os.makedirs` function is used to create the directory specified by `text_root_directory`, if it does not already exist. This ensures there's a place to save the extracted text files.

3. **Function to Extract Text from PDF** (`extract_text_from_pdf`):
   - This function takes a path to a PDF file and an output path for the text file as input.
   - It uses the `pdfplumber` library to open and read each page of the PDF.
   - It extracts text from each page, concatenating it into a single string.
   - The extracted text is then written to a file at the specified output path.

4. **Collect All PDF Paths**:
   - The script uses `os.walk` to traverse through the `pdf_root_directory` and collect paths to all PDF files.
   - It calculates the relative path for each PDF file's directory to maintain a similar directory structure in the `text_root_directory`.
   - It prepares a list (`pdf_files`) of tuples, each containing the path to a PDF file and the corresponding output path for the text file.

5. **Extract Text from Each PDF**:
   - It loops over each tuple in the `pdf_files` list.
   - For each tuple, it calls `extract_text_from_pdf` with the PDF path and output file path.
   - It uses `tqdm` to show a progress bar in the console, providing visual feedback on the progress of text extraction.

6. **Completion Message**:
   - After all files have been processed, it prints a message indicating that the extraction and saving are complete.

**Note**:
- The script includes error handling within the `extract_text_from_pdf` function to manage and report any issues that occur during the processing of a PDF file.

This script is useful for batch processing of PDFs to extract and save their text content, maintaining the directory structure between the source PDF files and the output text files.

'''

# Path to the root directory containing the PDF files
pdf_root_directory = '/Users/poojanpatel/Desktop/Final_attempt/pdfs/Testing'

# Path to the directory where the text files will be saved
text_root_directory = '/Users/poojanpatel/Desktop/Final_attempt/txt'
os.makedirs(text_directory, exist_ok=True)  # Creates the directory if it does not exist



# Function to extract and save text from PDF
def extract_text_from_pdf(pdf_path, output_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
            
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

        
        
# Collect all PDF paths and map them to their new text file paths
pdf_files = []
for dirpath, dirnames, filenames in os.walk(pdf_root_directory):
    for filename in [f for f in filenames if f.endswith('.pdf')]:
        pdf_path = os.path.join(dirpath, filename)
        relative_path = os.path.relpath(dirpath, pdf_root_directory)  # Get the relative directory path
        output_dir = os.path.join(text_root_directory, relative_path)  # Create a parallel structure in the target
        output_file_path = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}.txt')
        pdf_files.append((pdf_path, output_file_path))

# Extract text from each PDF with a progress bar
for pdf_path, output_file_path in tqdm(pdf_files, desc="Extracting PDFs"):
    extract_text_from_pdf(pdf_path, output_file_path)

print("Extraction and saving complete.")



'''
The code provided describes a Python script designed to preprocess text files extracted from PDFs, specifically aiming to lemmatize the text, remove stopwords, and discard punctuation. This script is typically used to clean and normalize text data, making it more suitable for further natural language processing (NLP) tasks. Here’s how the script is structured and what each part does:

1. **Load NLP Model**:
   - `nlp = spacy.load("en_core_web_sm")` loads a small English language model from SpaCy, which includes components for tokenization, part-of-speech tagging, parsing, named entity recognition (NER), and word vectors.

2. **Define Processed Text Directory**:
   - `processed_text_directory` specifies where the processed text files will be saved.
   - `os.makedirs(processed_text_directory, exist_ok=True)` creates this directory if it doesn't exist.

3. **Function for Text Preprocessing** (`preprocess_text`):
   - This function takes raw text as input, processes it using the SpaCy pipeline (`nlp`), and then applies filtering:
     - Lemmatization converts words to their base form (lemma).
     - Stopwords (commonly used words that may have little value in analysis like "and", "the", etc.) and punctuation are removed.
   - The resulting tokens are joined into a single string of cleaned text.

4. **Iterate Over Text Files for Processing**:
   - `os.walk(text_root_directory)` is used to traverse the directory containing the text files extracted from PDFs.
   - For each text file ending with ".txt", the script reads the content, processes it using the `preprocess_text` function, and saves the processed text:
     - The relative path of each file within the `text_root_directory` is maintained in the `processed_text_directory` to preserve the original directory structure.
     - Each processed text file is saved with the same filename in the corresponding directory under `processed_text_directory`.

5. **Progress and Completion**:
   - `tqdm` is used to display a progress bar in the console while processing the files, giving feedback on the progress.
   - After processing all files, a completion message ("Text preprocessing complete.") is printed to indicate that the script has finished running.

**Use Case**:
This script is useful for preparing textual data for machine learning or other types of textual analysis by reducing noise and standardizing the text format. Such preprocessing steps are crucial for improving the performance of NLP models and analyses.'''

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")


processed_text_directory = '/Users/poojanpatel/Desktop/Final_attempt/processed_text'
os.makedirs(processed_text_directory, exist_ok=True)

def preprocess_text(text):
    doc = nlp(text)
    # Lemmatize and remove stopwords and punctuation
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

for root, dirs, files in os.walk(text_root_directory):
    for filename in tqdm(files, desc="Processing Texts"):
        if filename.endswith(".txt"):
            text_path = os.path.join(root, filename)
            with open(text_path, 'r', encoding='utf-8') as file:
                text = file.read()
                processed_text = preprocess_text(text)
            
            # Create the same subdirectory structure in the processed directory
            relative_path = os.path.relpath(root, text_root_directory)
            processed_dir = os.path.join(processed_text_directory, relative_path)
            os.makedirs(processed_dir, exist_ok=True)

            processed_file_path = os.path.join(processed_dir, filename)
            with open(processed_file_path, 'w', encoding='utf-8') as p_file:
                p_file.write(processed_text)

print("Text preprocessing complete.")

