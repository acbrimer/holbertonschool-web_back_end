#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth

    ba = BasicAuth()
    res = ba.decode_base64_authorization_header("SEJUTg==")
    if res is None:
        print("decode_base64_authorization_header must return the decoded version of 'base64_authorization_header'")
        exit(1)

    if res != "HBTN":
        print("Wrong Base64 decode: {}".format(res))
        exit(1)

    print("OK", end="")
