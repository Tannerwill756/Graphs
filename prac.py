idk = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}

total = 0

for x in idk:
    if type(idk[x]) is int:
        total += idk[x]

print(total)
