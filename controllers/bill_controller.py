class BillController(object):
    def __init__(self,billService):
        self.billService = billService
    def addBill(self,id,groupId,amount,contributions,paidBy):
        return self.billService.addBill(id,groupId,amount,contributions,paidBy)
    
    def getUserBalance(self,userId):
        balance = 0
        for billId in self.billService.billDetails:
            bill = self.billService.billDetails.get(billId)
            if userId in bill.getContributions():
                balance -= bill.getContributions().get(userId)
            if userId in bill.getPaidBy():
                balance += bill.getPaidBy().get(userId)
        return balance
