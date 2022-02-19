# tach user name va email domain 
def xuly(email):
    #tach user name
    email_username = email[0:email.index("@")]
    #tach email domain
    email_domain = email[email.index("@")+1:]
    return [email_username, email_domain]
#Ham in 
def printMsg(email_username, email_domain):
    print(f"Username is: {email_username}")
    print(f"Email domain is: {email_domain}")

def main():
    email = input("Please enter your email adddress: ").strip()
    email_username, email_domain = xuly(email)
    printMsg(email_username, email_domain)


if __name__ == "__main__":
    main()