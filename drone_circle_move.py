from time import sleep
import tellopy
import math
from PIL import Image, ImageFilter

n = 8#n角形
R = 60#円の半径(cm)

rad = (180*(n-2)) / n#n角形の内角一つの角度
rad2 = 360 / n#三角関数計算用
X = R * math.sin(rad2)
Y = R * (1 - math.cos(rad2))
print(X)
print(Y)
def main():
    drone = tellopy.Tello()
    try:
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(1)
        drone.take_picture()
        #drone.clockwise(rad)
        #drone.land()
        i = 1
        
        while i <= n:
            drone.left(X)
            drone.forward(Y)
            sleep(3)
            drone.clockwise(rad)
            sleep(1)
            #drone.take_picture()
            #pic = drone.take_picture()
            #pic = 
            #pic.show()
            #pic.save('/Users/user/Desktop/lenna_square_pillow.jpg', quality=95)
            i = i + 1

        drone.land()
        sleep(1)
        drone.land()
        sleep(1)
        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    main()


