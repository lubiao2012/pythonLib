import sys
import os
import MySQLdb

class MysqlService():
    def __init__(self, ip, port, username, passwd, database):
        self.ip=ip
        self.port =port
        self.username = username 
        self.passwd = passwd
        self.database = database

    def connect(self):
        self.conn = MySQLdb.connect(host=self.ip,port=self.port,user=self.username ,passwd=self.passwd , db=self.database)
        self.cur=self.conn.cursor()



if __name__ == "__main__":
    test=MysqlService("127.0.0.1",3306,"root","wangrun","wangrun")
    test.connect()




#create databasea 
#    cur.execute('create database if not exists python')
#    conn.select_db('python')
#create table
#    cur.execute('create table test(id int,info varchar(20))')
#insert 
#    value=[1,'hi rollen']
#    cur.execute('insert into test values(%s,%s)',value)
#     
#    values=[]
#    for i in range(20):
#        values.append((i,'hi rollen'+str(i)))
#         
#    cur.executemany('insert into test values(%s,%s)',values)
#update 
#    cur.execute('update test set info="I am rollen" where id=3')
# 
#    conn.commit()
#    cur.close()
#    conn.close()
#error
#except MySQLdb.Error,e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

#  conn.select_db('python')
# 
#    count=cur.execute('select * from test')
#    print 'there has %s rows record' % count
#result
#    result=cur.fetchone()
#    print result
#    print 'ID: %s info %s' % result
# 
#    results=cur.fetchmany(5)
#    for r in results:
#        print r
# 
#    print '=='*10
#    cur.scroll(0,mode='absolute')
# 
#    results=cur.fetchall()
#    for r in results:
#        print r[1]
#     
# 
#    conn.commit()
#    cur.close()
#    conn.close()

        

