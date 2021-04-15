import argparse
from urllib.request import urlopen
from sys import argv, exit


parser=argparse.ArgumentParser(description='''[*] Usage: python(3) clickjacking_tester.py <file_name> ''',epilog="""Made by @Ashutosh""")

def check(url):

    try:
        if "http" not in url: url = "http://" + url

        data = urlopen(url)
        headers = data.info()

        if not "X-Frame-Options" in headers: return True

    except: return False



def main():
    ''' Everything comes together '''

    try: sites = open(argv[1], 'r').readlines()
    except: args=parser.parse_args();exit(0)

    for site in sites[0:]:
        print("\n[*] Checking " + site)
        status = check(site)

        if status:
            print(" [+] Website is vulnerable!")
            print(" [*] Created a poc and saved to <URL>.html")

        elif not status: print(" [-] Website is not vulnerable!")
        else: print('Every single thing is crashed, Python got mad, dude wtf you just did?')

if __name__ == '__main__': main()