#Topic of student managment using mysql 

import mysql.connector

con = mysql.connector.connect(host ="localhost",user ="root",passwd ="",database='sms')

cur = con.cursor()

from clrprint import*
clrhelp()

print(" ---------- STUDENT MANAGEMENT SYSTEM ---------- ")

ch='Y'

def while_fn ():
    while ch=="Y" or ch=="y":
        if menu==1:
            sd()
        elif menu==2 :
            pd()
        elif menu==3 :
            ad()
        elif menu==4 :
            clrprint("Thank you",clr='yellow')
            break
        else :
            clrprint("Invalid choice!",clr='red')
            menu_fn()
    while ch=="N" or ch=="n":
        clrprint("Thank you",clr='yellow')
        break

def sd():
    def menu_sdfn():
        global menu_sd
        menu_sd=int(input("\n ---- MENU---- \n press [1] To add new students data \n press [2] To show existing all data \n press [3] To delete student data using his\her name \n press [4] Main menu \n press [5] To Exit \n\n Enter your choice:"))
        if menu_sd==1:
            print(" ------ ENTER STUDENT PERSONAL DETAILS ------ ")
            name=str(input("Enter name of the student : "))
            dob=str(input("Enter  year of birth of the student : "))
            gnd=str(input("Enter male/female:"))
            fn=str(input("Enter father name of the student:"))
            mn=str(input("Enter mother name of the student:"))
            mt=str(input("Enter moter tongue of the student:"))
            nat=str(input("Enter nationality of the student:")) 
            rel=str(input("Enter religion of the student:"))
            add=str(input("Enter present address of the student:"))
            print(" \n------ ENTER STUDENT PRESENT CLASS DETAILS ------ ")
            reg=str(input("Enter regno of the student:"))
            cls=str(input("Enter class of the student:"))
            sec=str(input("Enter section of the student:"))
            com=str(input("Enter combination of the student:"))
            print(" \n------ ENTER STUDENT PASSEDOUT CLASS DETAILS ------ ")
            l=int(input("Enter  marks of the student in english : "))
            b=str(l)
            m=int(input("Enter  marks of the student in mathematics: "))
            c=str(m)
            n=int(input("Enter  marks of the student in science: "))
            d=str(n)
            o=int(input("Enter  marks of the student in social: "))
            e=str(o)
            p=int(input("Enter  marks of the student in hindi: "))
            f=str(p)
            q=sum([l,m,n,o,p])
            g=str(q)
            r=q/5
            h=str(r)

            sql = "create table if not exists student_tb ( sname varchar(30) primary key, sdob varchar(30), sgender varchar(10), sfather_name varchar(20), smother_name varchar(20), snationality varchar(40), sreligion varchar(20), saddress varchar(50), smother_tongue varchar(20), sregno varchar(20), sclass varchar(20), ssection varchar(20), scombination varchar(20))"
            cur.execute(sql)
            sql = "insert into student_tb (sname, sdob, sgender, sfather_name, smother_name, smother_tongue, snationality, sreligion, saddress, sregno, sclass, ssection, scombination) values ('"+name+"','"+dob+"','"+gnd+"','"+fn+"','"+mn+"','"+mt+"','"+nat+"','"+rel+"','"+add+"','"+reg+"','"+cls+"','"+sec+"','"+com+"')"
            cur.execute(sql)
            con.commit()
            sql="CREATE TABLE IF NOT EXISTS pocd (stu_name varchar(30) , English varchar(20) , Mathematics varchar(20), Science varchar(10),Social varchar(10), Hindi varchar(10), Total varchar(10), percentage varchar(20), PRIMARY KEY (stu_name))"
            cur.execute(sql)
            sql="insert into pocd (stu_name, English, Mathematics, Science, Social, Hindi, Total, percentage) values('"+name+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"')"
            cur.execute(sql)
            con.commit()
            print("Data Entered Successfully \n")
            menu_sdfn()

            file=open('project_data.txt','a')
            data=name+","+dob+","+gnd+","+fn+","+mn+","+mt+","+nat+","+rel+","+add+","+reg+","+cls+","+sec+","+com+","+b+","+c+","+d+","+e+","+f+","+g+","+h+'\n'
            file.write(data)
            file.close()
            
        elif menu_sd==2:
            sql='select sname, sdob, sgender, sfather_name, smother_name, smother_tongue, snationality, sreligion, saddress, English, Mathematics, Science, Social, Hindi, Total, percentage from student_tb,pocd where sname=stu_name'
            cur.execute(sql)
            fet=cur.fetchall()
            print("|| name || d-o-b || gender || fatname || motname || mot_tongue || nationality || religion || address || Eng || Math || Science || Social || Hindi || Total || percentage ||")
            for i in fet:
                print(i)
            menu_sdfn()

        elif menu_sd==3:
            search=str(input("Enter name of student :"))
            cur.execute("delete from student_tb where sname='"+search+"'")
            con.commit()
            cur.execute("delete from pocd where stu_name='"+search+"'")
            con.commit()
            print("\n Data delected successfully")
            menu_sdfn() 
            
        elif menu_sd==4:
            menu_fn()

        elif menu_sd==5 :
            clrprint("Thank you",clr='yellow')
            global ch
            ch='N'
            
        else:
            clrprint("Invalid choice!",clr='red')
            menu_sdfn()
    menu_sdfn()



