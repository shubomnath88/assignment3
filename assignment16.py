#TABLE - BOOK
import sqlite3
conn = sqlite3.connect('test.db')
print("opend db successfully")
conn.execute('''create table BOOK
                (BOOK_ID INT PRIMARY KEY  NOT NULL,
                TITLE_ID INT  NOT NULL,
                LOCATION CHAR(50)   NOT NULL,
                GENRE INT)''')
print("table created ")
conn.execute("INSERT INTO BOOK(BOOK_ID, TITLE_ID,LOCATION,GENRE) VALUES(1,23,'JUVE',85)")
conn.execute("INSERT INTO BOOK(BOOK_ID, TITLE_ID,LOCATION,GENRE) VALUES(2,12,'SPAIN',95)")
conn.execute("INSERT INTO BOOK(BOOK_ID, TITLE_ID,LOCATION,GENRE) VALUES(3,25,'BARCA',55)")
conn.commit()
print("record created")
cursor = conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE FROM BOOK")
for row in cursor:
    print("BOOK_ID = ",row[0])
    print("TITLE_ID = ",row[1])
    print("LOCATION =",row[2])
    print("GENRE = ",row[3])
print("operation done")
conn.execute("UPDATE BOOK set GENRE = 75 where BOOK_ID = 3")
conn.commit()
print("rows updated",conn.total_changes)
cursor = conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE FROM BOOK")
for row in cursor:
   print("BOOK_ID = ",row[0])
   print("TITLE_ID = ",row[1])
   print("LOCATION =",row[2])
   print("GENRE = ",row[3])
print("operation done")


#TABLE TITLES
conn.execute('''create table TITLES
              (TITLE_ID INT PRIMARY KEY  NOT NULL,
                TITLE CHAR(50)  NOT NULL,
                ISBN INT    NOT NULL,
                PUBLISHER_ID INT   NOT NULL,
                YOP INT   NOT NULL)''')
print("table created ")
conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,YOP) VALUES(85,'SUHU',8585,525202,1995)")
conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,YOP) VALUES(86,'JHHDG',5855,125242,1998)")
conn.commit()
print("record created")
cursor = conn.execute("SELECT TITLE_ID,TITLE,ISBN,PUBLISHER_ID,YOP FROM TITLES")
for row in cursor:
    print("TITLE_ID = ",row[0])
    print("TITLE = ", row[1])
    print("ISBN = ", row[2])
    print("PUBLISHER_ID = ", row[3])
    print("YOP = ", row[4])
print("done")
conn.execute("UPDATE TITLES set ISBN = 7896 where TITLE_ID = 86")
conn.commit()
print("rows updated",conn.total_changes)
cursor = conn.execute("SELECT TITLE_ID,TITLE,ISBN,PUBLISHER_ID,YOP FROM TITLES")
for row in cursor:
    print("TITLE_ID = ",row[0])
    print("TITLE = ", row[1])
    print("ISBN = ", row[2])
    print("PUBLISHER_ID = ", row[3])
    print("YOP = ", row[4])
print("done")


#TABLE - PUBLISHERS
conn.execute('''create table PUBLISHER
             (P_ID INT PRIMARY KEY  NOT NULL,
               NAME CHAR(50)  NOT NULL,
               S_ADDR CHAR(50)    NOT NULL,
               SUITE_NO INT   NOT NULL,
               ZC_ID INT   NOT NULL)''')
print("table created ")
conn.execute("INSERT INTO PUBLISHER(P_ID,NAME,S_ADDR,SUITE_NO,ZC_ID) VALUES(1,'SHU','LAMKJJ',5202,195)")
conn.execute("INSERT INTO PUBLISHER(P_ID,NAME,S_ADDR,SUITE_NO,ZC_ID) VALUES(2,'SHUBOM','BGTFGG',5252,196)")
conn.commit()
print("record created")
cursor = conn.execute("SELECT P_ID,NAME,S_ADDR,SUITE_NO,ZC_ID FROM PUBLISHER")
for row in cursor:
    print("P_ID = ",row[0])
    print("NAME = ", row[1])
    print("S_ADDR = ", row[2])
    print("SUITE_NO = ", row[3])
    print("ZC_ID = ", row[4])
