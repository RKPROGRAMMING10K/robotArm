from controller import Robot
from controller import Keyboard

robot = Robot()
keyboard = Keyboard()
timeStep = 64

shoulder_lift = robot.getDevice('shoulder_lift_joint')
shoulder_pan = robot.getDevice('shoulder_pan_joint')
elbow = robot.getDevice('elbow_joint')
wrist1 = robot.getDevice('wrist_1_joint')
wrist2 = robot.getDevice('wrist_2_joint')
wrist3 = robot.getDevice('wrist_3_joint')

finger1 = robot.getDevice('palm_finger_1_joint')
finger1_lower_knuckle = robot.getDevice('finger_1_joint_1')
finger1_middle_knuckle = robot.getDevice('finger_1_joint_2')
finger1_upper_knuckle = robot.getDevice('finger_1_joint_3')

finger2 = robot.getDevice('palm_finger_2_joint')
finger2_lower_knuckle = robot.getDevice('finger_2_joint_1')
finger2_middle_knuckle = robot.getDevice('finger_2_joint_2')
finger2_upper_knuckle = robot.getDevice('finger_2_joint_3')

finger3_lower_knuckle = robot.getDevice('finger_middle_joint_1')
finger3_middle_knuckle = robot.getDevice('finger_middle_joint_2')
finger3_upper_knuckle = robot.getDevice('finger_middle_joint_3')

sensor  = robot.getDevice('dsensor')

cam = robot.getDevice('camera')


# keyboard.enable(timeStep)
sensor.enable(timeStep)
cam.enable(timeStep)

cam.recognitionEnable(timeStep)


# print(sensor.getValue())

def addDelay(d_timeStep):
    timeCounter = 0
    while(robot.step(timeStep)!=-1):
        if(timeCounter >=d_timeStep):
            break
        timeCounter +=1
        

def moveBot(a=0, b=0, c=0, d=0, e=0, f=0, g=0.17, h=0.05, i=0, j=-0.06):
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist1.setPosition(d)
    wrist2.setPosition(e)
    wrist3.setPosition(f)

    finger1.setPosition(g)
    finger2.setPosition(g)

    finger1_lower_knuckle.setPosition(h)
    finger2_lower_knuckle.setPosition(h)
    finger3_lower_knuckle.setPosition(h)

    finger1_middle_knuckle.setPosition(i)
    finger2_middle_knuckle.setPosition(i)
    finger3_middle_knuckle.setPosition(i)

    finger1_upper_knuckle.setPosition(j)
    finger2_upper_knuckle.setPosition(j)
    finger3_upper_knuckle.setPosition(j)


shoulder_lift_pos = 0
shoulder_pan_pos = 0
elbow_pos = 0
wrist1_pos = 0
wrist2_pos = 0
wrist3_pos = 0

finger_pos = 0.17
lower_knuckle_pos = 0.05
middle_knuckle_pos = 0
upper_knuckle_pos = -0.06

while (robot.step(timeStep) != -1):
    
    val = sensor.getValue()
    print(val)
    if(val < 400):
        
        firtsObject = cam.getRecognitionObjects()[0]
        color = firtsObject.get_colors()
        red = color[0]
        green = color[1]
        blue = color[2]
        
        moveBot(0.15,1.57,-0.1,-0.04, h=0.3, i=0.3)
        addDelay(10)
        
        moveBot(-0.1,1.57,0,0, h=0.3, i=0.3)
        addDelay(10)
        
        lift_pos = 0
        
        if(red):
            lift_pos = -0.1
        elif(green):
            lift_pos = -0.9
        
        
        moveBot(-0.1,lift_pos,0,0, h=0.3, i=0.3)
        addDelay(10)
        
        moveBot(-0.1,lift_pos,0,0, h=0.05, i=0)
        addDelay(10)
        
        moveBot(-0.1,1.57)
        addDelay(10)
    else:
        moveBot(0.15,1.57,-0.1,-0.04)
        
    
    # keyPressed = keyboard.getKey()

    # if (keyPressed == 317):
    #     shoulder_lift_pos += 0.01
    # elif (keyPressed == 315):
    #     shoulder_lift_pos -= 0.01
    # elif (keyPressed == 314):
    #     shoulder_pan_pos += 0.01
    # elif (keyPressed == 316):
    #     shoulder_pan_pos -= 0.01
    # elif (keyPressed == 87):
    #     elbow_pos += 0.01
    # elif (keyPressed == 83):
    #     elbow_pos -= 0.01
    # elif (keyPressed == 65):
    #     wrist1_pos += 0.01
    # elif (keyPressed == 68):
    #     wrist1_pos -= 0.01
    # elif (keyPressed == 49):
    #     wrist2_pos += 0.01
    # elif (keyPressed == 50):
    #     wrist2_pos -= 0.01
    # elif (keyPressed == 51):
    #     wrist3_pos += 0.01
    # elif (keyPressed == 52):
    #     wrist3_pos -= 0.01

    # elif (keyPressed == 53):
    #     finger_pos += 0.01
    # elif (keyPressed == 54):
    #     finger_pos -= 0.01
    # elif (keyPressed == 55):
    #     lower_knuckle_pos += 0.01
    # elif (keyPressed == 56):
    #     lower_knuckle_pos -= 0.01
    # elif (keyPressed == 57):
    #     middle_knuckle_pos += 0.01
    # elif (keyPressed == 48):
    #     middle_knuckle_pos -= 0.01
    # elif (keyPressed == 45):
    #     upper_knuckle_pos += 0.01
    # elif (keyPressed == 61):
    #     upper_knuckle_pos -= 0.01

    # moveBot(shoulder_lift_pos, shoulder_pan_pos,
            # elbow_pos, wrist1_pos, wrist2_pos, wrist3_pos, finger_pos, lower_knuckle_pos, middle_knuckle_pos, upper_knuckle_pos)
