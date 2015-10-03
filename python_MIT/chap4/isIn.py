# coding: utf-8

def isIn(str1, str2):
    if (str1 in str2 or str2 in str1):
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = 'iwakuma'
    str2 = 'kuma'
    if (isIn(str1, str2)):
        print 'one includes another.'
    else:
        print 'one does NOT include another.'
