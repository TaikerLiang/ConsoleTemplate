"""
@apiDefine NotFoundError
@apiError 404 NotFound
@apiErrorExample Error-Response:
    HTTP/1.1 404 Not Found
    {
        "error": "not found"
    }
"""


"""
@apiDefine UnauthorizedError
@apiError 401 Unauthorized: Access is denied due to invalid credentials
@apiErrorExample Error-Response:
    HTTP/1.1 401 Unauthorized
    {
        "error": "Unauthorized: Access is denied due to invalid credentials."
    }
"""


"""
@api {post} /login Login (Login action)
@apiName Login
@apiGroup base
@apiVersion 1.0.0

@apiParam {String} email required. nerver empty.
@apiParam {String} password optional. can be empty string, if there is a login_token.
@apiParam {String} login_token optional. can be empty string, if there is no login_token. 
@apiParamExample {json} Request-Example:
    {
       'email': 'taiker@email.com',
       'password': 'taikepassword',
       'login_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0OTk4MDc0MjMsImlhdCI6MTQ5OTc4NTgyMywic3ViIjoiam9obkBlbWFpbC5jb20ifQ.dXO7O0bUVmGtD9qlZKmywUtI9jJTkFsEP71IZpjoD54'
    }

@apiSuccess {number} err 0: successful, -1: error
@apiSuccess {string} err_msg error message
@apiSuccess {string} api_token for api authentication, and you should store in code, not in cookie. (Prevent CSRF Attack)
@apiSuccess {string} login_token for login authentication, and you can store in cookie for quick login.

@apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "err": 0,
        "err_msg": "",
        "api_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjEzMjQ0ODgsImlhdCI6MTUyMTMwMjg4OCwic3ViIjoicGF1bEBnbWFpbC5jb20ifQ.K3JERnqPql18TWDJtghvzmPoTwlSgBe9wOl0ls4x8pA",
        "login_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0OTk4MDc0MjMsImlhdCI6MTQ5OTc4NTgyMywic3ViIjoiam9obkBlbWFpbC5jb20ifQ.dXO7O0bUVmGtD9qlZKmywUtI9jJTkFsEP71IZpjoD54"
    }

@apiSuccessExample {json} Failed-Response:
    HTTP/1.1 200 OK
    {
        "err": -1,
        "err_msg": "Invalid password.",
    }
    HTTP/1.1 200 OK
    {
        "err": -1,
        "err_msg": "Invalid email.",
    }
    HTTP/1.1 200 OK
    {
        "err": -1,
        "err_msg": "Invalid token. Please log in again.",
    }

@apiUse NotFoundError
"""


"""
@api {get} /dashboard dashboard (Dashboard Page)
@apiName dashboard
@apiGroup base
@apiVersion 1.0.0
@apiHeader {String} authorization Basic emai:api_token
@apiHeaderExample {Json} Header-Example:
    {
        "Authorization": "Basic cGF1bEBnbWFpbC5jb206ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SmxlSEFpT2pFMU1qRXpNalEwT0Rnc0ltbGhkQ0k2TVRVeU1UTXdNamc0T0N3aWMzVmlJam9pY0dGMWJFQm5iV0ZwYkM1amIyMGlmUS5LM0pFUm5xUHFsMThUV0RKdGdodnptUG9Ud2xTZ0JlOXdPbDBsczR4OHBB"
    }
@apiSuccess {number} err 0: successful, -1: error
@apiSuccess {string} err_msg error message
@apiSuccess {string} res return info
@apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "err": 0,
        "err_msg": "",
        "res": "This is dashboard"
    }

@apiUse UnauthorizedError
"""
