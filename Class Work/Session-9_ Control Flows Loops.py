In -


class exercise
    ●    Shubh
    forgot
    to
    complete
    his
    computer
    science
    homework.His
    teacher
    got
    angry and told
    him
    to
    type “I
    will
    complete
    my
    homework” 100
    times as punishment.To
    help
    Shubh
    write
    a
    python
    program
    that
    can
    print
    this
    statement
    100
    times
    using
    loops.

●    Hint: Use
loop
○    1. - Use
for loop
    ○    2. - Use
    while loop
        ➔  # Printing "I will complete my homework" 100 times
    ➔
    ➔    for i in range(100):
        ➔        print("I will complete my homework")
    ●

    ●    A
    computer
    teacher in a
    school
    wanted
    to
    take
    a
    rest and that’s
    why
    he
    told
    students
    to
    calculate
    the
    sum
    of
    the
    first
    1000
    numbers.Even
    students
    were
    allowed
    to
    use
    a
    calculator, still
    it
    will
    take
    at
    least
    15
    minutes
    to
    add
    all
    the
    numbers.Sonali
    used
    python and she
    was
    able
    to
    answer
    the
    question
    within
    2
    minutes.Write
    a
    code in python
    same as Sonali.
    ○    1.
    Use
    for loop
        ○    2.
        Use
        while loop
            ●    Answer
    ➔  # Find the sum of the first 1000 numbers using for loop
    ➔
    ➔    print("Sum of first n natural numbers")
    ➔    upper_limit = int(input("Enter the upper limit : "))
    ➔
    ➔    count = 0
    ➔    for i in range(upper_limit + 1):
        ➔        count += i
    ➔
    ➔    print("The sum of first", upper_limit, "number is", count)
    ●
    ●

    ●    An
    online
    essay
    writing
    competition
    was
    held in a
    school.The
    students
    were
    required
    to
    write
    at
    least
    250
    words.According
    to
    the
    rule, only
    that
    essay
    should
    be
    checked
    which
    contains
    at
    least
    250
    words.Teachers
    were
    just
    guessing
    the
    number
    of
    words in the
    essay
    but
    that
    was
    not an
    accurate
    way
    to
    count
    the
    number
    of
    words.So
    write
    a
    program
    that
    can
    count
    the
    number
    of
    words in an
    essay(Hint: Take
    input and count
    the
    number
    of
    words
    using
    for loop | Note: to
    count
    the
    number
    of
    words
    you
    can
    just
    count
    the
    number
    of
    blank
    spaces
    given in the
    input. )
    ●    Answer
    ➔  # Find the number words in an essay
    ➔
    ➔    essay = input("Paste your essay here :")
    ➔
    ➔    count = 0
    ➔
    ➔    for i in essay:
        ➔        if i == ' ':
            ➔            count += 1
    ➔
    ➔    words = count + 1
    ➔
    ➔    print("Total number of words in the given essay is:", words)
    ●
