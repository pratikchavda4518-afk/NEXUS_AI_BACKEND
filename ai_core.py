import datetime
import psutil


from ai_settings import (

    AISettings,

    SessionLocal

)




def load_config():

    db = SessionLocal()


    config = db.query(

        AISettings

    ).first()



    if not config:


        config = AISettings(

            name="NEXUS",

            mode="ACTIVE",

            voice="ENGLISH"

        )


        db.add(config)

        db.commit()

        db.refresh(config)



    db.close()



    return config








def get_ai_info():


    config = load_config()



    return {


        "name":

        config.name,



        "mode":

        config.mode,



        "voice":

        config.voice,



        "version":

        "1.0"

    }









def update_ai_config(

        name=None,

        mode=None,

        voice=None

):


    db = SessionLocal()



    config = db.query(

        AISettings

    ).first()




    if not config:


        config = AISettings()


        db.add(config)




    if name:

        config.name = name




    if mode:

        config.mode = mode




    if voice:

        config.voice = voice




    db.commit()


    db.close()



    return get_ai_info()







def process_command(command):


    config = load_config()



    ai_name = config.name



    command = command.lower().strip()





    if "hello" in command or "hi" in command:


        return (

            f"Hello. "

            f"{ai_name} AI "

            "is online."

        )






    elif "who are you" in command:


        return (

            f"I am {ai_name}. "

            "Your Advanced AI Command System."

        )






    elif "your name" in command:


        return (

            f"My name is {ai_name}."

        )







    elif "status" in command:


        return (

            f"{ai_name} is running "

            f"in {config.mode} mode."

        )







    elif "time" in command:


        return (

            "Current time is "

            +

            datetime.datetime.now()

            .strftime("%H:%M:%S")

        )







    elif "cpu" in command:


        return (

            f"CPU usage is "

            f"{psutil.cpu_percent()} percent."

        )







    elif "ram" in command:


        return (

            f"RAM usage is "

            f"{psutil.virtual_memory().percent} percent."

        )







    elif "battery" in command:


        battery = psutil.sensors_battery()


        if battery:

            return (

                f"Battery is "

                f"{battery.percent} percent."

            )


        return "Battery information unavailable."







    else:


        return (

            "Command received. "

            "AI learning module active."

        )