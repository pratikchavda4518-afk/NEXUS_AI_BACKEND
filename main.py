from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


import datetime

import platform

import psutil



from memory import (

    Memory,

    SessionLocal

)



from ai_core import (

    process_command,

    get_ai_info,

    update_ai_config

)





app = FastAPI(

    title="NEXUS AI Backend"

)





app.add_middleware(

    CORSMiddleware,


    allow_origins=["*"],

    allow_credentials=True,


    allow_methods=["*"],


    allow_headers=["*"]

)









@app.get("/")

def home():


    return {


        "message":

        "NEXUS AI Backend Online"

    }









@app.get("/system")

def system_status():


    return {


        "status":

        "ONLINE",



        "time":

        datetime.datetime.now(),



        "machine":

        platform.system(),



        "processor":

        platform.processor()

    }









@app.get("/monitor")

def monitor():


    battery = psutil.sensors_battery()



    return {


        "cpu":

        psutil.cpu_percent(),



        "ram":

        psutil.virtual_memory().percent,



        "disk":

        psutil.disk_usage("/").percent,



        "battery":

        battery.percent

        if battery

        else 100

    }









@app.post("/command")

def command(data:dict):


    user_command = data.get(

        "command",

        ""

    )



    response = process_command(

        user_command

    )



    db = SessionLocal()



    memory = Memory(

        command=user_command,

        response=response

    )



    db.add(memory)



    db.commit()



    db.close()




    return {


        "response":

        response

    }









@app.get("/memory")

def get_memory():


    db = SessionLocal()



    records = db.query(

        Memory

    ).order_by(

        Memory.id.desc()

    ).limit(20).all()




    result=[]




    for item in records:


        result.append({


            "id":

            item.id,



            "command":

            item.command,



            "response":

            item.response

        })




    db.close()



    return result










@app.get("/ai-info")

def ai_info():


    return get_ai_info()










@app.post("/config")

def config(data:dict):


    return update_ai_config(

        data.get("name"),

        data.get("mode"),

        data.get("voice")

    )