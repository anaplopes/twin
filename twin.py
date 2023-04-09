
def twin(a: str, b: str) -> bool:
    a = a.lower()
    b = b.lower()

    if a == b:
        return True

    if a == b[::-1]:
        return True

    find_first_letter = b.find(a[0])
    if find_first_letter >= 0:
        new_b = b[find_first_letter:len(b) + 1] + b[:find_first_letter]
        if new_b == a:
            return True

    return False


print(twin(a="Hello", b="world"))
print(twin(a="abc", b="cba"))
print(twin(a="Lookout", b="Outlook"))
