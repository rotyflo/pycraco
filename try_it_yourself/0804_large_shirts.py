def make_shirt(size='large', text="I love Python"):
    print(
        "This {} shirt will have '{}' printed on it."
        .format(size, text)
    )

make_shirt()
make_shirt('medium')
make_shirt(text="I love Java :O")