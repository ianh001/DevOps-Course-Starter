from flask import Flask
from flask import render_template
from flask import request 
from flask import redirect

from todo_app.flask_config import Config
#from todo_app.data.session_items import add_item
#from todo_app.data.session_items import get_item, save_item
from todo_app.trello import get_items, add_item, complete_item, get_item
from todo_app import trello

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():

    current_items=sorted(get_items(), key=lambda x: x['status'], reverse=True)  
    return render_template('index.html', items=current_items)

@app.route('/additem', methods=['POST'])
def additem():    
    add_item(request.form.get('title'))
    return redirect('/') 

#Add mark item as complete
#@app.route('/complete', methods=['POST'])
#def complete():
#    id_to_complete = request.form.get('ID')
#    item_to_complete = get_item(id_to_complete)
#    if item_to_complete is None:
#        return redirect('/')
#    else:
#        item_to_complete.update({'status':'Complete'})
#        save_item(item_to_complete) 
#        return redirect('/')

@app.route('/complete', methods=['POST'])
def complete():
    id_to_complete = request.form.get('ID')
    item_to_complete = get_item(id_to_complete)

    if item_to_complete is None:
        return redirect('/')
    else:
        item_id = item_to_complete['id']
        complete_item(item_id)  # Call the complete_item function from trello.py
        return redirect('/')
       
    
if __name__ == '__main__':
    app.run
    
    
    
 