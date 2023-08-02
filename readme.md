#  Double_frenquency_for_mixer

**A Basic .py  document to Control your instruments with Python.**

## Requirements
only in windows

- [python 3](https://www.python.org/downloads/)
- [pytorch 1.0 + torchvision](https://pytorch.org/)
- [pyvisa] （https://pyvisa.readthedocs.io/en/latest/）

## Install all dependences libraries like PyVISA
```bash
pip3 install pyvisa
```

##File and Folder Structure
```
├──  matlab_to_draw  -   here's .m and sample for how to draw double frenquency test and  peak detection 
│    └── double_frenquency.m 	-
│    └── peak_detection.m
│ 
│
├──  sweep_frenquency .py   -   here's is the .py can sweep double frenquency.for easily contraling,here is no bash code. 
│ 
│
├──  test _connect_device.py   -   here's is the .py can test connect the divice or not 
```

## Comments in Chinese 

这个repo中上传了使用计算机远程自动控制仪器进行双频测试的相关代码和内容。首先请使用test _connect_device.py文件测试设备是否连接成功，接着使用sweep_frenquency .py进行扫频测试，测试的结果会自动保存（注意！请阅读代码和注释设置保存路径）。使用matlab_to_draw的文件进行绘图


