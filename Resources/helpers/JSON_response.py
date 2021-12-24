from fastapi.responses import JSONResponse

class ReplyMessage:
    @staticmethod
    def successful_response_code( code: int ):
        return JSONResponse(
            content={ 
                'ok': True 
            },
            status_code=code
        )

    @staticmethod
    def successful_response( code: int, msg: str ):
        return JSONResponse(
            content={
                'ok': True,
                'msg': msg
            },
            status_code=code
        )

    @staticmethod
    def failed_response( code: int, msg: str ):
        return JSONResponse(
            content={
                'ok': False,
                'msg': msg
            },
            status_code=code
        )
    
    @staticmethod
    def successful_response_content( code: int, msg: str, content ):
        return JSONResponse(
            content={
                'ok': True,
                'msg': msg,
                'content': content
            },
            status_code=code
        )