total = float(input("Enter the amount of hours: "))
hours= total//1.0
totalTimeAfterHours = float((total % hours)*60)
minutes = totalTimeAfterHours//1.0
seconds = float((totalTimeAfterHours % minutes) * 60)

print ("%.0f hours, %.0f minutes and %.0f seconds." % (hours,minutes, seconds))

# print ("%f hours is: " % ())
# print ("%d hours, %d minutes and %d seconds. " % ())

#Before decimal is hours
#After decimal multiply by 60. That before decimal is minutes
#After that multiply by 60 and before deciaml is minutes
