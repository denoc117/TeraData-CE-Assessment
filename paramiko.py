import paramiko

ssh = paramiko.SSHClient()
ssh.connect(host, port=p, timeout=2)
cmd = "service httpd status; curl -X GET http://localhost:8080/app -i -f"

stdin, stdout, stderr = ssh.exec_command(cmd)

for line in stdout.readlines():
    print(line)
ssh.close()
