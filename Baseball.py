# Final project
# single, double, triple, HOMERUN!!!
# Logan Pennock



for i in range(3):
    speed_of_pitch = int(input("What is the speed of the pitch: "))
    angle_of_bat = int(input("What is the angle of the bat: "))
    speed_of_bat = int(input("What is speed of the bat in newtons: "))
    speed_of_outfielder = 8.8
    overall_speed_of_ball = speed_of_bat - speed_of_pitch
    while angle_of_bat >= 0:
        print ("hit in play")
        if angle_of_bat <= 5:
            print ("your out")
            break
        elif angle_of_bat == (6,):
            print ("you got a single")
            break
        else:
            print("you hit high enough to get more than a single")
    
