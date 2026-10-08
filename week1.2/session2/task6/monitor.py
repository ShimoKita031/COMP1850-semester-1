# Week 1.2, Session 2: Task 6
print ("Welcome to the factory monitor system.")

#get inputs

temperature = int(input("Enter machine temperature in degrees celcius: "))
pressure = int(input("Enter machine pressure in PSI: "))
operating = int(input("Enter 1 if machine is in operation, 0 if machine is not in operation:"))

match operating:
    case 1:
        if temperature > 80:
            print("Temperature is too high.")
        elif 50 <= temperature <= 80:
            print("Temperature is within safe limits.")
        else:
            print("Machine temperature is low. No action is needed to change the temperature")

        if pressure > 100:
            print("Pressure too high. Maintenance recommended")
        elif 70 <= pressure <= 100:
            print("Pressure is stable.")
        else:
            print("Pressure too low. Machine is running properly")

        if temperature > 80 or pressure > 100:
            print("Machine is currently running in unsafe conditions. Shutting the machine down is recommended.")

    case 0:
        print("The machine has stopped running. No immediate action is needed.")

    case _:
        print("Invalid operating status")