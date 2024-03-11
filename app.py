from flask import Flask,render_template,request
import re

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index(): 
        return render_template("index.html")
        
@app.route("/results",methods=['POST'])
def results():
        if request.method == 'POST':
        # Get the regex pattern and test string from the form
            regex_pattern = request.form.get("regex_pattern")
            test_string= request.form.get("test_string")
        # match the regex pattern with test string
            matches = re.findall(regex_pattern,test_string)
            no_matches = len(matches)
        # Result:
            if matches:
                result = f"Pattern '{regex_pattern}' ==> {no_matches} matches found."
            else:
                result = f"Pattern '{regex_pattern}'==> {no_matches} matches found."
        return render_template('index.html', results=result,matches=matches,no_matches=no_matches)

@app.route("/email_id",methods=['POST','GET'])
def email():
    if request.method == 'POST':
        # Get the email id from the form
        email = request.form.get('emailid')
        # email pattern
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        # Match the email_id with email_pattern
        email_matches = re.match(email_pattern,email)
        # Result:
        if email_matches:
            email_results = f"{email} is a valid Email Id."
        else:
            email_results = f"{email} is not a valid Email Id."
    return render_template('index.html',email_results=email_results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
