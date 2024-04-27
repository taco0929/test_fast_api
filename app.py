import uvicorn
from fastapi import FastAPI, Header, Request
from request_model import EchoBody

app = FastAPI()

@app.post(path = '/echo')
def post(request: Request, data: EchoBody, authorization: str = Header('')):
    print(f'token: {authorization}')
    if authorization:
        authorization = authorization.split()
        if authorization[0] != 'Token':
            print('token not ok')
        else:
            print('token ok')
    print(data.model_dump())
    return {'msg': 'ok'}

if __name__ == '__main__':
    uvicorn.run(app, port = 12345)
