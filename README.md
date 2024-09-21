# Unique Integer Sorter

This Python script reads a file containing integers, extracts the unique integers, sorts them in ascending order, and saves the results to a designated output directory.

## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
  
## Project Overview

The **Unique Integer Sorter** processes text files with integers (positive or negative) and:
1. Identifies all unique integers in the file.
2. Sorts them in ascending order.
3. Saves the sorted integers to a results file in the `sample_results` directory.

## Directory Structure

The project expects two directories:
- `sample_inputs/`: Contains the input files with integers.
- `sample_results/`: The directory where sorted results will be saved.

Example structure:
```
project_directory/
│
├── sample_inputs/
│   └── small_sample_input_04.txt
├── sample_results/
│   └── small_sample_input_04_results.txt
└── UniqueInt.py
```

## Features

- Reads input files from the `sample_inputs` directory.
- Extracts unique integers from the file.
- Sorts the integers in ascending order.
- Saves the results in the `sample_results` directory.

## Requirements

- Python 3.x
- Works on both Linux and Windows environments.
  
## Usage

1. **Prepare your input file**: Place your file containing integers in the `sample_inputs` directory. Make sure the integers are in plain text format, one or more per line.

2. **Run the script**:
   ```
   python3 UniqueInt.py
   ```

3. **Input the filename**: You will be prompted to enter the filename (with extension) of the input file stored in the `sample_inputs` directory.

4. **Check the output**: The sorted unique integers will be saved in a new file inside the `sample_results` directory. The result file will be named as `<input_filename>_results.txt`.

### Example Command:
```
Please enter the filename (with extension): small_sample_input_04.txt
```

The sorted results will be saved in:
```
sample_results/small_sample_input_04_results.txt
```

## Example

### Input (small_sample_input_04.txt):
```
3 7 -1 8 0 2 3 8
-5 10 -3 2 -3 7
5 3 2
```

### Output (small_sample_input_04_results.txt):
```
-5
-3
-1
0
2
3
5
7
8
10
```
