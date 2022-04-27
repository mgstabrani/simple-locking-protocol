class transactionTabel:
    def __init__ (self, file):
        file = open(file, "r")

        self.content = []
        for line in file.readlines():
            self.content.append(line.replace('\n', ''))

        self.transactions = self.content[0].split('     ')
        for i in range (len(self.transactions)):
            self.transactions[i] = self.transactions[i].replace(' ', '')

        self.operationOrder = []
        for i in range(1,len(self.content)):
            nthTransaction = int(self.getnthTransaction(len(self.content[i].split('    '))))
            operation = self.content[i].replace('    ', '')
            self.operationOrder.append(operation[0] + str(nthTransaction) + operation[1:])

    def getAllTransactions(self):
        return self.transactions

    def getOperationOrder(self):
        return self.operationOrder

    def getnthTransaction(self, numberOfElmt):
        return (numberOfElmt-1)/2 + 1

    def getDataItemFromOperation(self, operation):
        return operation[-2]

    def getTransactionFromOperation(self, operation):
        transaction = 'T' + operation[1:2]
        for i in range(2,len(operation)):
            if operation[i] != '(':
                transaction += operation[i]
            else:
                break
        return transaction
