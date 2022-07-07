with open('python.txt', 'w') as f:
    f.write(''' Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.''')
t_words = []
with open('python.txt', 'r') as f:
    for i in f.read().split(' '):
        if 't' in i:
            t_words.append(i)
        if 'T' in i:
            t_words.append(i)
print(t_words)

