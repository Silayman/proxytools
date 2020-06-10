from proxyerrors import InvalidProxy

class formatproxy:
	def __init__(self,proxy):
		self.proxy = proxy
	def format_request(self):
		if self.proxy.lower() == "local":
			request_proxy = None
		else:
			try:
				proxy_parts = self.proxy.split(':')
				if len(proxy_parts) == 4:
					ip, port, user, password = proxy_parts[0], proxy_parts[1], proxy_parts[2], proxy_parts[3]
					request_proxy = {'http': 'http://{}:{}@{}:{}'.format(user, password, ip, port),
								'https': 'https://{}:{}@{}:{}'.format(user, password, ip, port)}
				elif len(proxy_parts) == 2:
					ip, port = proxy_parts[0], proxy_parts[1]
					request_proxy = {'http': 'http://{}:{}'.format(ip, port),
								'https': 'https://{}:{}'.format(ip, port)}
				elif len(proxy_parts) == 5:
					ip, port, user, password = proxy_parts[1], proxy_parts[2], proxy_parts[3], proxy_parts[4]
					ip = ip.split("/")[2]
					request_proxy = {'http': 'http://{}:{}@{}:{}'.format(user, password, ip, port),
								'https': 'https://{}:{}@{}:{}'.format(user, password, ip, port)}
				else:
					raise InvalidProxy("Invalid proxy")
			except:
				raise InvalidProxy("Invalid proxy")
		return request_proxy

		
	