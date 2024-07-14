Engineering materials
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2024.

## Content

* `t-photos` contains 2 photos of the team (an official one and one funny photo with all team members)
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `video` contains the video.md file with the link to a video where driving demonstration exists
* `schemes` contains one or several schematic diagrams in form of JPEG, PNG or PDF of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `src` contains code of control software for all components which were programmed to participate in the competition
* `models` is for the files for models used by 3D printers, laser cutting machines and CNC machines to produce the vehicle elements. If there is nothing to add to this location, the directory can be removed.
* `other` is for other files which can be used to understand how to prepare the vehicle for the competition. It may include documentation how to connect to a SBC/SBM and upload files there, datasets, hardware specifications, communication protocols descriptions etc. If there is nothing to add to this location, the directory can be removed.

## Introduction

_This part must be filled by participants with the technical clarifications about the code: which modules the code consists of, how they are related to the electromechanical components of the vehicle, and what is the process to build/compile/upload the code to the vehicle’s controllers._

## April

This is the month were we start to work because our school's robotics club started. In this month we prioritized on learning the new rules of this years competition so we may do any necessary adjustments to our robot from last year. We started testing the robot to make sure that all of it's components were working properly and we also started to try to find ways to connect the camera to the LiDAR sensor so that the LiDAR doesn't detect the blocks as walls and goes through them properly.

## May

In this month we decided to use our code from last year as a base for this years code, this code used mainly Python to program the LiDAR, although this did make programming with the LiDAR more difficult as there aren't that many libraries for LiDAR in Python and, although there were a lot of libraries for ROS we decided to stay away from ROS because last year we had a lot of errors with ROS.

## June and July

This month we spent primarily focused on making the LiDAR work properly, but that didn't go very well, at first the robot crashed into the wall and we thought that was because the LiDAR was too high up, but when we fixed that the LiDAR still didn't see the walls, so it was an issue with the code. After checking the code we spent multiple days trying to fix it but for every error we fixed 2 more showed up. Eventually we realized that the LiDAR was reading the distances in reverse, so the farther away an object was the closer the LiDAR said it was. But in better news we were able make the camera detect colors correctly, as it turns out the reason it didn't read colors correctly last year was because of illumination so we added a light source to the robot so it could see colors properly.
