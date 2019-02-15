def Fizzbuzz (list1, list2):
    totallength = len(list1) + len(list2)

    if totallength % 3 == 0:
        return 'Fizz'

        elif totallength % 5 == 0:
            return 'Buzz'

            elif totallength % 5 == 0 and totallength % 3 ==0:
                return 'FizzBuzz'

                else:
                    return totallength
                

            

    