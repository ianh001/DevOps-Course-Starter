from flask import Flask
from flask import render_template
from flask import request 
from flask import redirect

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()    
    return render_template('index.html',items=items)

@app.route('/additem', methods=['POST'])
def additem():    
    add_item(request.form.get('title'))
    return redirect('/') 

if __name__ == '__main__':
    app.run
    