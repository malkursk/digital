def pr6_task2(): 

    p1 = input ('1 друг ')
    p2 = input ('2 друг ')
    p3 = input ('3 друг ')

    m1 = p1.split()
    m2 = p2.split()
    m3 = p3.split()

    m = [ m1[1]+ ' ' + m1[0], m2[1]+ ' ' + m2[0]+ ' ' , m3[1]+ ' ' + m3[0] ]

    m.sort()

    m1 = m [0].split()
    m2 = m [1].split()
    m3 = m [2].split()

    print(m1[1] + ' ' + m2[1] + ' ' + m3[1])
    # print()

pr6_task2()
