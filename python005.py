filename = open('C:/pydata/tmpprecip2012.dat')
raincount = 0
raintotal = 0

for line in filename:
    try:
        rain = float(line[11:16])
    except ValueError:
        print '%r = Bad Data' % (line)
        continue
    if rain > 0:
        raincount += 1
        raintotal += rain
print 'Rain days -', raincount
print 'Rain amount -', raintotal



"""def column_read():
    for line in filename:
        try:
            rain = float(line[11:16])
        except ValueError:
                print rain
                continue
    for line in filename:
        try:
            percipitation = float(line[12:16])
        except ValueError:
            print percipitation
            continue

print column_read()

"""

"""columns = line.split(separator)
        if len(columns) >= 2:
            print columns[1]
        return column_read"""

#return column_read

"""
open file
get data
counter for days with rainfall
counter for percipitation for the year
slice percipitation and convert to float
rain=(line[12:16])
"""
