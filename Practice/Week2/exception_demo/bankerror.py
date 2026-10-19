class LimitExceedError(Exception):
    def __init__(self,amount):
            self.amount=amount
            self.message= "Limit Exceeded"
            super().__init__(self.message)