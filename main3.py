from pyscript import display, document 


def ave_numbers(e): # e for event handler
    num1 = float(document.getElementById("Score1").value)
    num2 = float(document.getElementById("Score2").value)
    result = (num1 + num2) / 2 #formula
    

    display(result, target="average", append=False) #average displayer
    if result >= 75:
        display("yep", target="pass", append=False)
    else:
        display("nope", target="pass", append=False)

        #passing or failing grade