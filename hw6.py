from math import gcd
from math import pow
from math import sqrt
import time
from guppy import hpy
import csv


# String Modifier
def string_mdf(s):
    beg = s.find("Total size = ")
    end = s.find(" bytes.")
    s = s[beg:end]
    s = s.replace('Total size = ', '')

    return s


# Trial division
def trial_division(n):
    if n == 2:
        return n
    if n < 2 or n % 2 == 0:
        return 2

    i = 3
    while i <= int(sqrt(n) + 1):
        if n % i == 0:
            return i
        i += 2

    return n


# Pollard's Rho
def pollards_rho(n):
    x = 2
    y = 2
    d = 1
    g = lambda x: ((pow(x, 2) + 1) % n)

    while d == 1:
        x = int(g(x))
        # print(str(x))
        y = int(g(g(y)))
        # print(str(y))
        d = gcd(abs(x-y), n)
        # print(str(d))

    return d


def test(n):
    p = trial_division(n)
    return n,p,(n/p)


#  Stress Testing
def stress_test():
    n = 144483604528043653279487

    h = hpy()
    start_time = time.time()

    p = trial_division(n)

    print(str(n) + " = " + str(p) + " * " + str(n/p))
    print("Time = " + str(time.time() - start_time))
    size = str(h.heap())
    print("Size = " + string_mdf(size))
    return


# main function
def main():
    numbers = list()
    # 3 digit
    numbers.append(221)  # 13x17
    numbers.append(323)  # 17x19
    numbers.append(437)  # 19x23
    numbers.append(667)  # 23x29
    numbers.append(713)  # 23x31

    # 4 digit
    numbers.append(1271) #41x31
    numbers.append(1927) #41x47
    numbers.append(2491) #53x47
    numbers.append(3127) #53x59
    numbers.append(3599) #59x61

    # 5 digit
    numbers.append(16637) #127x131
    numbers.append(18209) #131x139
    numbers.append(20711) #139x149
    numbers.append(25777) #149x173
    numbers.append(33043) #173x191

    # 6 digit
    numbers.append(777899)  # 877x887
    numbers.append(808057)  # 887x911
    numbers.append(846319)  # 911x929
    numbers.append(862717)  # 911x947
    numbers.append(925363)  # 953x971

    # 7 digit
    numbers.append(1022117)  # 1009x1013
    numbers.append(1143677)  # 1013x1129
    numbers.append(1340123)  # 1129x1187
    numbers.append(1444579)  # 1217x1187
    numbers.append(1568713)  # 1217x1289

    #8 digit
    numbers.append(30272003)  # 5501x5503
    numbers.append(30371057)  # 5503x5519
    numbers.append(35604893)  # 5953x5981
    numbers.append(86099837)  # 9277x9281
    numbers.append(96314587)  # 9811x9817

    #9 digit
    numbers.append(851624989)  # 29033x29333
    numbers.append(860600887)  # 29333x29339
    numbers.append(861011633)  # 29339x29347
    numbers.append(863124617)  # 29411x29347
    numbers.append(865536319)  # 29411x29429

    #10 digit
    numbers.append(2694648091)  # 51907x51913
    numbers.append(2695790177)  # 51929x51913
    numbers.append(2698802059)  # 29339x29347
    numbers.append(2706496567)  # 52021x52027
    numbers.append(2710451819)  # 52057x52067

    #11 digit
    numbers.append(10010602793)  # 100049x100057
    numbers.append(10012603933)  # 100069x100057
    numbers.append(10081565633)  # 100403x100411
    numbers.append(14572594073)  # 120721x120713
    numbers.append(17562875621)  # 132523x132527

    #12 digit
    numbers.append(250272073759)  # 500257x500287
    numbers.append(250674454267)  # 50671x50677
    numbers.append(271816249599)  # 521359x521361
    numbers.append(283914202727)  # 532823x532849
    numbers.append(253558574107)  # 503543x503549


    with open("result3.csv", mode='w') as data_file:
        wr = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for num in numbers:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            h = hpy()
            start_time = time.time()
            n, p1, p2 = test(num)
            tm = round(time.time() - start_time, 5)
            tm = tm * 1000
            print(tm)
            size = str(h.heap())
            size = string_mdf(size)
            wr.writerow([str(n), float(p1), float(p2), tm, size])


main()
