from flask import Flask, render_template, request # from package import class

app = Flask(__name__)

# # flask basics
# @app.route('/')
# def index():
#     return "<h1>Hello Puppy!</h1>"
#
# @app.route('/information')
# def info():
#     return "<h1>Puppies are cute!</h1>"
#
# @app.route('/puppy/<name>')
# def puppy(name):
#     return "<h1>this is a page for {}</h1>".format(name.upper())

# # template basics (connect to HTML) and static file
# # how to pass python variable to the html file
# # 'basic.html' should be in a folder 'templates'
# @app.route('/')
# def index():
#     name = 'Tianyu'
#     letters = list(name)
#     pup_dictionary = {'pup_name':'Sammy'}
#     return render_template('basic.html', name=name, letters=letters,
#     pup_dictionary=pup_dictionary)

# # template control flow
# # html for loop
# @app.route('/')
# def index():
#     # code code
#     user_logged_in = True
#     mylist = [1,2,3,4,5]
#     return render_template('basic2.html', mylist=mylist,
#                         user_logged_in=user_logged_in)

# # template inheritance
# # did not call 'base.html'
# @app.route('/')
# def index():
#     return render_template('home.html')
# @app.route('/puppy/<name>')
# def pup_name(name):
#     return render_template('puppy.html',name=name)

# # html form
# @app.route('/')
# def index():
#     return render_template('signup_home.html')
# @app.route('/signup_form')
# def signup_form():
#     return render_template('sign_up.html')
# @app.route('/thank_you')
# def thank_you():
#     first = request.args.get('first')
#     last = request.args.get('last')
#     return render_template('thank_you.html',first=first,last=last)
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# # e1
# @app.route('/')
# def index():
#     return render_template('e1_1.html')
# @app.route('/result')
# def result():
#     name = request.args.get('name')
#     rules = [
#     lambda s: any(x.isupper() for x in name) or 'must have an upper case letter',
#     lambda s: any(x.islower() for x in name) or 'must have an lower case letter',
#     lambda s: name[-1].isdigit()                 or 'must have a number at the end',
#     ]
#     problems = [p for p in [r(name) for r in rules] if p != True]
#     problems_len = len(problems)
#     return render_template('e1_2.html',problems=problems,problems_len=problems_len)





if __name__ == '__main__':
    app.run(debug=True)
