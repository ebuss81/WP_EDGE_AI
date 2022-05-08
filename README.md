# WP_EDGE_AI
ANN in STMs:
We use the MCDCNN, iter 0, as example network. First it is converted from .hdf5 to .tflite (mcdcnnBest.tflite).

To run AI on STMs the sofware package X-Cube-AI need to be installed (https://wiki.stmicroelectronics.cn/stm32mcu/wiki/AI:X-CUBE-AI_documentation , https://www.digikey.de/en/videos/d/digi-key-electronics/tinyml-getting-started-with-stm32-x-cube-ai-digi-key-electronics).

MCDCNN:

- Input: 
  - Data preprocessed by a z-score normalization.
  - Raw test and train data available, code for nomalization too.
  
- Output:
  - Array of five probabilities [no stimulus, wind, temperature, blue light, red light] = [class 0, class 1,class 2, class 3, class 4]

STM:
-00_AI_BLE.zip in STM includes the implementation.

-IMPORTANT: Do not generate codea via CubeMX otherwise important c-code will be deleted. If you need to run Cube-MX, let me know. I will point you to the deleted code.

-The important code for you is in main.c
  1) Example data of each class are available in line 62 - 71
  2) The input array of the ANN is build in the for loop at line 202
  3) The network classifies at line 207
  4) A comparison of the probabilites is done at line 216
  5) If a connection is established, a notification of 1 byte with the class number is send to the peer
  
The code was tested with the mobile app LightBlue

You will probably need some of the following UUIDs to get access to the send data.

#define COPY_AI_SERVICE_UUID(uuid_struct)            COPY_UUID_128(uuid_struct,0x5a,0x3b,0x00,0x00,0xf6,0xdd,0x4c,0x45,0xb3,0x1f,0xe8,0x9c,0x05,0xae,0x33,0x90)

#define COPY_AI_CHARAC_UUID(uuid_struct)             COPY_UUID_128(uuid_struct,0x5a,0x3b,0x01,0x00,0xf6,0xdd,0x4c,0x45,0xb3,0x1f,0xe8,0x9c,0x05,0xae,0x33,0x90)

#define COPY_AI_NOTIFY_UUID(uuid_struct)             COPY_UUID_128(uuid_struct,0x5a,0x3b,0x02,0x03,0xf6,0xdd,0x4c,0x45,0xb3,0x1f,0xe8,0x9c,0x05,0xae,0x33,0x90)


