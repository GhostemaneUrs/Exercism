def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob_pregunta(hey_bob):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob_pregunta(hey_bob):
        return "Sure."
    return "Whatever."


def hey_bob_pregunta(hey_bob):
    return hey_bob.endswith("?")
