# Default value for parameter/argument
def wish(name='Guest', message='Hello'):
    print(message, name)


wish("Don", "Greetings")  # Passing by position
wish(message="Good Morning", name="Scott")  # Passing by name (keyword)
wish("Tom")
wish()
wish(message="Hi")
