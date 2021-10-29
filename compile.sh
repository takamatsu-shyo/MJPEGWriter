g++ MJPEGWriter.cpp main.cpp -v -o MJPEG -lpthread -lopencv_highgui -lopencv_core `pkg-config --libs opencv4 --cflags opencv4`  
