from transactionTable import transactionTabel

class transactionManager:
    def __init__(self, transactionTable: transactionTabel):
        self.transactionTable = transactionTable
        self.waitOperations = []
        self.operationSchedule = []
        self.lockGrant = {}

        for transaction in self.transactionTable.getAllTransactions():
            self.lockGrant[transaction] = []

        operationOrder = transactionTable.getOperationOrder()

        for operation in operationOrder:
            transaction = transactionTable.getTransactionFromOperation(operation)
            dataItem = transactionTable.getDataItemFromOperation(operation)

            if(not self.isDataItemGranted(dataItem, transaction)):
                self.lockGrant[transaction].append(dataItem)
                self.operationSchedule.append(operation)
            
            else:
                self.waitOperations.append(operation)

    def getOperationSchedule(self):
        return self.operationSchedule

    def isDataItemGranted(self, dataItem, transaction):
        for grant in self.lockGrant:
            if(dataItem in self.lockGrant[grant] and grant != transaction):
                return True
            else:
                return False

    def getWaitOperations(self):
        return self.waitOperations
