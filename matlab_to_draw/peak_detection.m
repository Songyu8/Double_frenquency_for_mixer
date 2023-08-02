xx=linspace(min(x11),max(x11));
yy=spline(x11,y11,xx);
plot(xx,yy,'r',x11,y11,'o')
 hold on
xx=linspace(min(x22),max(x22));
yy=spline(x22,y22,xx);
plot(xx,yy,'g',x22,y22,'o')
 hold on
 xx=linspace(min(x33),max(x33));
yy=spline(x33,y33,xx);
plot(xx,yy,'b',x33,y33,'o')
 hold on