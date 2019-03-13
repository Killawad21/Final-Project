'''
Logan Pennock
3/13/19
single, double, triple, HOMERUN!!!!
Final Project
all work done in assosiation with Korbin Griffin
the code is to determine if your three at bats get a single double triple or homerun.
it does this by using the speed of the pitch, the angle of the bat, the speed of your hit
and the speed of the outfielder
'''



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
        elif angle_of_bat <= 30 and angle_of_bat >= 6:
            print ("you got a single")
            break
        else:
            print("you hit high enough to get more than a single")
            x = True
            break
# Uses overall_speed_of_ball and angle_of_bat to determine if infield or not
    while x == True:
        if overall_speed_of_ball >= 20 and angle_of_bat <= 50:
            print ("you got a single")
            break
        elif overall_speed_of_ball >= 21 and overall_speed_of_ball <= 60 and angle_of_bat >= 91:
            print ("you got to the outfield")
            ball_catch = overall_speed_of_ball / speed_of_outfielder
# Uses ball_catch to determine if the outfielder can reach the ball in time
            if ball_catch <= 7:
                print ("ball caught")
                break
            elif ball_catch >= 8 and ball_catch <= 10:
                print ("you got a single")
                break
            elif ball_catch >= 11 and ball_catch <= 17:
                print("you got a double")
                break
            elif ball_catch >= 18 and ball_catch <= 30:
                print("you got a triple")
                break
            else:
                print ("HOMERUN!!!")
                break
