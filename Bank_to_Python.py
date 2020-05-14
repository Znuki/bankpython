from BankData.Data import *

BankData = []  # 데이터 리스트 만들어주기

class LikelionBank(Data):
    def __init__(self):
        pass # 실행할 거 없을 때

    def CreateAcc(self):
        print("<   계좌 생성   >")      ##
        AccNumber = input("<   생성할 계좌를 입력하세요 :  >")
        for Data in BankData:       ##
            if AccNumber == Data.AccNumber:     ##
                print("<   같은 계좌가 존재합니다.   >")
                return 0
            if AccNumber < 0:
                print("<   잘못된 입력입니다.   >")
                return 0
        self.AccNumber = AccNumber
        self.name = input("<   계좌 이름을 입력하세요.  :   >   "   )
        self.Account = int(input("<   얼마나 입금할까요?  :  >  "))
        BankData.append(LL)
        print("<   계좌가 생성되었습니다.   >")


    def deposit(self):
        print("<   입금 하기   >")
        # if len(BankData) == 0: ##
        #     print("<   계좌가 없습니다.   >")
        #     return 0
        Acc_Data = input("<   계좌 번호를 입력하세요.   >")
        for Data in BankData:
            if Acc_Data == Data.AccNumber:
                print("<   계좌 이름 :   >", Data.name)
                print("<   계좌 번호 :   >", Data.Account)
                deposit_Amount = int(input("<   입금하려는 금액을 입력하세요.   >"))
                if deposit_Amount < 0:
                    print("<   잘못된 입력입니다.   >")
                elif deposit_Amount > 0:
                    Data.Account += deposit_Amount
                    print("<계좌 금액 : ", Data.Account, "원>")
                    print("<   계좌 입금 완료.   >")
                return 0
            # else:
            #     if(Data == BankData[0]):       ##
            #         print("<   좆된 입력입니다.   >")
            #         break


    def withdraw(self):
        print("<    출금 하기   >")
        # if len(BankData) == 0: ##
        #     print("<   계좌가 없습니다.   >")
        #     return 0
        Acc_Data = input("<   계좌 번호를 입력하세요.   >")
        for Data in BankData:
            if Acc_Data == Data.AccNumber:
                print("<   계좌 이름 :   >", Data.name)
                print("<   계좌 번호 :   >", Data.Account)
                withdraw_Amount = int(input("<   출금하려는 금액을 입력하세요.   >"))
                if withdraw_Amount < 0:
                    print("<   잘못된 입력입니다.   >")
                elif withdraw_Amount <= Data.Account:
                    Data.Account -= withdraw_Amount
                    print("<계좌 금액 : ", Data.Account, "원>")
                    print("<   계좌 출금 완료.   >")
                else:
                    print("<   잘못된 입력입니다.   >")
                return 0
            # else:
            #     if(Data == BankData[-1]):       ##
            #         print("<   잘못된 입력입니다.   >")
            #         break

    def AccStatus(self):
        # if len(BankData) == 0: ##
        #     print("<   계좌가 없습니다.   >")
        #     return 0
        # else:
            print("<   계좌 확인   >")
            for Data in BankData:
                print("계좌 번호 : ", Data.AccNumber, "\n 이름 : ", Data.name, "\n 금액 : ", Data.Account, " 원")




if __name__ == "__main__":

    LL = LikelionBank()
    
    while True:
        print()
        print("======Likelion Bank======\n"
                "      1. 계좌 생성\n"        
                "      2. 입금 하기\n"       
                "      3. 출금 하기\n"        
                "      4. 계좌 조회\n"       
                "      5. 업무 종료\n"       
             "===========================")

        menu = int(float(input(" 어떤 업무를 보시겠습니까? : ")))

        if menu == 1:
            LL.CreateAcc()

        elif menu == 2:
            LL.deposit()

        elif menu == 3:
            LL.withdraw()

        elif menu == 4:
            LL.AccStatus()

        elif menu == 5:
            print("<   업무를 종료합니다   >")
            break

        else:
            print("<   잘못된 입력입니다   >")