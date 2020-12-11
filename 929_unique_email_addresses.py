class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[0:local.index('+')]
            local = local.replace('.', '') + '@' + domain
            unique_emails.add(local)
        return len(unique_emails)