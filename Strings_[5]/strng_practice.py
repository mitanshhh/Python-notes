def replace_domain (email, old_domain, new_donain):
    if "@"+ old_domain in email:
       index = email.index("@" + old_domain)
       new_email = email[:index] + "@" + new_donain
       return new_email
    return email

print(replace_domain("mitansh.j2007@gmail.com", "gmail.com", "outlook.com"))