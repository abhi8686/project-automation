import os,socket,getpass,subprocess

dataBaseType=["","mysql","mongodb","Postgresql","exit"]
commandForDatabase=['',
'sudo apt-get install --yes --force-yes mysql-server',
'sudo apt-get install -y mongodb-org',
'sudo apt-get install --yes --force-yes postgresql pgadmin3']
def installDatabase():
	print "enter which database u want "
	for i in range(1,len(dataBaseType)):
		print "       enter     "+str(i)+"       for        " +dataBaseType[i]
	databaseinput=input();
	if(databaseinput==4):
		print "sucessfully installed"
	elif(databaseinput!=4):

		os.system(commandForDatabase[databaseinput])
	print "projects have been sucessfully installed please notify if u need anything more "
def installRuby():
	os.system("sudo apt-get install ruby-full")
	os.system("gem list")
	print "following gems have been installed if u requirment is not met please install manually";
	installDatabase();

def installAndriod():
	os.system("mkdir -p ~/opt/abhi")
	os.system("cd ~/opt/abhi")
	os.system("wget http://dl.google.com/android/android-sdk_r24-linux.tgz")
	os.system("gunzip android-sdk_r24-linux.tgz")
	os.system("tar xvf android-sdk_r24-linux.tar")
	os.system("mv android-sdk-linux android-sdk")
	os.system("rm android-sdk_r24-linux.tar")
	print "please check the following folder for the sdk "+"~/opt/abhi";
	os.system("ls -a ~/opt/local")
	installDatabase();

def installDjango():
	os.system("pip install django");
if(getpass.getuser()!="ehc"):
	print "u must be a ehc employ"
else:
	print "greetings :"+getpass.getuser();
path_user=os.environ['HOME']
print path_user

print socket.gethostname()
applicationType=["ruby on rails","andriod development kits", "django"]

for  i in range(0,len(applicationType)):
	print "    enter   " +str(i)+ "     for  " +applicationType[i];

application_type=input()

if(0<application_type<3):
	if(application_type==0):
		print "ur application type is ruby all the depencices will be installed"
		installRuby();
	if(application_type==1):
		print "ur application type is andriod all the depencices wiill be installed"
		installAndriod()

	if(application_type==2):
		print "ur applcation type is django all the dependcies will be installed"
		installDjango()
