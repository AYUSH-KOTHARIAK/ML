from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # decorator --> just like inheritance of oop
# app is my object which i create 
def some_function():
    return "Some message from flask "


# @app.route('/home')
# def some_function2():
#     return render_template('Home.html')
# Renders the 'Home.html' template and returns it as the response
# Make sure to create a folder named 'templates' in the same directory as your Python file
# All your HTML files should be placed in this 'templates' folder

@app.route('/home/<name>')
def some_function2(name):
    print(name)  # This will print the name to the console for debugging purposes
    return render_template('Home.html', name_value=name)

app.run(debug=True)