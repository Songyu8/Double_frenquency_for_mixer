import time
import os
import numpy as np
import pandas as pd
import xlwt
import matplotlib.pyplot as plt
import pyvisa as visa


#初步入门知识代码在这里,不是很复杂,工业界经常可见相关的编程代码控制硬件
#  https://blog.csdn.net/weixin_44635546/article/details/123973376?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166341332916782427420872%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166341332916782427420872&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-123973376-null-null.142^v47^pc_rank_34_default_23,201^v3^add_ask&utm_term=pyvisa%E6%8E%A7%E5%88%B6%E4%BF%A1%E5%8F%B7%E6%BA%90&spm=1018.2226.3001.4187

rm=visa.ResourceManager()

t=rm.list_resources()  #这两行代码是必须,使用pyvisa硬件库连接

DG4182=rm.open_resource('USB0::0x1AB1::0x0641::DG4C145000820::INSTR')#这里的地址即连结的硬件的地址,采用usb线连接

N90000B=rm.open_resource('TCPIP0::K-N90X0A-000005.local::inst0::INSTR')#这里的地址即连结的硬件的地址,采用网线连接

#固定代码
DG4182.query('*IDN?')
N90000B.query('*IDN?')
print(DG4182.query('*IDN?'))
print(N90000B.query('*IDN?'))
#用于测试硬件是否连接成功

#测试相关的硬件语言是否成功写入硬件
DG4182.write(':SYSTem:KLOCk OFF')#效果为DG4182解锁操作,可以人工直接线下操作DG4182
N90000B.write(':CALC:MARK1:X 47000000')#效果为N90000B光标操作,讲光标定位到47000000HZ
print(N90000B.query(':CALC:MARK1:Y?'))#查看返回结果是否成功写入硬件