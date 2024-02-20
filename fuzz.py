import subprocess
import random
import string

def main():
    test_size = 50
    choices = string.ascii_letters + string.digits
    while test_size < 500:
        print(f"\n############################################"
              f"\n#      TEST DATA LENGTH {test_size}        #"
              f"\n############################################\n")
        data = 'a'
        for chars in range(test_size):
            data += random.choice(choices)
        print(f"\n###################################################"
              f"\n#                                                 #"
              f"\n#     ****          RESPONSE            ****      #"
              f"\n#                                                 #"
              f"\n###################################################"
              f"\n")
        output = subprocess.run(f"echo '{data}' | netcat 0.0.0.0 8888", shell=True, capture_output=True).stdout.decode()
        print(output)


        print(f"\n###################################################"
              f"\n#                                                 #"
              f"\n#     ****             DATA             ****      #"
              f"\n#                                                 #"
              f"\n###################################################"
              f"\n"
              f"{data}\n")

        for i in range(len(data)):
            match = True
            try:
                if data[i] != output[i]:
                    print(f"Character {i} does not match.")
                    match = False
            except:
                print("Length does not match.")
                match = False
                break

        if match:
            print("Output matches.")
        test_size += 50




if __name__ == '__main__':
    main()