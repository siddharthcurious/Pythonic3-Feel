import subprocess
def isReachable(ip):
    out = subprocess.Popen(['wc', '-l', 'my_text_file.txt'],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

def Reachable(filename):

    with open(filename) as fileobj:
        data = fileobj.readlines()
        for ip in data:
            p = isReachable(ip.strip())
            print(p)

if __name__ == "__main__":

    Reachable("/home/siddharth/ipaddress.txt")