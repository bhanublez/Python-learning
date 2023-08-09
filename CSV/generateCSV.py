import csv
# hosts=[["workstation.local","192.168.252.28"],["webserver.cloud","10.2.4.2"]]
# with open("hosts.csv","w") as hosts_csv:
#     writer=csv.writer(hosts_csv)
#     writer.writerows(hosts)

#read csv hosts file
with open("hosts.csv") as hosts_csv:
    reader=csv.reader(hosts_csv)
    for row in reader:
        print("{} has the ip {}".format(row[0],row[1]))