import base64


def encode_with_salt(payload: str, salt_key: str, salt_index: int) -> str:

    salted_payload = payload[:salt_index] + salt_key + payload[salt_index:]

    payload_bytes = salted_payload.encode('utf-8')

    base64_bytes = base64.b64encode(payload_bytes)

    return base64_bytes.decode('utf-8')


def decode_with_salt(encoded_payload: str, salt_key: str, salt_index: int) -> str:

    try:
        decoded_bytes = base64.b64decode(encoded_payload)
        decoded_str = decoded_bytes.decode('utf-8')

        if decoded_str[salt_index:salt_index + len(salt_key)] == salt_key:
            original_payload = decoded_str[:salt_index] + decoded_str[salt_index + len(salt_key):]
            return original_payload
        else:
            return "Error: Incorrect salt key or salt index."

    except Exception as e:
        return f"Error during decoding: {e}"


if __name__ == "__main__":
    payload = "Hello, World!"
    salt_key = "secretkey"
    salt_index = 5

    encoded = encode_with_salt(payload, salt_key, salt_index)
    print(f"Encoded Payload: {encoded}")

    decoded = decode_with_salt(encoded, salt_key, salt_index)
    print(f"Decoded Payload: {decoded}")

    decoded_incorrect = decode_with_salt(encoded, "wrongkey", salt_index)
    print(f"Decoded with incorrect salt key: {decoded_incorrect}")

    decoded_incorrect_index = decode_with_salt(encoded, salt_key, salt_index + 1)
    print(f"Decoded with incorrect salt index: {decoded_incorrect_index}")
