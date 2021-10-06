from tkinter import *
import random
import array
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password():
    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = 12

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x

    # print out password
    entry3.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    dataweb= entry1.get()
    dataeu = entry2.get()
    datap = entry3.get()
    print(dataweb,dataeu,datap)
    f1 = open('fie1.txt','a')
    f1.write(f'\n {dataweb} | {dataeu} |  {datap}')
    f1.close()





# ---------------------------- UI SETUP ------------------------------- #

root = Tk()

root.title('Password Manager')
root.config(padx=50,pady = 50)


imag = PhotoImage(file='logo.png')
canvas = Canvas(root,width = 200,height = 200)
canvas.create_image(100,100,image =imag )
canvas.grid(row = 0,column = 1)

lebal0 = Label(root, text = 'Website:')
lebal0.grid(row = 1,column = 0)
entry1 = Entry(root,width = 35)
entry1.grid(row = 1,column = 1, columnspan = 2 )
entry1.focus()


lebal1 = Label(root, text = 'Email/Username:')
lebal1.grid(row = 2,column = 0)
entry2 = Entry(root,width = 35)
entry2.grid(row = 2,column = 1, columnspan = 2)





lebal2 = Label(root, text = 'Password:')
lebal2.grid(row = 3,column = 0)
entry3 = Entry(root,width = 21)
entry3.grid(row = 3,column = 1)

btn1 = Button(root,text = 'Generate Password',bg = 'grey',command = password)
btn1.grid(row=3,column = 2 )

btn = Button(root,text = 'Add',width = 36 ,bg ='blue',command=add  )
btn.grid(row = 4,column = 1,columnspan =2)


root.mainloop()