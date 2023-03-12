def say_hello(name):
    print('Hello, ', name, '!', sep='')

def insert_separator(s="=", repeat=30):
    print(s * repeat)

def recite_poem():
    print("How about a Monty Python poem?")
    insert_separator("-", 20)
    print("Much to his Mum and Dad’s dismay")
    print("Horace ate himself one day.")
    print("He didn’t stop to say his grace,")
    print("He just sat down and ate his face.")

def say_goodbye(name):
    print('Goodbye, ', name, '!', sep='')

def main():
    your_name = input('What is your name? ')
    insert_separator("-", 20)
    say_hello(your_name)
    insert_separator()
    recite_poem()
    insert_separator()
    say_goodbye(your_name)

main()