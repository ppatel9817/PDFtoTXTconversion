# PDF Text Extraction and Preprocessing Tools

Description
This repository contains Python scripts designed to automate the extraction of text from PDF files and subsequent preprocessing for natural language processing (NLP) tasks. The scripts facilitate the batch processing of PDFs to extract text, normalize, and clean it by removing stopwords and punctuation and performing lemmatization.

Components
PDF Text Extractor: This script extracts text from each PDF file found in a specified directory and saves it as a text file, preserving the directory structure between the source PDFs and the output text files.

Text Preprocessor: After text extraction, this script preprocesses the text by lemmatizing it, removing stopwords and punctuation, and saving the cleaned text back into a structured directory format. This makes the text ready for further NLP tasks.

Structure of the Scripts PDF Text Extractor (pdf_text_extractor.py):
Traverses the specified root directory to find PDF files.
Extracts text from each PDF using pdfplumber.
Saves the extracted text in a new text file, mirroring the PDF's directory structure.


Text Preprocessor (text_preprocessor.py):
Reads text files from the extraction output directory.
Processes each file using SpaCy to lemmatize the text and remove stopwords and punctuation.
Saves the processed text in a structured format that mirrors the input text files' directory structure.

Notes
The scripts include error handling to manage issues that may arise during the processing of PDF files, such as corrupted files or unreadable content.
Progress bars are displayed in the console during the processing of files to provide feedback on the progress.
