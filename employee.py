#--   Python coding challenge Employee program  --#

class Employee:
    def __init__ (self):
        self.name = 'Sandeep'
        self.age = 26
        self.salary = 75000
        self.email = 'sandeep_sreehari@gmail.com'

    def modify_name_and_email (self, new_name, new_email):
        self.name = new_name
        self.email = new_email
        return (self.name, self.email)


f = Employee()
print ("\nOriginal: ")
print ("\nName  --> {}\nEmail --> {}\nAge --> {}\nSalary --> {}".format (str (f.name), str (f.email), str (f.age), str (f.salary)))

#----

e = Employee()
new_name = 'TestName'
new_email = 'Test.Name@emailid.com'

updated_name, updated_email = e.modify_name_and_email (new_name, new_email)

print ("\n\nUpdated: ")
print ("\nName  --> {}\nEmail --> {}\nAge --> {}\nSalary --> {}".format (str (updated_name), str (updated_email), str (e.age), str (e.salary)))
print ("\n")

#--
