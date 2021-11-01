from .models import Post
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