def pd():
    def menu_pdfn():
        global menu_pd
        menu_pd=int(input("\n ---- MENU---- \n press [1] To show existing all data \n press [2] To search student details using student name \n press [3] To modify student details \n press [4] Main menu \n press [5] To Exit \n\n Enter your choice:"))
        if menu_pd==2:
            search=str(input("Enter name of student :"))
            cur.execute("select sname, sdob, sgender, sfather_name, smother_name, smother_tongue, snationality, sreligion, saddress from student_tb where sname='"+search+"'")
            result = cur.fetchall()
            if result==[]:
                print("No student with such Name")
            else:
                print("\n|| name || d-o-b || gnd || fathername || mothername || mother_tongue || nationality || religion || address ||")
                for x in result:
                    print(x)
                menu_pdfn()   

        elif menu_pd==3:
            y=str(input("Enter the name of student:"))
            print("-- Field names -- \n press [1] student date of birth \n press [2] student gender \n press [3] student father name \n press [4] student mother name \n press [5] student nationality \n press [6] student religion \n press [7] student sddress \n press [8] student mother tongue \n")
            k=int(input("Select the name of the field:"))
            if k<=8:
                l=['sdob','sgender','sfather_name','smother_name','snationality','sreligion','saddress','smother_tongue']
                x=l[k-1]
                z=str(input("Enter the modification required:"))
                sql="update student_tb set "+x+"='"+z+"' where sname like '"+y+"'"
                cur.execute(sql)
                con.commit()
                sql="select sname, sdob, sgender, sfather_name, smother_name, smother_tongue, snationality, sreligion, saddress from student_tb where sname like '"+y+"'"
                cur.execute(sql)
                d=cur.fetchall()
                print("Data successfully modifed")
                print("|| sname || d-o-b || gender || fathername || mothername || mother_tongue|| nationality || religion || address ||")
                for i in d:
                    print(i)
            else:
                print("Invalid choice")
                menu_pd
            

        
        elif menu_pd==1:
            sql='select sname, sdob, sgender, sfather_name, smother_name, smother_tongue, snationality, sreligion, saddress from student_tb'
            cur.execute(sql)
            fet=cur.fetchall()
            for i in fet:
                print(i)
            menu_pdfn()
        elif menu_pd==4:
            menu_fn()
        elif menu_pd==5:
            clrprint("Thank you",clr='yellow')
            global ch
            ch='N' 
        else:
            clrprint("Invalid choice!",clr='red')
            menu_pdfn()
    menu_pdfn()


def ad():
    def ad_menu():
        menu_ad=int(input("\n\n ----MAIN MENU---- \n press [1] present class details \n press [2] passedout class details \n press [3] For Main menu \n press [4] To Exit \n\n Enter your choice:"))
        if menu_ad==1:
            search=str(input("Enter name of student :"))
            cur.execute("select sregno,sclass,ssection,scombination from student_tb where sname='"+search+"'")
            result = cur.fetchall()
            print("\n|| sregno || sclass || ssection || scombination ||")
            for x in result:
                print(x)
            ad_menu()
        elif menu_ad==2:
            def menu_pfn():
                global menu_p
                menu_p=int(input("\n ---- MENU---- \n press [1] To show existing all data \n press [2] To search student passedout class details using student name \n press [3] To modify student passedout class details \n press [4] Main menu \n press [5] To Exit \n\n Enter your choice:"))
                if menu_p==2:
                        search=str(input("Enter name of student :"))
                        cur.execute("select * from pocd where stu_name='"+search+"'")
                        result = cur.fetchall()
                        if result==[]:
                            print("No student with such Name")
                        else:
                            print("\n|| stu_name || English || Mathematics || Science || Social || Hindi || Total || percentage ||")
                            for x in result:
                                print(x)
                            menu_pfn()   
                elif menu_p==3:
                    y=str(input("Enter the name of student:"))
                    x=str(input("Enter the name of the subject:"))
                    z=str(input("Enter the modification required:"))
                    sql="update pocd set "+x+"='"+z+"' where stu_name like '"+y+"'"
                    cur.execute(sql)
                    con.commit()
                    sql="select English,Mathematics,Science,Social,Hindi from pocd where stu_name like '"+y+"'"
                    cur.execute(sql)
                    data=cur.fetchall()
                    con.commit()
                    for i in data:
                        sm=0
                        for j in i:
                            x=int(j)
                            sm=sm+x
                        pct=sm/5
                    per=str(pct)
                    s=str(sm)
                    sql="update pocd set Total='"+s+"',percentage='"+per+"' where stu_name like '"+y+"'"
                    cur.execute(sql)
                    con.commit()
                    sql="select * from pocd where stu_name like '"+y+"'"
                    cur.execute(sql)
                    d=cur.fetchall()
                    print("Data successfully modifed")
                    print("|| stu_name || English || Mathematics || Science || Social || Hindi || Total || percentage ||")
                    for i in d:
                        print(i)
                    menu_pfn()
                elif menu_p==1:
                    sql='select * from pocd order by stu_name'
                    cur.execute(sql)
                    fet=cur.fetchall()
                    print("|| stu_name || English || Mathematics || Science || Social || Hindi || Total || percentage ||")
                    for i in fet:
                        print(i)
                    menu_pfn()
                elif menu_p==4:
                    menu_fn()
                elif menu_p==5:
                    clrprint("Thank you",clr='yellow')
                    global ch
                    ch='N'
                else:
                    clrprint("Invalid choice!",clr='red')
                    menu_pfn()
            menu_pfn()

        elif menu_ad==3:
            menu_fn()
        elif menu_ad==4:
            clrprint("Thank you",clr='yellow')
            global ch
            ch='N'
        else:
            clrprint("Invalid choice!",clr='red')
            ad_menu()
    ad_menu()
    
    

def menu_fn () :
    global menu
    menu=int(input(" \n ------ STUDENT PROFILE ------ \n\n ----MAIN MENU---- \n press [1] For adding new student \n press [2] For student personal details \n press [3] For student academic details \n press [4] For exit \n\n Enter your choice:"))
    while_fn()
             
menu_fn ()

print("By Monish")

































