import pyvisa as visa
import time
import xlwt

##注意,以下操作均在windows平台操作,故而并没有添加bash指令.
rm=visa.ResourceManager()
t=rm.list_resources()
DG4182=rm.open_resource('USB0::0x1AB1::0x0641::DG4C145000820::INSTR')
N90000B=rm.open_resource('TCPIP0::K-N90X0A-000005.local::inst0::INSTR')
DG4182.query('*IDN?')
N90000B.query('*IDN?')
print(DG4182.query('*IDN?'))
print(N90000B.query('*IDN?'))#此前代码意义可查看test _connect_device.py中的注释



freq_star1=4000000#设置扫频信号1起始频率4000000hz

freq_end1=6000000#设置扫频信号1终止频率6000000hz

freq_star2=4000000#设置扫频信号2起始频率4000000hz

freq_end2=6000000#设置扫频信号2起始频率6000000hz

step=10000#步进数

DG4182.write(':OUTPut1 ON ')#设置信号源输出口1开启

DG4182.write(':OUTPut2 ON ')#设置信号源输出口2开启

DG4182.write(':SYSTem:KLOCk OFF')#设置信号源解锁可线下操作


book = xlwt.Workbook(encoding='utf-8', style_compression=0)#设置存储数据格式

# 在excel中创建一个sheet表单,名字为test,可重设值
sheet = book.add_sheet('test', cell_overwrite_ok=True)

# 自定义列名
col = ('x轴', 'y轴', 'dbm')

# 将列属性元组col写进sheet表单中
for i in range(0, 3):
    sheet.write(0, i, col[i])  # 第一个参数是行，第二个参数是列
n=1
while freq_star1<=freq_end1:
    DG4182.write(':APPLy:SINusoid %d,2.5' % freq_star1)#输出信号,电压为2.5v
    print(freq_star1)
    while freq_star2<=freq_end2:
        DG4182.write('SOURce2:APPLy:SINusoid %d,2.5' % freq_star2)
        print(freq_star2)
        sheet.write(n, 0, freq_star1)
        sheet.write(n, 1, freq_star2)
        freq_star2=freq_star2+step
        print(N90000B.query(':CALC:MARK1:Y?'))
        time.sleep(0.02)#加入间隔时间,防止读写太快无法反应

        sheet.write(n,2, N90000B.query(':CALC:MARK1:Y?'))
        n=n+1

    freq_star1=freq_star1+step
    freq_star2=4000000


# 保存excel文件
savepath = 'D:/test1/datatest.xls'
book.save(savepath)
