# pip3 install fastapi uvicorn
from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get('/check_domain/{domain}')
async def check_domain(domain: str, user_agent: str = Header(None)):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"

    headers = {"accept": "application/json", "x-apikey": "9f7cf5c129825162b49fb1b9d20b921d794471c1e4861c919279ab1be9696330"}

    if user_agent:
        headers["User-Agent"] = user_agent

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Domain not found", headers={"Access-Control-Allow-Origin": "*"})

    content = response.json()
    
    res_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    }

    return JSONResponse(content=content, headers=res_headers)

if _name_ == '_main_':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)