from flask import Flask,render_template,request


app=Flask("__name__")



@app.route('/',methods=["GET","POST"])
def form():
    
    if request.method=="GET":
        return render_template('button.html')
    import random
    cnumber = random.randrange(0,5)
    user_input = int(request.form["user_input"])
    
    Match=""

    if(cnumber != user_input):
       Match = "Match Not Found"
        
    else:
        Match = "Match Found"
    
    return render_template('button.html',Match=Match,cnumber=cnumber,user_input=user_input)
if __name__ == "__main__":
    app.run(debug=True)
    