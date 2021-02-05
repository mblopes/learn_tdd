import sys
sys.path.append('.')

from flask import Flask, render_template, redirect, request
from controllers.category_controller import CategoryController
from models.category_model import Category

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

@app.route('/category/create', methods=['POST', 'GET'])
def create_category():
    if request.method == 'POST':
        controller = CategoryController()
        name = request.form['name']
        description = request.form['description']
        category = Category(name, description)
        controller.create(category)
        return redirect('/category')
    
    return render_template('create_category.html')

@app.route('/category/delete/<int:id>')
def delete_category(id):
    controller = CategoryController()
    category = controller.read_by_id(id)
    controller.delete(category)
    return redirect('/category')



app.run(debug=True)