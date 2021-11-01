from .models import Post
from ariadne import convert_kwargs_to_snake_case
def listPosts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        payload = {
            "success": True,
            "posts": posts
        }

    except  Exception as err:
        payload = {
            "success" : False,
            "errors": [str(err)]
        }
    
    return payload

@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    
    except AttributeError: #todo not found
        payload = {
            "success": False,
            "error":["Post item matchin {id} not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def delete_post_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {"success": True, "post": post.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload 