n = 0

A_room = 9
A1 = [3,[[],[],[]]]
A2 = [4,[[],[],[],[]]]
A3 = [2,[[],[]]]


B_room = 9
B1 = [3,[[],[],[]]]
B2 = [4,[[],[],[],[]]]
B3 = [2,[[],[]]]


C_room = 9
C1 = [3,[[],[],[]]]
C2 = [4,[[],[],[],[]]]
C3 = [2,[[],[]]]


f= False
while n < 2512: #3 x 3 x (3+4+2) x 31 + 1
    A_class = {'A1':[A1],'A2':[A2],'A3':[A3]}
    B_class = {'B1':[B1],'B2':[B2],'B3':[B3]}
    C_class = {'C1':[C1],'C2':[C2],'C3':[C3]}
    print('A room:',A_class)
    print('B room:',B_class)
    print('C room:',C_class)
    class_type = input('Please enter the type of room: [A,B,C]=')
    bed_number = int(input('How many bed: [1,2,3]?'))
    if class_type=='A':
        if A_room > 0:
            if bed_number==1:
                if A1[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in A1[1][0]:
                                A1[1][0].append(date+day)
                                if len(A1[1][0])>30:
                                    A1[0] -= 1
                                    A_room -= 1
                            elif day+date not in A1[1][1]:
                                A1[1][1].append(date+day)
                                if len(A1[1][1])>30:
                                    A1[0] -= 1
                                    A_room -= 1
                            elif day+date not in A1[1][2]:
                                A1[1][2].append(date+day)
                                if len(A1[1][2])>30:
                                    A1[0] -= 1
                                    A_room -= 1
                            else:
                                print('day',date+day,'is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')


                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue

            elif bed_number==2:
                if A2[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in A2[1][0]:
                                A2[1][0].append(date+day)
                                if len(A2[1][0])>30:
                                    A2[0] -= 1
                                    A_room -= 1
                            elif day+date not in A2[1][1]:
                                A2[1][1].append(date+day)
                                if len(A2[1][1])>30:
                                    A2[0] -= 1
                                    A_room -= 1
                            elif day+date not in A2[1][2]:
                                A2[1][2].append(date+day)
                                if len(A2[1][2])>30:
                                    A2[0] -= 1
                                    A_room -= 1
                            elif day+date not in A2[1][3]:
                                A2[1][3].append(date+day)
                                if len(A2[1][3])>30:
                                    A2[0] -= 1
                                    A_room -= 1
                            else:
                                print('day',date+day,'is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')
                            

                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue
            
            elif bed_number==3:
                if A3[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in A3[1][0]:
                                A3[1][0].append(date+day)
                                if len(A3[1][0])>30:
                                    A3[0] -= 1
                                    A_room -= 1
                            elif day+date not in A3[1][1]:
                                A3[1][1].append(date+day)
                                if len(A3[1][1])>30:
                                    A3[0] -= 1
                                    A_room -= 1
                            else:
                                print(date+day,'th day is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')

                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue
            else:
                print('You chose a wrong number of beds, try again')
                continue

        else:
            print(class_type,'rooms are full, try for another type')
            continue

    

    elif class_type=='B':
        if B_room > 0:
            if bed_number==1:
                if B1[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in B1[1][0]:
                                B1[1][0].append(date+day)
                                if len(B1[1][0])>30:
                                    B1[0] -= 1
                                    B_room -= 1
                            elif day+date not in B1[1][1]:
                                B1[1][1].append(date+day)
                                if len(B1[1][1])>30:
                                    B1[0] -= 1
                                    B_room -= 1
                            elif day+date not in B1[1][2]:
                                B1[1][2].append(date+day)
                                if len(B1[1][2])>30:
                                    B1[0] -= 1
                                    B_room -= 1
                            else:
                                print('day',date+day,'is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')


                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue

            elif bed_number==2:
                if B2[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in B2[1][0]:
                                B2[1][0].append(date+day)
                                if len(B2[1][0])>30:
                                    B2[0] -= 1
                                    B_room -= 1
                            elif day+date not in B2[1][1]:
                                B2[1][1].append(date+day)
                                if len(B2[1][1])>30:
                                    B2[0] -= 1
                                    B_room -= 1
                            elif day+date not in B2[1][2]:
                                B2[1][2].append(date+day)
                                if len(B2[1][2])>30:
                                    B2[0] -= 1
                                    B_room -= 1
                            elif day+date not in B2[1][3]:
                                B2[1][3].append(date+day)
                                if len(B2[1][3])>30:
                                    B2[0] -= 1
                                    B_room -= 1
                            else:
                                print('day',date+day,'is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')
                            

                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue
            
            elif bed_number==3:
                if B3[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in B3[1][0]:
                                B3[1][0].append(date+day)
                                if len(B3[1][0])>30:
                                    B3[0] -= 1
                                    B_room -= 1
                            elif day+date not in B3[1][1]:
                                B3[1][1].append(date+day)
                                if len(B3[1][1])>30:
                                    B3[0] -= 1
                                    B_room -= 1
                            else:
                                print(date+day,'th day is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')

                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue
            else:
                print('You chose a wrong number of beds, try again')
                continue

        else:
            print(class_type,'rooms are full, try for another type')
            continue

    elif class_type=='C':
        if C_room > 0:
            if bed_number==1:
                if C1[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in C1[1][0]:
                                C1[1][0].append(date+day)
                                if len(C1[1][0])>30:
                                    C1[0] -= 1
                                    C_room -= 1
                            elif day+date not in C1[1][1]:
                                C1[1][1].append(date+day)
                                if len(C1[1][1])>30:
                                    C1[0] -= 1
                                    C_room -= 1
                            elif day+date not in C1[1][2]:
                                C1[1][2].append(date+day)
                                if len(C1[1][2])>30:
                                    C1[0] -= 1
                                    C_room -= 1
                            else:
                                print('day',date+day,'is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')


                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue

            elif bed_number==2:
                if C2[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in C2[1][0]:
                                C2[1][0].append(date+day)
                                if len(C2[1][0])>30:
                                    C2[0] -= 1
                                    C_room -= 1
                            elif day+date not in C2[1][1]:
                                C2[1][1].append(date+day)
                                if len(C2[1][1])>30:
                                    C2[0] -= 1
                                    C_room -= 1
                            elif day+date not in C2[1][2]:
                                C2[1][2].append(date+day)
                                if len(C2[1][2])>30:
                                    C2[0] -= 1
                                    C_room -= 1
                            elif day+date not in C2[1][3]:
                                C2[1][3].append(date+day)
                                if len(C2[1][3])>30:
                                    C2[0] -= 1
                                    C_room -= 1
                            else:
                                print('day',date+day,'is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')
                            

                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue
            
            elif bed_number==3:
                if C3[0] > 0:
                    date = int(input('When will you come: [1-30]?'))
                    days = int(input('How long will you stay: [1-30]?'))
                    if (date+days-1)>31:
                        print('day out of range, try again')
                    else:
                        f = True
                        for day in range(days):
                            if day+date not in C3[1][0]:
                                C3[1][0].append(date+day)
                                if len(C3[1][0])>30:
                                    C3[0] -= 1
                                    C_room -= 1
                            elif day+date not in C3[1][1]:
                                C3[1][1].append(date+day)
                                if len(C3[1][1])>30:
                                    C3[0] -= 1
                                    C_room -= 1
                            else:
                                print(date+day,'th day is not empty, try for other days')
                                f = False
                                break
                        if f:
                            n -= days
                            print(f"{class_type} room for {bed_number} bed been booked on {date} till {date+days-1}")
                            print('=========================================')

                else:
                    print(f'{class_type} room for {bed_number} bed is not empty, try again')
                    continue
            else:
                print('You chose a wrong number of beds, try again')
                continue

        else:
            print(class_type,'rooms are full, try for another type')
            continue

    