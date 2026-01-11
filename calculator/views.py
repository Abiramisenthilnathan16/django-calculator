from django.shortcuts import render

def home(request):
    expression = ""

    if request.method == "POST":
        expression = request.POST.get("expression")
        btn = request.POST.get("btn")

        if expression is None:
            expression = ""

        if btn == "C":
            expression = ""
        elif btn == "=":
            try:
                expression = str(eval(expression))
            except:
                expression = "Error"
        else:
            if btn is not None:
                expression += btn

    return render(request, "home.html", {"expression": expression})
