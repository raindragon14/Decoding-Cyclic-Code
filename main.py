from cyclic_code_utils import text_to_binary, segment_message, binary_to_text
from cyclic_code import CyclicCode

def print_encoding_info(block_num: int, info: dict):
    print(f"\nBlock {block_num} Encoding Process:")
    print(f"Message polynomial m(x) = {info['message_poly']}")
    print(f"Shifted polynomial x^n·m(x) = {info['shifted_poly']}")
    print(f"Generator polynomial g(x) = {info['generator_poly']}")
    print(f"Remainder r(x) = {info['remainder_poly']}")
    print(f"Codeword c(x) = {info['codeword_poly']}")

def print_transmission_info(block_num: int, info: dict):
    print(f"\nBlock {block_num} Transmission:")
    print(f"Original codeword c(x) = {info['original_poly']}")
    if info['error_positions']:
        print(f"Error pattern e(x) = {info['error_pattern_poly']}")
        print(f"Received polynomial r(x) = c(x) + e(x) = {info['received_poly']}")
    else:
        print("No errors introduced during transmission")

def print_decoding_info(block_num: int, info: dict):
    print(f"\nBlock {block_num} Decoding Process:")
    print(f"Received polynomial r(x) = {info['received_poly']}")
    print("\nSyndrome Calculation:")
    print(f"r(x) = {info['syndrome_calculation']['dividend']}")
    print(f"g(x) = {info['syndrome_calculation']['divisor']}")
    print(f"Syndrome s(x) = {info['syndrome_poly']}")
    
    if info['error_detected']:
        print("\nError Analysis:")
        if info['corrected']:
            print(f"Error detected at position {info['error_position']}")
            print(f"Error pattern e(x) = {info['error_pattern_poly']}")
            print(f"Corrected codeword c(x) = {info['corrected_poly']}")
        else:
            print("Error detected but could not be corrected")
    else:
        print("\nNo errors detected")

def main():
    # Initialize with generator polynomial g(x) = 1 + x + x^3
    generator_polynomial = [1, 1, 0, 1]
    cyclic_code = CyclicCode(generator_polynomial)
    
    # Get input message
    message = input("Enter message to encode: ")
    binary_message = text_to_binary(message)
    print(f"\nBinary message: {binary_message}")
    
    # Segment message
    block_size = 4  # (7,4) cyclic code
    message_blocks = segment_message(binary_message, block_size)
    print(f"\nMessage blocks: {message_blocks}")
    
    # Encode blocks
    print("\n=== ENCODING PROCESS ===")
    encoded_blocks = []
    encoding_infos = []
    for i, block in enumerate(message_blocks):
        encoded_block, encoding_info = cyclic_code.encode_block(block)
        encoded_blocks.append(encoded_block)
        encoding_infos.append(encoding_info)
        print_encoding_info(i, encoding_info)
    
    # Simulate transmission with errors
    print("\n=== TRANSMISSION WITH ERRORS ===")
    received_blocks = []
    transmission_infos = []
    for i, block in enumerate(encoded_blocks):
        error_positions = [i % 3] if i % 2 == 0 else None
        received_block, transmission_info = cyclic_code.simulate_transmission(block, error_positions)
        received_blocks.append(received_block)
        transmission_infos.append(transmission_info)
        print_transmission_info(i, transmission_info)
    
    # Decode blocks
    print("\n=== DECODING AND ERROR CORRECTION ===")
    decoded_blocks = []
    for i, block in enumerate(received_blocks):
        decoded_block, decoding_info = cyclic_code.decode_block(block)
        decoded_blocks.append(decoded_block)
        print_decoding_info(i, decoding_info)
    
    # Reassemble and convert to text
    decoded_binary = ''.join(decoded_blocks)
    decoded_text = binary_to_text(decoded_binary)
    print(f"\nFinal decoded message: {decoded_text}")

if __name__ == "__main__":
    main()