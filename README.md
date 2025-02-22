# MJPEGWriter
OpenCV Video HTTP Streaming via MJPEG.
Based on the code found in 
[StackExchange -  CodeReview](http://codereview.stackexchange.com/questions/124321/multithreaded-mjpg-network-stream-server/156915#156915) and [Answers - OpenCV](http://answers.opencv.org/question/6976/display-iplimage-in-webbrowsers/)

## Example main server

```C++
int main()
{
    MJPEGWriter test(7777); //Creates the MJPEGWriter class to stream on the given port
    VideoCapture cap;
    bool ok = cap.open(0); //Opens webcam
    if (!ok)
    {
        printf("no cam found ;(.\n");
        pthread_exit(NULL);
    }
    Mat frame;
    cap >> frame;
    test.write(frame); //Writes a frame (Mat class from OpenCV) to the server
    frame.release();
    test.start(); //Starts the HTTP Server on the selected port
    while(cap.isOpened()){
        cap >> frame; 
        test.write(frame); 
        frame.release();
    }
    test.stop(); //Stops the HTTP Server
    exit(0);
}
```
Note: you have to write an image to the MJPEGWriter class before start the server.

## Python client
```Python
import cv2

cap = cv2.VideoCapture("http://localhost:7777")
if not(cap.isOpened()):
    print("Failed to open MJPEG streaming")

ret, frame = cap.read()
 
while(True):
    ret, frame = cap.read()
    cv2.imshow("MJPEG Reader", frame)
    cv2.waitKey(1)

```

## Compiling
Compile with C++11, OpenCV libraries and pthread:

### CMake

```sh
mkdir build
cd build
cmake ..
make
```

## g++

```sh
# For OpenCV4
g++ MJPEGWriter.cpp main.cpp -o MJPEG -lpthread -lopencv_highgui -lopencv_core `pkg-config --libs opencv4 --cflags opencv4`  
```

## Roadmap
You can follow the development and request new features at https://trello.com/b/OZVtAu05
