# WP_EDGE_AI
ANN in STMs:
We use the MCDCNN, iter 0, as example network. First it is converted from .hdf5 to .tflite (mcdcnnBest.tflite).

To run AI on STMs the sofware package X-Cube-AI need to be installed (https://wiki.stmicroelectronics.cn/stm32mcu/wiki/AI:X-CUBE-AI_documentation).

MCDCNN:
- Input: 
  - data preprocessed by a z-score normalisation
  - Test and train data available
- Output:
  - Array of five probabilities [no stimulus, wind, temperature, blue light, red light] = [class 0, class 1,class 2, class 3, class 4]

