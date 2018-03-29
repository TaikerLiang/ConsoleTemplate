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
@api {get} /user get (User info)
@apiName user_get
@apiGroup user
@apiVersion 1.0.0
@apiHeader {String} authorization Basic emai:api_token
@apiHeaderExample {Json} Header-Example:
    {
        "Authorization": "Basic cGF1bEBnbWFpbC5jb206ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SmxlSEFpT2pFMU1qRXpNalEwT0Rnc0ltbGhkQ0k2TVRVeU1UTXdNamc0T0N3aWMzVmlJam9pY0dGMWJFQm5iV0ZwYkM1amIyMGlmUS5LM0pFUm5xUHFsMThUV0RKdGdodnptUG9Ud2xTZ0JlOXdPbDBsczR4OHBB"
    }
@apiParam {String} email required. nerver empty.
@apiParamExample {json} Request-Example:
    {
       'email': 'paul@email.com',
    }
@apiSuccess {number} err 0: successful, -1: error
@apiSuccess {string} err_msg error message
@apiSuccess {string} name user name
@apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "err": 0,
        "err_msg": "",
        "name": "paul"
    }

@apiUse UnauthorizedError
"""

"""
@api {post} /user post (Add a new user)
@apiName user_post
@apiGroup user
@apiVersion 1.0.0
@apiParam {String} email required. user email.
@apiParam {String} password required. user password.
@apiParam {String} name required. user name. 
@apiParamExample {json} Request-Example:
    {
        'name': 'taiker',
        'email': 'taiker@email.com',
        'password': 'taikepassword',
    }
@apiSuccess {number} err 0: successful, -1: error
@apiSuccess {string} err_msg error message
@apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "err": 0,
        "err_msg": "Insert successful."
    }
"""


"""
@api {put} /user put (Update user info)
@apiName user_put
@apiGroup user
@apiVersion 1.0.0
@apiHeader {String} authorization Basic emai:api_token
@apiHeaderExample {Json} Header-Example:
    {
        "Authorization": "Basic cGF1bEBnbWFpbC5jb206ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SmxlSEFpT2pFMU1qRXpNalEwT0Rnc0ltbGhkQ0k2TVRVeU1UTXdNamc0T0N3aWMzVmlJam9pY0dGMWJFQm5iV0ZwYkM1amIyMGlmUS5LM0pFUm5xUHFsMThUV0RKdGdodnptUG9Ud2xTZ0JlOXdPbDBsczR4OHBB"
    }
@apiParam {String} email required. user email.
@apiParam {String} name required. user name.
@apiParamExample {json} Request-Example:
    {
        'email': 'taiker@email.com',
        'name': 'taiker2',
    }
@apiSuccess {number} err 0: successful, -1: error
@apiSuccess {string} err_msg error message
@apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "err": 0,
        "err_msg": "Update successful."
    }
"""

"""
@api {delete} /user delete (Delete user)
@apiName user_delete
@apiGroup user
@apiVersion 1.0.0
@apiHeader {String} authorization Basic emai:api_token
@apiHeaderExample {Json} Header-Example:
    {
        "Authorization": "Basic cGF1bEBnbWFpbC5jb206ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SmxlSEFpT2pFMU1qRXpNalEwT0Rnc0ltbGhkQ0k2TVRVeU1UTXdNamc0T0N3aWMzVmlJam9pY0dGMWJFQm5iV0ZwYkM1amIyMGlmUS5LM0pFUm5xUHFsMThUV0RKdGdodnptUG9Ud2xTZ0JlOXdPbDBsczR4OHBB"
    }
@apiParam {String} email required. user email.
@apiParamExample {json} Request-Example:
    {
        'email': 'taiker@email.com',
    }
@apiSuccess {number} err 0: successful, -1: error
@apiSuccess {string} err_msg error message
@apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "err": 0,
        "err_msg": "Delete successful."
    }
"""
