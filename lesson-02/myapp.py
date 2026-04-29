import random
import string
import time

def generate_password():
    length = random.randint(8, 16)

    digit = random.choice(string.digits)
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    special = random.choice('#.,!@&^%*')

    all_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase + '#.,!@&^%*'
    remaining = [random.choice(all_chars) for _ in range(length - 4)]

    password_list = [digit, lower, upper, special] + remaining
    random.shuffle(password_list)

    password = ''.join(password_list)

    time.sleep(0.05)

    return password


def app(environ, start_response):
    password = generate_password()

    response_body = f"Password: {password}\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Content-Length", str(len(response_body))),
    ])

    return [response_body.encode('utf-8')]