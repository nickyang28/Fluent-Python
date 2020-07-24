def test(name, *args, cls=None, **kwargs):
    print(name)
    print(args)
    print(cls)
    print(kwargs)


test("Bob", 14, 155, age=14, height=166, cls="Student")
