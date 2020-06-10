from proxytools import formatproxy
def main():
    returned_proxy = formatproxy("192.168.1.1").format_request()
    print(returned_proxy)


if __name__ == "__main__":
    main()