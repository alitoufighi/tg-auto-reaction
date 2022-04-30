from client import app


@app.on_message()
async def react(_, message):
    print(message)


app.run()
