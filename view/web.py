import sys
sys.path.append('.')

from flask import Flask, render_template
from controllers.category_controller import CategoryController

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category')
def category():
    controller = CategoryController()
    categories = controller.read_all()
    return render_template('list_categories.html', categories=categories)



app.run(debug=True)