# 14. Write a Python function to create the HTML string with tags around the
# word(s).

def add_tags(tg, stmnt):
    out_exe = "<" + tg + ">"
    termi = "</" + tg + ">"
    return out_exe + stmnt + termi


usr_input = input("Enter Tag specification of html: ")
usr_stmt = input("Statment that you want to execute: ")
print(add_tags(usr_input, usr_stmt))
