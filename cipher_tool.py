def shift_char(ch, key):
    if ch.isupper():
        base = 65
    elif ch.islower():
        base = 97
    else:
        return ch

    return chr((ord(ch) - base + key) % 26 + base)


def encrypt(text, key):
    return ''.join(shift_char(c, key) for c in text)


def decrypt(text, key):
    return ''.join(shift_char(c, -key) for c in text)


def get_key():
    while True:
        raw = input("Pick your shift key (1-25): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= 25:
            return int(raw)
        print("that's not a valid key, try again")


def main():
    print("=== DecodeLabs Cipher Tool ===")
    msg = input("Enter the text you want to protect: ")
    key = get_key()

    enc = encrypt(msg, key)
    dec = decrypt(enc, key)

    print("\nOriginal :", msg)
    print("Encrypted:", enc)
    print("Decrypted:", dec)

    if dec == msg:
        print("\nround trip check passed, data integrity confirmed")
    else:
        print("\nsomething broke, decrypted text doesn't match original")


if __name__ == "__main__":
    main()
