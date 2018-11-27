def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print("- " + item)

make_sandwich('lettuce', 'tomato')
make_sandwich('cheese')
make_sandwich('onion', 'pickles', 'turkey')