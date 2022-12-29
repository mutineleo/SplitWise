import sys
sys.path.append('/Users/a23135334/Documents/splitwise')

from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from controllers.bill_controller import BillController

from services.user_service import UserService
from services.group_service import GroupService
from services.bill_service import BillService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('User1','Osama')
user2 = userController.addUser('User2','Adnan')
user3 = userController.addUser('User3','Akmal')
user4 = userController.addUser('User4','Faizan')
user5 = userController.addUser('User5','Ali')

members = [user1,user2,user3,user4,user5]

group1 = groupController.addGroup('Group1','Ashiyana',members)
# print(group1.getMembers())

paidBy = {'User1':100,'User2':150,'User3':50,'User5':200}
contribution = {'User1':100,'User2':100,'User3':100,'User4':100,'User5':100,}

billController.addBill('Bill1','group1', 500, contribution, paidBy )

balance = billController.getUserBalance('User3')
print(balance)