import time


class CalculateTime:
    def __init__(self, differenceintime):
        self.getdifferencetime = differenceintime

    # Converting the floating seconds data into structured time
    def getStructuredTime(self):
        convert_seconds_to_readable_value = time.gmtime(self.getdifferencetime)
        covert_to_struct_time = time.struct_time(convert_seconds_to_readable_value)

        return convert_seconds_to_readable_value

    def SeperateSeconds(self):
        StructuredTime = self.getStructuredTime()
        seconds = StructuredTime.tm_sec
        return seconds

    def SeperateMinutes(self):
        StructureTime = self.getStructuredTime()
        minutes = StructureTime.tm_min
        return minutes

    def SeperateHours(self):
        StructuredTime = self.getStructuredTime()
        hours = StructuredTime.tm_hour
        return hours

    def convertEverythingIntoSeconds(self):
        Seconds = self.SeperateSeconds()
        Minutes = self.SeperateMinutes()
        Hours = self.SeperateHours()

        allInSeconds = ((Hours * 60 * 60) + (Minutes * 60) + Seconds)
        return allInSeconds


if __name__ == '__main__':
    obj = CalculateTime(differenceintime=time.time())
    print(obj.SeperateSeconds())
    print(obj.SeperateHours())
    print(obj.SeperateMinutes())
