def solution(s):
        return ''.join(' ' + i if i.isupper() else i.strip() for i in s).strip()
