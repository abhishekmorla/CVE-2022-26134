import shodan
import argparse

def get_argspar():
    parser = argparse.ArgumentParser()
    parser.add_argument("-API", "--YOUR_API", dest="API", help="Your Shodan API")
    parser.add_argument("-L", "--LIMIT", dest="LIMIT", help="Enter LIMIT")
    parser.add_argument("-D", "--Shodan_Dork", dest="DORK", help="Enter Shodan Dork")
    option = parser.parse_args()
    if not option.API:
        parser.error("Please Enter Your Shodan API:")
    elif not option.LIMIT:
        parser.error("Please Enter Your Limit:")
    elif not option.DORK:
        parser.error("Please Enter Shodan Dork:")
    return option

options = get_argspar()


limit = int(options.LIMIT)  # set the limit according to your query credits
counter = 0

api = shodan.Shodan(options.API)
try:
    # Search Shodan
    # Show the results

    for result in api.search_cursor(options.DORK): # edit the "your_shodan_dork"
        print('%s' % result['ip_str']+":"+'%s' % result['port'])
        counter += 1
        if counter >= limit:
            break

except shodan.APIError as e:
    print('Error: %s' % e)
