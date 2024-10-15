class Comments:
    def __init__(self):
        # Initialize an empty list to store comments
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def display_comments(self):
        # Display all comments
        if not self.comments:
            return "No comments yet."
        return "\n".join(self.comments)


comment_system = Comments()


comment_system.add_comment("This is the first comment!")
comment_system.add_comment("Great post, very informative.")
comment_system.add_comment("I learned a lot from this.")


print("Comments:", comment_system.display_comments())

