import subprocess
import random
import string

def main():
    choices = string.ascii_letters + string.digits + string.punctuation
    data = 'a'
    for chars in range(1500):
        data += random.choice(choices)
    output = subprocess.run(f"echo {data} | netcat 0.0.0.0 8888")

if __name__ == '__main__':
    main()