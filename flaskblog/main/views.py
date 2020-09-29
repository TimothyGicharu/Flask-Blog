from flask import render_template, request,Blueprint
from flaskblog.models import Post, Quotes
from ..requests import get_quotes

main = Blueprint('main', __name__)


@main.route('/')
def index():
    quotes = get_quotes()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('index.html', posts=posts, quotes=quotes)


@main.route('/about')
def about():
    title = 'About'
    return render_template('about.html', title=title)

