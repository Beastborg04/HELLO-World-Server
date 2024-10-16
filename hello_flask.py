# from flask import Flask, request,jsonify

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello World"

# if __name__ == '__main__':
#     app.run(debug = True)




from flask import Flask,  request, jsonify
import uuid

app = Flask(__name__)

list_of_comments = []


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return data['age']

@app.route('/comments', methods = ["POST"])
def add_comments():
    comments = request.json
    comment = comments.get('comment')
    comment_id = uuid.uuid4()
    if comment:
        list_of_comments.append({"Comment id": comment_id, "comment": comment, "replies": []})
        return jsonify({'message': "Your comment has been successfully added",
                        "comment": comment,
                        "comment_id": comment_id})

    else:
        return jsonify({"ERROR": "Your comment has not been added"}) 
       
    

@app.route('/display_comments', methods = ["GET"])
def get_comments():
    return jsonify[{"comments": list_of_comments}], 200
               
    

@app.route('/reply/<int:comment_id>', methods = ["post"])
def add_reply(comment_id):
    reply_data = request.json
    reply = reply_data.get('reply')
    global list_of_comments

    if comment_id< 0 or comment_id > len(list_of_comments):
        return jsonify({"ERROR": "Comment is not available"})

    if reply:
        list_of_comments[comment_id]["replies"].append({"reply": reply, "reply_to_reply": []})
        return jsonify({
            "message" : "Your reply has been successfully added",
            "comment_id": comment_id,
            "reply": reply
        })
    else:
        return jsonify({"ERROR": "Your reply has not been added"}), 500
    
@app.route('/display_reply', methods = ["GET"])
def get_reply():
    return jsonify({"comments" : list_of_comments}), 200
    


@app.route('/reply_to_reply/<int:comment_id>/<int:reply_id>', methods = ["POST"])
def add_reply_to_reply(comment_id, reply_id):
    reply_to_reply_data = request.json
    reply_to_reply = reply_to_reply_data.get('reply_to_reply')

    if comment_id<0 or comment_id> len(list_of_comments):
        return jsonify({"ERROR": "The comment is not available"}), 404
    
    if reply_id <0 or reply_id> len(list_of_comments[comment_id]["replies"]):
        return jsonify({"ERROR": "The reply is not available"}), 404

    if reply_to_reply:
        list_of_comments[comment_id]["replies"][reply_id]["reply_to_reply"].append(reply_to_reply)
        return jsonify({
            "message": "Your reply to the reply has been added",
            "comment_id": comment_id,
            "reply_id": reply_id,
            "reply to reply": reply_to_reply 
        }) ,201
    else:
        return jsonify({"ERROR": "Your reply to reply has NOT been added"}), 404

# @app.route('display of reply to reply', methods = ["GET"])
# def get_reply_to_reply():
    # wants to return the list of replies to replies


# @app.route('/comments/like', methods = ["Post"])
# def like_comment(comment_id):
#     if comments['id'] == comment_id:
#         comments['Like'] +=1
#         return "You have liked the comment!!!!"
#     else:
#         return "ERROR"
    

# @app.route('/comments/dislike', methods = ["Post"])
# def like_comment(comment_id):
#     if comments['id'] == comment_id:
#         comments['dislike'] +=1
#         return "You have disliked the comment!!!!"
#     else:
#         return "ERROR"
    


if __name__ == '__main__':
    app.run(port=8081)