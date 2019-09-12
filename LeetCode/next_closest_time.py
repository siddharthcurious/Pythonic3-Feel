class Solution:
    def nextClosestTime(self, time: str) -> str:

        t = time.split(":")
        hours = int(t[0])
        minutes = int(t[1])

        tminutes = hours * 60 + minutes

        digits = set(time)
        # print(digits)

        c = 0
        while(True):

            tminutes += 1

            minutes = tminutes % 60
            hours = tminutes // 60

            if hours >= 24:
                hours -= 24

            hrs = str(hours)
            mint = str(minutes)
            if hours <= 9:
                hrs = "0"+str(hours)
            if minutes <= 9:
                mint = "0"+str(minutes)




            new_time = "{}:{}".format(hrs, mint)
            new_digits = set(new_time)

            if new_digits.issubset(digits):
                return new_time


if __name__ == "__main__":

    obj = Solution()
    time = "19:34"
    time = "23:59"
    r = obj.nextClosestTime(time)
    print(r)
