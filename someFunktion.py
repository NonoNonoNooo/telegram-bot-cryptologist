def caesar_cipher(text, shift):
    """
    This function implements the Caesar cipher for English text with the given shift.
    """
    cipher_text = ""
    for char in text:
        if char.isalpha():
            # Get the character's position in the alphabet
            if char.islower():
                num = ord(char) - ord('a')
                # Apply the shift to the character's position
                num = (num + shift) % 26
                # Convert the new character's position back to a letter
                cipher_text += chr(num + ord('a'))
            else:
                num = ord(char) - ord('A')
                # Apply the shift to the character's position
                num = (num + shift) % 26
                # Convert the new character's position back to a letter
                cipher_text += chr(num + ord('A'))
        else:
            # Leave non-alphabetic characters unchanged
            cipher_text += char
    return cipher_text


def caesar_decipher(cipher_text, shift):
    """
    The function provides decryption of Caesar cipher_text in Russian with shift shift.
    """
    plain_text = caesar_cipher(cipher_text, -shift)
    return plain_text


dict_atbash_code = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                    'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                    'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                    'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                    'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B',
                    'Z': 'A', 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w',
                    'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r',
                    'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm',
                    'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h',
                    't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
                    'y': 'b', 'z': 'a', '0': '0', '1': '1', '2': '2',
                    '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
                    '8': '8', '9': '9', '!': '!', '"': '"', '#': '#',
                    '$': '$', '%': '%', '&': '&', "'": "'", '(': '(',
                    ')': ')', '*': '*', '+': '+', ',': ',', '-': '-',
                    '.': '.', '/': '/', ':': ':', ';': ';', '<': '<',
                    '=': '=', '>': '>', '?': '?', '@': '@', '[': '[',
                    '\\': '\\', ']': ']', '^': '^', '_': '_', '`': '`',
                    '{': '{', '|': '|', '}': '}', '~': '~', ' ': ' ', '\t': '\t'}
def atbash_cipher(text):
    global dict_atbash_code
    result = ''
    for i in text:
        result += dict_atbash_code[i]
    return result



dict_atbash_decode = {'Z': 'A', 'Y': 'B', 'X': 'C', 'W': 'D', 'V': 'E',
                     'U': 'F', 'T': 'G', 'S': 'H', 'R': 'I', 'Q': 'J',
                     'P': 'K', 'O': 'L', 'N': 'M', 'M': 'N', 'L': 'O',
                     'K': 'P', 'J': 'Q', 'I': 'R', 'H': 'S', 'G': 'T',
                     'F': 'U', 'E': 'V', 'D': 'W', 'C': 'X', 'B': 'Y',
                     'A': 'Z', 'z': 'a', 'y': 'b', 'x': 'c', 'w': 'd',
                     'v': 'e', 'u': 'f', 't': 'g', 's': 'h', 'r': 'i',
                     'q': 'j', 'p': 'k', 'o': 'l', 'n': 'm', 'm': 'n',
                     'l': 'o', 'k': 'p', 'j': 'q', 'i': 'r', 'h': 's',
                     'g': 't', 'f': 'u', 'e': 'v', 'd': 'w', 'c': 'x',
                     'b': 'y', 'a': 'z', '0': '0', '1': '1', '2': '2',
                     '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
                     '8': '8', '9': '9', '!': '!', '"': '"', '#': '#',
                     '$': '$', '%': '%', '&': '&', "'": "'", '(': '(',
                     ')': ')', '*': '*', '+': '+', ',': ',', '-': '-',
                     '.': '.', '/': '/', ':': ':', ';': ';', '<': '<',
                     '=': '=', '>': '>', '?': '?', '@': '@', '[': '[',
                     '\\': '\\', ']': ']', '^': '^', '_': '_', '`': '`',
                     '{': '{', '|': '|', '}': '}', '~': '~', ' ': ' ', '\t': '\t'}

def atbash_decipher(text):
    global dict_atbash_decode
    result = ''
    for i in text:
        result += dict_atbash_decode[i]
    return result




