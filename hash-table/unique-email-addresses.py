class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()

        for email in emails:
            localName, domainName = email.split("@")
            # remove '.'
            localName = localName.replace(".", "")
            # clean "+"
            plusIdx = localName.split("+")
            if len(plusIdx) > 0:
                localName = plusIdx[0]

            emailSet.add(f"{localName}@{domainName}")

        return len(emailSet)