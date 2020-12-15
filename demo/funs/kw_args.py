def details(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


details(name="Abc", email="abc@gmail.com", age=20)
details(first_name="Abc", last_name="Xyz")
# details(10,20,30) --> Error

