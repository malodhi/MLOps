from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
import uvicorn
from utils import calculate_simpleInterest
# instantiate fastapi
app= FastAPI()

@app.get("/get-simpleInterest/")
async def get_input(request:Request):
    """
        Get inputs from users and call the simple interest function to evaluate
        the parameters then return the output.
    """
    getInput = await request.json()
    principal = getInput['principle']
    rate = getInput['rate']
    period = getInput['time']

    # evaluate interest
    interest = calculate_simpleInterest(principal, rate, period)

    return jsonable_encoder([{'interest': interest}, getInput])

# main driver app
if __name__=='__main__':
    uvicorn.run(app)