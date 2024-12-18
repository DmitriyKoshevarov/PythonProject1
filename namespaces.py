def test_function(a):
    def inner_function(a):
        print('Я в области видимости функции test_function')
    inner_function(a)

test_function(2)

inner_function(2)