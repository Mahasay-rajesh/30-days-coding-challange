def decor_function(result_function):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print('distinction')
        result_function(marks)
    return distinction
@decor_function
def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print('fail')
    else:
        print('pass')
result([40,35,66,78,89])