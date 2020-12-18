# class Solution(object):
#     def reformatDate(self, date):
#         """
#         :type date: str
#         :rtype: str
#         """
#         months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#         splitted = date.split(' ')
#         day = splitted[0][:-2]
#         month = str(months.index(splitted[1]) + 1)
#         year = splitted[2]
#         month = month if len(month) == 2 else '0' + month
#         day = day if len(day) == 2 else '0' + day
#         return year + '-' + month + '-' + day

class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        months = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12", }

        splitted = date.split(' ')
        return '{}-{}-{:0>2}'.format(splitted[2], months[splitted[1]], splitted[0][:-2])