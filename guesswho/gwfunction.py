import picamera,time


#
def getPic(name):
    try:
        with picamera.PiCamera() as camera:
            q = "n"
            while q == "n":
                print("Say cheese!")
                camera.start_preview()
                time.sleep(3)
                fn = "{0}.jpeg".format (name)
                camera.capture(fn)
                camera.stop_preview()
                q = input("Is this image okay? (y/n)  ")
    except picamera.exc.PiCameraMMALError:
        print("*** Camera is not connected, re-connect it and reboot. ***")
    print("Your file is called {0}.jpeg".format (name))
    return fn


#
def getChar():

    hairList=["Brown","Blonde","Ginger","Bald"]
    eyeList=["Brown","Green","Blue","Grey","Hazel"]
    glassesList=["y","n"]
    genderList=["Male","Female","Other"]
    hatList=["y","n"]
    facialList=["y","n"]
    
    
    name = ""
    while name == "":
        name = input("What is your name?")
    hair = ""
    while not (hair in hairList):
        hair = input("what colour hair do you have? (Brown/Blonde/Ginger/Bald)")
    eyes = ""
    while not (eyes in eyeList):
        eyes = input("What colour eyes do you have? (Brown/Green/Blue/Grey/Hazel)")
    glasses = ""
    while not (glasses in glassesList):
        glasses = input("Do you wear glasses or not? (y/n)")
    gender = ""
    while not (gender in genderList):
        gender = input("What gender are you? (Male/Female/Other)")
    hat = ""
    while not (hat in hatList):
        hat = input("Are you wearing a hat or not? (y/n)")
    facial = ""
    while not (facial in facialList):
        facial = input("Do you have facial hair? (y/n)")
    filename = getPic(name)

    profilelist = [name,hair,eyes,glasses,gender,hat,facial]

    return profilelist
    
