# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

from collections import Counter
import time


# Complete the isValid function below.
def isValid_sun_1(s):
    freq = Counter(s).values()
    freq_removed_dup = list(set(freq))
    freq_cnt = Counter(freq)
    if len(freq_removed_dup) == 1:
        return 'YES'
    if len(freq_cnt) == 2:
        if freq_cnt[1] == 1 or 1 in set(freq_cnt) and abs(list(set(freq))[0] - list(set(freq))[1]) == 1:
            return 'YES'
    return 'NO'


def isValid_ans(string):
    string = Counter(Counter(string).values())
    # print(string)
    if len(string.keys()) == 1:
        print("YES")

    elif len(string.values()) == 2:
        key1, key2 = string.keys()
        if string[key1] == 1 and (key1 - 1 == key2 or key1 - 1 == 0):
            print("YES")
        elif string[key2] == 1 and (key2 - 1 == key1 or key2 - 1 == 0):
            print("YES")
        else:
            print("NO")

    else:
        print("NO")


def isValid_ho(s):
    freq = {}
    cnt = set()
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for num in freq.values():
        cnt.add(num)

    if len(cnt) == 1:
        return 'YES'

    elif len(cnt) > 2:
        return 'NO'

    else:
        for key in freq:
            freq[key] -= 1
            temp = list(freq.values())
            try:
                temp.remove(0)
            except:
                pass
            if len(set(temp)) == 1:
                return 'YES'
            else:
                freq[key] += 1
    return 'NO'


if __name__ == '__main__':
    s = input()
    start_time = time.time()
    isValid_ans(s)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    isValid_sun_1(s)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    isValid_ho(s)
    print("--- %s seconds ---" % (time.time() - start_time))

# https://hr-testcases-us-east-1.s3.amazonaws.com/8816/input13.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1618547009&Signature=2bnRZDGAFefVszdbJzgQEuX%2FTAU%3D&response-content-type=text%2Fplain
