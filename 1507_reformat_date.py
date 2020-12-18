class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        splitted = date.split(' ')
        day = splitted[0][:-2]
        month = str(months.index(splitted[1]) + 1)
        year = splitted[2]
        month = month if len(month) == 2 else '0' + month
        day = day if len(day) == 2 else '0' + day
        return year + '-' + month + '-' + day