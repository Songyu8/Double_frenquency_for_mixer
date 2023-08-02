% a=sign(dbm+87.5)
% tri=delaunay(x1,y1);
% figure(233)
% trisurf(tri,x1,y1,dbm)
% shading interp
% 
% <<FILENAME.PNG>>
% 
% hold on
% colorbar
% view(3);grid on;colorbar

x=datatest1(:,1)/1000000;y=datatest1(:,2)/1000000;z=datatest1(:,3);
[X,Y,Z]=griddata(x,y,z,linspace(min(x),max(x))',linspace(min(y),max(y)),'cubic');%插值
% figure,contourf(X,Y,Z) %等高线图
% colorbar
% figure,surfc(X,Y,Z)%三维曲面
z1=sign(z+85.5)
figure,scatter(x,y,5,z1)%散点图
colorbar
