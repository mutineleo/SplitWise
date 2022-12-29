import abc
class BillServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addBill(self,id,groupId,amount,contributions,paidBy):
        pass