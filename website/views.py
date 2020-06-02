from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def add(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    num_past_1 = num_1
    num_past_2 = num_2

    if request.method == "POST":
        answer = request.POST['answer'] #Ten answer jest właśnie tym name, które sobie zdefiniowałem w formularzu
        old_num_1 = request.POST['old_num_1']
        old_num_2 =request.POST['old_num_2']

        #Error handling if no form fillout
        if not answer:
            my_answer= "Chyba zapomniałeś wpisać liczb"
            return render(request, 'add.html',{
                'my_answer':my_answer,
                'answer':answer,
                'num_1':num_1,
                'num_2':num_2,
                })

        correct_answer =int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Super! " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Niestety nie udało Ci się, " + "poprawny wynik to: " + old_num_1 + " + " + old_num_2 +  " = " + str(correct_answer)
            color="danger"

        return render(request, 'add.html',{
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

    return render(request,'add.html',{
        'num_1':num_1,
        'num_2':num_2,
    })

def substract(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer'] #Ten answer jest właśnie tym name, które sobie zdefiniowałem w formularzu
        old_num_1 = request.POST['old_num_1']
        old_num_2 =request.POST['old_num_2']

        #Error handling if no form fillout
        if not answer:
            my_answer= "Chyba zapomniałeś wpisać liczb"
            return render(request, 'add.html',{
                'my_answer':my_answer,
                'answer':answer,
                'num_1':num_1,
                'num_2':num_2,
                })

        correct_answer =int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Super! " + old_num_1 + " - " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Niestety nie udało Ci się, " + "poprawny wynik to: " + old_num_1 + " - " + old_num_2 +  " = " + str(correct_answer)
            color="danger"

        return render(request, 'substract.html',{
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

    return render(request,'substract.html',{
    'num_1':num_1,
    'num_2':num_2,
    })
    
def multiply(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer'] #Ten answer jest właśnie tym name, które sobie zdefiniowałem w formularzu
        old_num_1 = request.POST['old_num_1']
        old_num_2 =request.POST['old_num_2']

        #Error handling if no form fillout
        if not answer:
            my_answer= "Chyba zapomniałeś wpisać liczb"
            return render(request, 'add.html',{
                'my_answer':my_answer,
                'answer':answer,
                'num_1':num_1,
                'num_2':num_2,
                })

        correct_answer =int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Super! " + old_num_1 + " * " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Niestety nie udało Ci się, " + "poprawny wynik to: " + old_num_1 + " * " + old_num_2 +  " = " + str(correct_answer)
            color="danger"

        return render(request, 'multiply.html',{
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

    return render(request,'multiply.html',{
    'num_1':num_1,
    'num_2':num_2,
    })

def divide(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(1,10)

    if request.method == "POST":
        answer = request.POST['answer'] #Ten answer jest właśnie tym name, które sobie zdefiniowałem w formularzu
        old_num_1 = request.POST['old_num_1']
        old_num_2 =request.POST['old_num_2']

        #Error handling if no form fillout
        if not answer:
            my_answer= "Chyba zapomniałeś wpisać liczb"
            return render(request, 'add.html',{
                'my_answer':my_answer,
                'answer':answer,
                'num_1':num_1,
                'num_2':num_2,
                })

        correct_answer =int(old_num_1) / int(old_num_2)
        if float(answer) == correct_answer:
            my_answer = "Super! " + old_num_1 + " / " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Niestety nie udało Ci się, " + "poprawny wynik to: " + old_num_1 + " / " + old_num_2 +  " = " + str(correct_answer)
            color="danger"

        return render(request, 'divide.html',{
            'answer':answer,
            'my_answer':my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })

    return render(request,'divide.html',{
    'num_1':num_1,
    'num_2':num_2,
    })