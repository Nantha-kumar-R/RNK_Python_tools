filename = input("Enter the stlfilename:")
stl = open(filename,'r')
Tot_area,tri_area,vol,pts = 0.0,0.0,0.0,[]
for line in stl:
    if 'normal' in line or 'vertex' in line:
        pts.append([float(x) for x in line.split() [-3:]])
        if(len(pts) == 4):
            tri_area = ((((((pts[1][1] - pts[2][1])*(pts[1][2] - pts[3][2])) - ((pts[1][1] - pts[3][1])*(pts[1][2] - pts[2][2])))**2)+((((pts[1][0] - pts[3][0])*(pts[1][2] - pts[2][2])) - ((pts[1][0] - pts[2][0])*(pts[1][2] - pts[3][2])))**2)+((((pts[1][0] - pts[2][0])*(pts[1][1] - pts[3][1])) - ((pts[1][0] - pts[3][0])*(pts[1][1] - pts[2][1])))**2))**0.5)*0.5
            vol = vol +(((((pts[1][0]+pts[2][0]+pts[3][0])/3.0)*pts[0][0])+(((pts[1][1]+pts[2][1]+pts[3][1])/3.0)*pts[0][1])+(((pts[1][2]+pts[2][2]+pts[3][2])/3.0)*pts[0][2])) * tri_area /3.0)
            Tot_area = Tot_area + tri_area
            pts.clear()
print('Surface area: ', Tot_area,'\nVolume: ',vol)


            
