from DHT import paramA
paramB = paramA

def settingsMenu(paramA):
    statusA = statusA(paramA)
    ask_A(statusA)
    choiseParam(statusA)
    statusB = statusB(paramB)
    ask_B(statusLCD_b, statusLog_b, statusTerm_b)
    paramA = paramB
    return paramA
def choiseParam(statusA):
    userChoise = str(input("choise: "))
    paramF = paramA
    if userChoise == "1":
        if statusA(statusLCD_a) == 1:
            paramA1 = "1"
        else:
            paramA1 = "0"
        paramF = paramF.add[0](paramA1)

    elif userChoise == "2":
        if statusA(statusLog_a) == 1:
            paramB1 = "1"
        else:
            paramB1 = "0"
        paramF = paramF.add[1](paramB1)

    if userChoise == "3":
        if statusA(statusTerm_a) == 1:
            paramC1 = 1
        else:
            paramC1 = 0
        paramF = paramF.add[2](paramC1)

    elif userChoise == "4":
        statusLCD_b = "ON"
        statusLog_b = "ON"
        statusTerm_b = "ON"
        paramF = [1, 1, 1]

    elif userChoise == "5":
        paramF = DHT11.paramA()
        DHT11.menu(DHT11.paramA)
    else:
        print("Error with choise " + str(userChoise))
    choiseParam()
    paramB = paramF
    statusB = statusB(paramB)
    return paramB
def ask_A(statusLCD_a, statusLog_a, statusTerm_a):
    print("-----Settings-----" + "\n" + "1 - вкл/выкл отображение измерений на LCD экране.     сейчас: " + str(statusLCD_a) + "\n" + "2 - вкл/выкл логирование в csv.              сейчас: " + str(statusLog_a) + "\n" + "3 - вкл/выкл отображение в терминале.          сейчас: " + str(statusTerm_a) + "\n" + "4 - настройки по умолчанию." + "\n" + "5 - Назад" +"\n")
    return
def ask_B(statusLCD_b, statusLog_b, statusTerm_b):
    print("-----Settings-----" + "\n" + "1 - вкл/выкл отображение измерений на LCD экране.     сейчас: " + str(statusLCD_b) + "\n" + "2 - вкл/выкл логирование в csv.              сейчас: " + str(statusLog_b) + "\n" + "3 - вкл/выкл отображение в терминале.          сейчас: " + str(statusTerm_b) + "\n" + "4 - настройки по умолчанию." + "\n" + "5 - Назад" +"\n")
    return
def statusA(paramA):
    if paramA == [1, 1, 1] :
        statusLCD_a = "ON"
        statusLog_a = "ON"
        statusTerm_a = "ON"
    elif paramA == [1, 1, 0] :
        statusLCD_a = "ON"
        statusLog_a = "ON"
        statusTerm_a = "OFF"
    elif paramA == [1, 0, 1] :
        statusLCD_a = "ON"
        statusLog_a = "OFF"
        statusTerm_a = "ON"
    elif paramA == [0, 1, 1] :
        statusLCD_a = "OFF"
        statusLog_a = "ON"
        statusTerm_a = "ON"
    elif paramA == [0, 0, 1] :
        statusLCD_a = "ON"
        statusLog_a = "ON"
        statusTerm_a = "OFF"
    elif paramA == [0, 0, 0] :
        statusLCD_a = "OFF"
        statusLog_a = "OFF"
        statusTerm_a = "OFF"
    else:
        print("Error status")
    return statusLCD_a, statusLog_a, statusTerm_a
def statusB(paramB):
    if paramB == [1, 1, 1] :
        statusLCD_b = "ON"
        statusLog_b = "ON"
        statusTerm_b = "ON" 
    elif paramB == [1, 1, 0] :
        statusLCD_b = "ON"
        statusLog_b = "ON"
        statusTerm_b = "OFF"
    elif paramB == [1, 0, 1] :
        statusLCD_b = "ON"
        statusLog_b = "OFF"
        statusTerm_b = "ON"
    elif paramB == [0, 1, 1] :
        statusLCD_b = "OFF"
        statusLog_b = "ON"
        statusTerm_b = "ON"
    elif paramB == [0, 0, 1] :
        statusLCD_b = "ON"
        statusLog_b = "ON"
        statusTerm_b = "OFF"
    elif paramB == [0, 0, 0] :
        statusLCD_b = "OFF"
        statusLog_b = "OFF"
        statusTerm_b = "OFF"
    else:
        print("Error status")
    return statusLCD_b, statusLog_b, statusTerm_b, paramB
settingsMenu(paramA)