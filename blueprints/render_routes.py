from flask import Blueprint, render_template

sidebar_route = Blueprint('sidebar', __name__)


@sidebar_route.route('/render-sidebar-html')
def render_sidebar():
    return render_template('sidebar.html')