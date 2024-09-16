from flask import Flask, render_template, request, Response, jsonify
from functions.search_multi import fetch_posts, get_info # Import your fetch_posts function
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    query = request.form.get('query')  # Get search query from the form
    results = []
    if query:
        headers = {'User-Agent': 'Mozilla/5.0'}  # Define your headers
        results = fetch_posts(query, headers)  # Fetch search results based on the query
    return render_template('index.html', results=results)
@app.route('/proxy-image')
def proxy_image():
    image_url = request.args.get('url')
    response = requests.get(image_url, stream=True)
    return Response(response.content, content_type=response.headers['Content-Type'])
    
@app.route('/get-movie-info')
def get_movie_info():
    link = request.args.get('link')
    headers = {
        'User-Agent': 'your-user-agent'
    }
    
    movie_info = get_info(link, headers)
    
    return jsonify(movie_info) 
if __name__ == '__main__':
    app.run(debug=True)