print("done")
conn.execute("UPDATE PUBLISHER set SUITE_NO = 7896 where P_ID = 1")
conn.commit()
print("rows updated",conn.total_changes)
cursor = conn.execute("SELECT P_ID,NAME,S_ADDR,SUITE_NO,ZC_ID FROM PUBLISHER")
for row in cursor:
    print("P_ID = ",row[0])
    print("NAME = ", row[1])
    print("S_ADDR = ", row[2])
    print("SUITE_NO = ", row[3])
    print("ZC_ID = ", row[4])
print("done")

#TABLE - ZIP_C
conn.execute('''create table ZIP_C
             (ZC_ID INT PRIMARY KEY  NOT NULL,
               CITY CHAR(50)  NOT NULL,
               STATE CHAR(50)    NOT NULL,
               ZC INT   NOT NULL)''')
print("table created ")
conn.execute("INSERT INTO ZIP_C(ZC_ID,CITY,STATE,ZC) VALUES(195,'SHU','LAMKJJ',5202)")
conn.execute("INSERT INTO ZIP_C(ZC_ID,CITY,STATE,ZC) VALUES(196,'SHUN','LAMKJKJJ',2202)")
conn.commit()
print("record created")
cursor = conn.execute("SELECT ZC_ID,CITY,STATE,ZC FROM ZIP_C")
for row in cursor:
    print("ZC_ID = ",row[0])
    print("CITY = ", row[1])
    print("STATE = ", row[2])
    print("ZC = ", row[3])

print("done")
conn.execute("UPDATE ZIP_C set STATE = 'JHHHJK' where ZC_ID = 196")
conn.commit()
print("rows updated",conn.total_changes)
cursor = conn.execute("SELECT ZC_ID,CITY,STATE,ZC FROM ZIP_C")
for row in cursor:
    print("ZC_ID = ",row[0])
    print("CITY = ", row[1])
    print("STATE = ", row[2])
    print("ZC = ", row[3])


#TABLE - AUTHORS TITLE
conn.execute('''create table A_TITLE
             (AT_ID INT PRIMARY KEY NOT NULL,
           A_ID INT  NOT NULL,
          TID INT  NOT NULL)''')
print("table created")
conn.execute("INSERT INTO A_TITLE(AT_ID,A_ID,TID) VALUES(19,452,158)")
conn.execute("INSERT INTO A_TITLE(AT_ID,A_ID,TID) VALUES(20,451,156)")
conn.commit()
print("record created")

cursor = conn.execute("SELECT AT_ID,A_ID,TID FROM A_TITLE")
for row in cursor:
    print("AT_ID = ",row[0])
    print("A_ID = ", row[1])
    print("TID = ", row[2])
conn.execute("UPDATE A_TITLE set A_ID = 400 where AT_ID = 19")
conn.commit()
print("rows updated",conn.total_changes)
cursor = conn.execute("SELECT AT_ID,A_ID,TID FROM A_TITLE")
for row in cursor:
    print("AT_ID = ",row[0])
    print("A_ID = ", row[1])
    print("TID = ", row[2])


#TABLE - AUTHORS
conn.execute('''create table AUTHOR
             (A_ID INT PRIMARY KEY NOT NULL,
             FN CHAR(50)  NOT NULL,
             MN CHAR(50)  NOT NULL,
             LN CHAR(50) NOT NULL)''')
print("table created")
conn.execute("INSERT INTO AUTHOR(A_ID,FN,MN,LN) VALUES(19,'SHGY','NBVCC','HJDG')")
conn.execute("INSERT INTO AUTHOR(A_ID,FN,MN,LN) VALUES(20,'SHGHJHJY','VCC','MNHJDG')")
conn.commit()
print("record created")

cursor = conn.execute("SELECT A_ID,FN,MN,LN FROM AUTHOR")
for row in cursor:
    print("A_ID = ",row[0])
    print("FN = ", row[1])
    print("MN = ", row[2])
    print("LN = ", row[3])
conn.execute("UPDATE AUTHOR set LN = 'NATH' where A_ID = 19")
conn.commit()
print("rows updated",conn.total_changes)
cursor = conn.execute("SELECT A_ID,FN,MN,LN FROM AUTHOR")
for row in cursor:
    print("A_ID = ",row[0])
    print("FN = ", row[1])
    print("MN = ", row[2])
    print("LN = ", row[3])





