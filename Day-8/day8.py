# Caesar Cipher
def caesar_cipher(text: str, shift: int, mode: str = 'encode') -> str:
    """
    Encrypts or decrypts text using the Caesar cipher method.
    """
    result = []
    
    # Reverse shift for decryption
    if mode.lower() == 'decode':
        shift = -shift

    # Normalize shift to stay within the 26-letter alphabet range
    shift = shift % 26

    for char in text:
        if char.isalpha():
            # Determine starting ASCII offset based on casing
            start = ord('A') if char.isupper() else ord('a')
            
            # Apply shift with wrapping via modulo 26
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            result.append(shifted_char)
        else:
            # Leave non-alphabet characters unchanged
            result.append(char)

    return "".join(result)


def main():
    print("=" * 35)
    print("      CAESAR CIPHER PROGRAM      ")
    print("=" * 35)

    while True:
        mode = input("\nDo you want to (E)ncrypt or (D)ecrypt? (Or type 'Q' to quit): ").strip().lower()
        
        if mode in ['q', 'quit']:
            print("Goodbye!")
            break
            
        if mode not in ['e', 'encrypt', 'd', 'decrypt']:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")
            continue

        direction = 'encode' if mode in ['e', 'encrypt'] else 'decode'
        message = input("Enter your message: ")

        while True:
            try:
                shift = int(input("Enter shift value (integer): "))
                break
            except ValueError:
                print("Please enter a valid integer for the shift value.")

        output = caesar_cipher(message, shift, direction)
        print(f"\nResult ({direction.upper()}D): {output}\n")


if __name__ == "__main__":
    main()