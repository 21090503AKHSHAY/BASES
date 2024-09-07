import base64
import binascii
import pyfiglet
import sys

# Print banner with name
banner = pyfiglet.figlet_format("BASES")
print(banner, "--by Akhshay TP / ByteButcherX\n")

# Helper functions for each encoding type
def decode_base32(encoded_text):
    try:
        return base64.b32decode(encoded_text).decode('utf-8')
    except binascii.Error:
        return None

def decode_base45(encoded_text):
    try:
        import base45  # You might need to install this with 'pip install base45'
        return base45.b45decode(encoded_text).decode('utf-8')
    except:
        return None

def decode_base58(encoded_text):
    try:
        import base58  # You might need to install this with 'pip install base58'
        return base58.b58decode(encoded_text).decode('utf-8')
    except:
        return None

def decode_base62(encoded_text):
    try:
        import base62  # You might need to install this with 'pip install base62'
        return base62.decodebytes(encoded_text).decode('utf-8')
    except:
        return None

def decode_base64(encoded_text):
    try:
        return base64.b64decode(encoded_text).decode('utf-8')
    except binascii.Error:
        return None

# Function to detect and decode automatically
def auto_detect_decode(encoded_text):
    decoders = {
        'Base32': decode_base32,
        'Base45': decode_base45,
        'Base58': decode_base58,
        'Base62': decode_base62,
        'Base64': decode_base64,
    }

    for base, decode_func in decoders.items():
        decoded = decode_func(encoded_text)
        if decoded:
            return f"Decoded using {base}: {decoded}"
    
    return "Unable to detect or decode the encoding."

# Print help message
def print_help():
    help_message = """
ByteButcherX 1.0.0
by Akhshay TP

USAGE:
    python3 main.py [ENCODED_TEXT]

FLAGS:
    -h, --help       Prints help information

EXAMPLES:
    python3 main.py "SGVsbG8gV29ybGQh"

DESCRIPTION:
    This tool detects and decodes base32, base45, base58, base62, and base64-encoded text automatically.
    """
    print(help_message)

# Main function
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print_help()
    else:
        encoded_input = sys.argv[1]
        print(auto_detect_decode(encoded_input))
