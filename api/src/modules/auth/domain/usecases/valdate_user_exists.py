

class ValidateUserExists:
    def __init__(self, user_repository : UserReositoryInterface) -> None:
        self.user_repository = user_repository
    
    async def execute(self, ):
        raise NotImplementedError