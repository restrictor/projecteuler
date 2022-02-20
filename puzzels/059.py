""" XOR decryption

Problem 59
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard
Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given
value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on
the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of
random bytes. The user would keep the encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout
the message. The balance for this method is using a sufficiently long password key for security, but short
enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using
p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words, decrypt the message and find the
sum of the ASCII values in the original text.
"""

from time import perf_counter
start = perf_counter()

# space is most common in english text and a lowercase character xor with his uppercase results in a space!
from collections import Counter
from spellchecker import SpellChecker
from textwrap import fill


def decrypt_ciphertext() -> None:
    cipher = [int(x) for x in open('../data/059.txt').read().strip().split(',')]
    top_ten_occurrence_numbers = sorted(Counter(cipher), key=Counter(cipher).get, reverse=True)[:10]
    print(f"top ten occurrences: {top_ten_occurrence_numbers}")

    filtered_letters = [x for x in top_ten_occurrence_numbers if 91 > x > 64 or 123 > x > 96]
    small_letter = [x ^ ord(" ") for x in filtered_letters]
    print(f"letters: {[chr(x) for x in filtered_letters]} and xor with space {[chr(x) for x in small_letter]} \n")

    words, best_key, known = 0, "", SpellChecker().known
    for key in [[a,  b, c] for a in small_letter for b in small_letter for c in small_letter]:
        if len(known("".join([chr(cipher[i] ^ key[i % len(key)]) for i in range(0, len(cipher))]).split(" "))) > words:
            words = len(known("".join([chr(cipher[i] ^ key[i % len(key)]) for i in range(0, len(cipher))]).split(" ")))
            best_key = key
    print(fill("".join([chr(cipher[i] ^ best_key[i % len(best_key)]) for i in range(0, len(cipher))]), 100), "\n")

    print(sum(ord(x) for x in [chr(cipher[i] ^ best_key[i % len(best_key)]) for i in range(0, len(cipher))]))


decrypt_ciphertext()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# top ten occurrences: [80, 69, 88, 0, 17, 29, 21, 12, 4, 22]
# letters: ['P', 'E', 'X'] and xor with space ['p', 'e', 'x']
#
# An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum
# reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an
# elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on
# the quadrature of the circle, so that if the true sum of this series is obtained, from it at once
# the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth
# part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this
# series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I
# will soon show that the sum of this series to be approximately 1.644934066842264364; and from
# multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is
# indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the
# same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16
# + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this
# multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a
# circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums
# of the subsequent series in which the exponents are even numbers.
#
# 129448
# Runtime of the program is 0.1514471000
