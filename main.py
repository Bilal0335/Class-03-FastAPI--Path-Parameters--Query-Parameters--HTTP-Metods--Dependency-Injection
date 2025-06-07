from fastapi import FastAPI, Path,Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/username/{username}/{user_id}")
def read_user(
    username: str,
    user_id: int = Path(..., gt=1, lt=100)
):
    return {"username": username, "user_id": user_id}

@app.get("/username/junaid")
def read_username_junaid():
    return {"username": "Junaid Hussain"}

@app.get("/username/bilal?token=1234&")
def read_username():
    return {"username": "Bilal"}


@app.get("/username/all")
def read_all_usernames(limit:int | None = Query(default=10, ge=1, le=10)):
    print(f"Limit: {limit}")
    if limit is not None:
        return {"usernames": ["Junaid Hussain"]}
    else:
        return {"usernames": ["Junaid Hussain", "Bilal"]}