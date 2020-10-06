from time import sleep
import tellopy

def main():
    drone = tellopy.Tello()
    try:
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(5)
        drone.clockwise(50)
        sleep(3)
        drone.clockwise(0)
        sleep(1)
        drone.counter_clockwise(50)
        sleep(3)
        drone.counter_clockwise(0)
        sleep(1)
        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    main()