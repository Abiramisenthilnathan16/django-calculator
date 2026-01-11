from django.shortcuts import render

def home(request):
    expression = request.POST.get("expression", "")
    btn = request.POST.get("btn")

    if request.method == "POST":
        # 1. Handle Clear / All Clear
        if btn in ["C", "AC"]:
            expression = ""
        
        # 2. Handle Equals (Calculation)
        elif btn == "=":
            try:
                # Replace visual symbols with python operators before evaluating
                safe_expression = expression.replace('÷', '/').replace('×', '*')
                # eval handles basic math. 
                # round() is used to match the "Decimal places - 2" look from the UI
                result = eval(safe_expression)
                expression = str(round(result, 2))
            except Exception:
                expression = "Error"

        # 3. Handle Backspace (The ← button)
        elif btn == "back":
            expression = expression[:-1]

        # 4. Handle Special buttons
        elif btn == "00":
            expression += "00"
            
        # 5. Handle Square Root (Simple version)
        elif btn == "sqrt":
            try:
                import math
                expression = str(round(math.sqrt(float(expression)), 2))
            except:
                expression = "Error"

        # 6. Default: Append button value to the expression
        else:
            if btn is not None:
                # If the previous result was "Error" or "0", start fresh
                if expression == "Error" or expression == "0":
                    expression = btn
                else:
                    expression += btn

    return render(request, "home.html", {"expression": expression})