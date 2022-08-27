from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "Any string we want"

# Have the root route render a template that displays the number of times the client has visited this site. 
# Refresh the page several times to ensure the counter is working.
@app.route("/")
def groot():
    # We can't increment something that doesn't exist! Here's how to check if a key exists in session yet:
    # session["count"]
    # if 'count' in session:
    #     print('key exists!')
    # else:
    #     print("key 'count' does NOT exist")
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

# Add a "/destroy_session" route that clears the session and redirects to the root route. 
@app.route('/destroy_session')
def destroy_session():
    session.clear()     # clears all keys
    # session.pop('key_name')     # clears a specific key
    return redirect('/')

# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route("/plustwo")
def plustwo():
    session['count'] += 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)