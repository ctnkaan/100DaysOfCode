#front_is_clear() 
#wall_in_front()
#right_is_clear() 
#wall_on_right()
#at_goal()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
i = 0
while not at_goal():
    if right_is_clear():
        i+=1
        
        if i >= 6:
            if front_is_clear():
                i=0
                move()
            else:
                turn_left()
 
        elif right_is_clear:         
            turn_right()
            move()
    elif front_is_clear():
        i=0
        move()
    else:
        i=0
        turn_left()