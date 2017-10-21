# Real-Time-Object-Tracker
This is a real-time object recognition project developed using Python Programming Language 

## How it works
* First, it starts off the webcam for video capture
* Now we extract frame by frame fro the image and do analysis on it
* (Note we are analyzing frames in grayscale)
* Now we have a loaded trainee image that will be used to track
* Since we got the tracking image now we will compare it with each frame we will get from the video
* As the pixels of tracking photo matches with certain pixels on the frame, we will draw a rectangle over there at ROI (Region of Interest)
* Hence as soon as we got a frame and object is recognized there will be a new rectangle formed.

## For your Image
* Add your own image into the images folder
* And give reference of it into the python code

## Two Methods
* There are two methods of object tracking into it .
* Both have their own accuracy and procedure
