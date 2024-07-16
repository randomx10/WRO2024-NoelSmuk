#!/usr/bin/env python3
'''Measures distances in the back, front, left, and right directions in meters'''
import rplidar
from rplidar import RPLidar
import numpy as np
import time
import serial

PORT_NAME = '/dev/wro/lidar'
ARDUINO_PORT = '/dev/wro/arduino'
DMAX = 4000
DELAY = 0.1  # Delay in seconds
ser = serial.Serial(ARDUINO_PORT, 115200, timeout=5)
TURNING = False

def calculate_cartesian_coordinates(angle_rad, distance_mm):
    distance_m = distance_mm / 1000.0  # Convert to meters
    x = distance_m * np.cos(angle_rad)
    y = distance_m * np.sin(angle_rad)
    return x, y

def run():
    ser.write(str.encode('f9'))
    lidar = RPLidar(PORT_NAME, 115200, 3)
    lidar.start_motor()
    try:
        TWIST=0
        ser.write(str.encode('f9'))
        for scan in lidar.iter_scans():
            min_distances = {
                'left': float('inf'),
                'right': float('inf'),
                'front': float('inf'),
                'back': float('inf')
            }

            for quality, angle, distance_mm in scan:
                angle_rad = np.radians(angle)
                if 50 <= angle <= 100 or 250 <= angle <= 300:  # Front or back
                    if 50 <= angle <= 100:  # Front
                        min_distances['front'] = min(min_distances['front'], distance_mm)
                    else:  # Back
                        min_distances['back'] = min(min_distances['back'], distance_mm)
                elif 150 <= angle <= 200 or (angle<=30 or angle>=359): #left or right
                    if 150 < angle < 200:  # Left
                        min_distances['left'] = min(min_distances['left'], distance_mm)
                    else:  # Right
                        min_distances['right'] = min(min_distances['right'], distance_mm)
            if min_distances['front']<=800:
                if min_distances['left']>min_distances['right']:
                    ser.write(str.encode('r'))
                    TURNING = True
                    print("turning right")
                    time.sleep(1)
                    ser.write(str.encode('c'))
                    TURNING = False
                    TWIST+=1
                else:
                    ser.write(str.encode('l'))
                    TURNING = True
                    print("turning left")
                    time.sleep(1)
                    ser.write(str.encode('c'))
                    TURNING = False
                    TWIST+=1


            # Display the minimum distances in each direction
            for direction, min_distance in min_distances.items():
                if min_distance != float('inf'):
                    print(f"Minimum distance in {direction} direction (milimeters):", min_distance)

            time.sleep(DELAY)  # Introduce a delay
            if TWIST==12:
                time.sleep(1)
                ser.write(str.encode('s'))
                break
    except KeyboardInterrupt:
        pass  # Allow Ctrl+C to stop the program gracefully
    except ValueError:
        lidar.clean_input()
        ser.write(str.encode('s')) 
        print("valueerror")
        lidar.clean_input()
        run()
    except rplidar.RPLidarException:
        lidar.clean_input()
        ser.write(str.encode('s'))
        print("RPLidarException")
        lidar.clean_input()
        run()

    lidar.stop_motor()    
    lidar.stop()
    lidar.disconnect()
    ser.write(str.encode('s'))

if __name__ == '__main__':
    run()
