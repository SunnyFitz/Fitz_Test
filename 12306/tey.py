import time
num = 0
def main():
    global num
    try:
        time.sleep(1)
        print("\n\n########## TEST SCRIPT ATTEMPT: {} ##########".format(num))
        num += 1
        if num >10:
            print('done')
            return(1)
        if num >3:
            int('ac')

        main()
    except:
        num += 2
        main()



print(main())
