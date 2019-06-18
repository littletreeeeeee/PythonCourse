dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
lengthArray = []
for day in dayOfWeek:
    lengthArray.append(len(day))
print lengthArray

print [len(day) for day in dayOfWeek]
print [day for day in dayOfWeek if len(day) > 6]
print [len(day) for day in dayOfWeek if len(day) < 8]
sun, mon, tue, wed, thr, fri, sat = dayOfWeek
print sun, wed, fri