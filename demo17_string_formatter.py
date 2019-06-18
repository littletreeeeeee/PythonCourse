radius = 4.0
area = radius * radius * 3.14159
print 'rad=%f, area=%f\n' % (radius, area)
print 'rad=%.2f, area=%.2f\n' % (radius, area)
print 'rad=%(radius).2f, area=%(area).2f\n' % {'radius': radius, 'area': area}
print 'rad=%(radius).2f, area=%(area).2f\n' % {'area': area, 'radius': radius}
print 'rad={}, area={}\n'.format(radius, area)
print 'rad={:.2f}, area={:.2f}\n'.format(radius, area)
print 'rad={1:.2f}, area={0}\n'.format(area, radius)
print 'rad={r:.2f}, area={a:.2f}\n'.format(r=radius, a=area)
print 'rad={r:.2f}, area={a:.2f},area3={a:.2f},area4={a:.2f}\n'.format(r=radius, a=area)
