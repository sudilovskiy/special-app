name = input("Имя: ")
duty = int(input("Долг: "))

msg = "{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей. {0}!".format(
    name,
    duty
)

print(msg)
