# TkPDF

## Description

TkPDF Utility is a simple graphical application built with Tkinter that allows you to:
- Convert images to PDF files
- Merge multiple PDF files into a single document

## Prerequisites

- Python 3.x
- The following libraries:
  - Tkinter
  - Pillow (PIL)
  - PyPDF2

## Installation

1. Clone the repository or download the project files.
2. Install the necessary dependencies using pip:

```sh
pip install tkinter pillow pypdf2
```

## Usage

To run the application, launch the main script `main.py`:

```sh
python main.py
```

### Features

#### Convert an Image to PDF

1. Click the "Convert img to PDF" button.
2. Select the image to convert in the file selection dialog.
3. Choose the location and name for the output PDF file.

#### Merge PDF Files

1. Click the "Merge PDF" button.
2. Select the PDF files to merge in the file selection dialog.
3. Choose the location and name for the merged output PDF file.

## Tests

Unit tests for this project are located in the `tests` directory. To run the tests, use the following command:

```sh
python -m unittest discover -s tests
```

## Project Structure

```
tkpdf/
├── main.py
└── tests/
    └── test_pdf_utility.py
```

### main.py

Contains the main application with PDF conversion and merging functionalities.

### tests/test_pdf_utility.py

Contains unit tests for the PDF conversion and merging functions.

## Contributions

Contributions are welcome! Please submit a pull request or open an issue to discuss major changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

