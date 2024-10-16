import uuid
import json
class Comments():
    def __init__(self):
        self.comments = []

    def add_comments(self, content, user,):
        comments = {
        "Comment_id": str(uuid.uuid4()),
        "User": user,
        "Comment": content
    }
        self.comments.append(comments)

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
            "Reply": reply
        }
        self.reply.append(reply)

    def display_reply(self):
        if self.reply:
            return json.dumps(self.reply, indent = 3)
        else:
            return "There is no reply available in the list"
        

tim = Comments()
fred = Reply()

tim.add_comments("Hi my name is tim", "User_1")
tim.add_comments("Hi my name is Fred", "User_2")


comment_id = tim.comments[0]['Comment_id']
fred.add_reply("Hi There", "User_7",comment_id,)


print(tim.display_Comments())
print(fred.display_reply())

