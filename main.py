from fastapi import Request, FastAPI


def _to_file(json: str):
    with open("json_logs.txt", "a") as file:
        file.write(json + '\n')


app = FastAPI()


@app.post("/webhook", status_code=200)
async def get_publication_by_bookmark(request: Request):
    json = await request.json()
    print(json)
    _to_file(str(json))
    return {'status': 'ok'}

