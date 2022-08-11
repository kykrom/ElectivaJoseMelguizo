my_string = "hello, world!"
single_quote_string = "Hello, world!"

#a estas variables se les asigno texto en modo de informacion

string_with_quotes = "Hello, its me"
another_with_quotes = 'He said "You are amazing!" yesterday.'
# que las comillas se leen como texto

escaped_quotes = 'He said "you are amazing!" yesterday.'


multiline = """Hello, world
my name is jose. welcome to my program."""
print(multiline)

#Cuando habro las 3 comillas todo lo que tenga abajo sera formato tipo texto hasta que lo cierre 

name = "jose"
greeting = "hello, " + name

print(greeting)

#Aqui se estahaciendo una concatenacion

age = 34
print("you are " + age)

#Sale error porque 

age = 34
age_as_string = str(34)
print("you are " + age_as_string)

#para solucionar el error del ejercisio pasado se convierte una variable int en una str para poder sumarla