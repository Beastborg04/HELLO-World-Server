import uuid
import json
class Comments():
    def __init__(self):
        self.comments = []

    def add_comments(self, content, user,):
        comments = {
        "Comment_id": str(uuid.uuid4()),
        "User": user,
        "Comment": content,
        "Likes": 0,
        "Dislikes": 0
    }
        self.comments.append(comments)

    def likes_Comments(self,comment_id):
        for comment in self.comments:
            if comment["Comment_id"] == comment_id:
                comment["Likes"] += 1
                return f"Comment {comment_id} has {comment['Likes']} Likes"
            
        return "Comment nor found"
            
    def dislikes_Comments(self,comment_id):
        for comment in self.comments:
            if comment["Comment_id"] == comment_id:
                comment["Dislikes"] += 1
                return f"Comment {comment_id} has {comment['Dislikes']} Likes"
            
        return "Comment nor found"

    def display_Comments(self):
        if self.comments:
            return json.dumps(self.comments,indent=4)
        else:
            return "There is no comments availavle in the list"
        

class Reply(Comments):
    def __init__(self):
        super().__init__()
        self.reply = []

    def add_reply(self, reply, user, Comment_id):
        reply = {
            "Comment_id": Comment_id,
            "Reply_id": str(uuid.uuid4()),
            "User": user,
            "Reply": reply,
            "Likes": 0,
            "Dislikes": 0
        }
        self.reply.append(reply)

    def likes_Reply(self,Reply_id):
        for reply in self.reply:
            if reply["Reply_id"] == Reply_id:
                reply["Likes"] += 1
                return f"Comment {Reply_id} has {reply['Likes']} Likes"
            else:
                return "Comment nor found"
            
    def dislikes_Reply(self,Reply_id):
        for reply in self.reply:
            if reply["Reply_id"] == Reply_id:
                reply["Dislikes"] += 1
                return f"Comment {Reply_id} has {reply['Dislikes']} Likes"
            else:
                return "Comment nor found"

    def display_reply(self):
        if self.reply:
            return json.dumps(self.reply, indent = 3)
        else:
            return "There is no reply available in the list"
        

tim = Comments()
fred = Reply()

tim.add_comments("Hi my name is tim", "User_1")
tim.add_comments("Hi my name is Fred", "User_2")


comment_id = tim.comments[1]['Comment_id']
fred.add_reply("Hi There", "User_7",comment_id)

tim.likes_Comments(comment_id)
tim.dislikes_Comments(comment_id)


Reply_id = fred.reply[0]['Reply_id']
fred.likes_Reply(Reply_id)
fred.dislikes_Reply(Reply_id)


print(tim.display_Comments())
print(fred.display_reply())

