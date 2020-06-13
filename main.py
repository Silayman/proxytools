from proxytools.formatproxy import formatproxy
def main():
    returned_proxy = formatproxy("162.10.10.10:3128").format_request()
    print(returned_proxy)


if __name__ == "__main__":
    main()