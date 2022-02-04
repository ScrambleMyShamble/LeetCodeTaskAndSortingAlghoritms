def is_palindrome(s: str) -> bool:
    ttl = ''.join(i for i in s if i.isalpha() or i.isdigit())
    return ttl[::].lower() == ttl[::-1].lower()


frase = "A man, a plan, a canal: Panama"

print(is_palindrome(frase))
