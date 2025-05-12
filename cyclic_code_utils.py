import numpy as np

def text_to_binary(text):
    """Convert text to binary ASCII code"""
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def segment_message(binary_message, block_size):
    """Segment binary message into blocks of specified size"""
    segments = [binary_message[i:i + block_size] for i in range(0, len(binary_message), block_size)]
    # Pad the last segment if necessary
    if len(segments[-1]) < block_size:
        segments[-1] = segments[-1].ljust(block_size, '0')
    return segments

def binary_to_text(binary):
    """Convert binary back to text"""
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))