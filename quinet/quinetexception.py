class QuinetException(Exception):
    def __init__(self,ErrorInfo):
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo