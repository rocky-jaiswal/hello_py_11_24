from hello_py.greeting import Greeting


def test_greeting():
    greeting = Greeting()
    assert greeting.get_greeting() == "Hello Python!"
