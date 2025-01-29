class Actor :
    def __init__(self,actorId,actorName,actorFollowing) :
        self.actorId = actorId
        self.actorName = actorName
        self.actorFollowing = actorFollowing
    def __str__(self):
        return f"actorId : {self.actorId}, actorName : {self.actorName}, actorFollowing : {self.actorFollowing}"
