# Decoding Cyclic Code

This project implements a Cyclic Code encoder and decoder for error detection and correction in digital communication systems. It specifically implements a (7,4) cyclic code, which can encode 4-bit messages into 7-bit codewords and correct single-bit errors.

## Features

- Polynomial-based encoding and decoding
- Error detection and correction for single-bit errors
- Syndrome calculation and error pattern matching
- Transmission simulation with customizable error positions
- Detailed information about the encoding/decoding process

## Requirements

To run this project, you need Python 3.x and the following packages:
- numpy

You can install the required packages using:
```bash
pip install -r requirements.txt
```

## Usage

The main components of the system are:
1. `CyclicCode` class for encoding and decoding
2. Utility functions in `cyclic_code_utils.py`
3. Example usage in `main.py`

To run the example:
```bash
python main.py
```

## Project Structure

- `cyclic_code.py` - Main implementation of the CyclicCode class
- `cyclic_code_utils.py` - Utility functions
- `main.py` - Example usage and demonstrations
- `requirements.txt` - Project dependencies

## GitHub Repository

Find the latest code at: https://github.com/raindragon14/Decoding-Cyclic-Code