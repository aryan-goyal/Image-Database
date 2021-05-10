# Required imports
import os
import humanize
from flask import Flask, request, jsonify, flash, redirect
from firebase_admin import credentials, firestore, initialize_app
from google.cloud import storage

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
doc_coll = db.collection('imageDatabase')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
client = storage.Client()
bucket = client.get_bucket('shopifycodingchallenge.appspot.com')

ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'tiff', 'gif'])


@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add an image to Firestore collection with request body.
        e.g. json={'title': 'Write a blog post'}
    """
    try:
        file = request.files['image']
        if file:
            # upload to GCS
            filename = secure_filename(file.filename)
            blob = bucket.blob(filename)
            blob.upload_from_file(file)
            # log entry in firestore
            doc_coll.document(doc_coll.document().id).set(
                {"filename": filename, "type": file.content_type, "size": humanize.naturalsize(blob.size)})
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/search', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = doc_coll.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in doc_coll.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        doc_coll.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port, debug=False)
