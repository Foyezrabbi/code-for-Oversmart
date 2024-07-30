import base64

# Your code to encode
your_code = """
def hello_world():
    print("Hello, World!")

hello_world()
"""

# Encoding the code in Base64
encoded_code = base64.b64encode(your_code.encode()).decode()

# Decoding the code back from Base64
decoded_code = base64.b64decode(encoded_code).decode()

# Executing the decoded code
exec(decoded_code)
