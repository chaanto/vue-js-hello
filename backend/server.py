import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# end of instantitate the app

#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
#end cors

#defined data (assume from database)
BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title' : 'Title 1',
        'author' : 'Author 1',
        'read' : True
    },
    {
        'id': uuid.uuid4().hex,
        'title' : 'Title 2',
        'author' : 'Author 2',
        'read' : False
    },
    {
        'id': uuid.uuid4().hex,
        'title' : 'Title 3',
        'author' : 'Author 3',
        'read' : True
    }
]
# end of defined data

#func
def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False
#end func

#Route
@app.route("/members", methods=['GET'])
def members():
    return jsonify("members")

@app.route("/books", methods=['GET', 'POST'])
def books():
    response_object = {'status': 'success'}
    if request.method == 'POST' :
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title' : post_data.get('title'),
            'author' : post_data.get('author'),
            'read' : post_data.get('read')
        })
        response_object['message'] = "added bro!"
    else :
        response_object['books'] = BOOKS
    
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

# end route
if __name__ == "__main__" :
    app.run(debug=True)