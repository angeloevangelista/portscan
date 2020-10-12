import socket

ports = [21, 23, 80, 443, 3333, 8080]

for port in ports:
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.settimeout(0.5)
  code = client.connect_ex(('127.0.0.1', port))
  if code == 0:
    print port, 'OPEN'
