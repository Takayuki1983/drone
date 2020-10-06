import sys
import traceback
import tellopy
import av
import cv2.cv2 as cv2
import numpy
import time
import os
import datetime


def main():
    drone = tellopy.Tello()

    try:
        drone.connect()
        drone.wait_for_connection(60.0)
        #drone.takeoff()
        retry = 3
        container = None
        while container is None and 0 < retry:
            retry -= 1
            try:
                container = av.open(drone.get_video_stream())
            except av .AVError as ave:
                print(ave)
                print('retry')

        frame_skip = 300
        i = 0
        while True:
            for frame in container.decode(video=0):
                if 0 < frame_skip:
                    frame_skip = frame_skip - 1#
                    continue
                start_time = time.time()
                image = cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)
                #略
                cv2.imshow('image', image)
                #画像を保存
                #drone.clockwise(50)
                cv2.imwrite('/Users/user/Desktop/pic/lena_opencv_red.jpg', image)
                #cv2.imwrite('/Users/user/Desktop/pic.jpg', image)
                #cv2.imwrite(os.path.join('/Users/user/Desktop/pic/'+"pic_00"+str(i)+".jpg"), image)
                #drone.clockwise(0)
                #drone.forward(40)

                #cv2.imwrite(os.path.join('/Users/user/Desktop/pic/'+"pic_00"+str(i+1)+".jpg"), image)
                
                i = i + 1
                

                cv2.waitKey(1)
                if frame.time_base < 1.0/60:
                    time_base = 1.0/60
                else:
                    time_base = frame.time_base
                #フレームスキップ値を算出
                frame_skip = int((time.time() - start_time) / time_base)

        

    except Exception as ex:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print(ex)
    finally:
        drone.quit()
        cv2.destroyAllAiundows()

if __name__ == '__main__':
    
    main()            

    