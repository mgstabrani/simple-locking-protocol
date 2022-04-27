from transactionTable import transactionTabel

class transactionManager:
    def __init__(self, transactionTable: transactionTabel):
        self.transactionTable = transactionTable
        self.waitOperations = []
        self.operationSchedule = []
        self.grantOrder = []
        self.lockGrant = {}

        for transaction in self.transactionTable.getAllTransactions():
            self.lockGrant[transaction] = []

        operationOrder = transactionTable.getOperationOrder()

        for operation in operationOrder:
            transaction = transactionTable.getTransactionFromOperation(operation)
            dataItem = transactionTable.getDataItemFromOperation(operation)
            if operation[0] == 'U':
                self.lockGrant[transaction].remove(dataItem)
            elif operation[0] == 'C':
                self.lockGrant[transaction] = []
                self.operationSchedule.append(operation)
                self.grantOrder.append(['-1','-1'])
            else:
                if not self.isDataItemGranted(dataItem, transaction):
                    if dataItem not in self.lockGrant[transaction]:
                        self.grantOrder.append([transaction, dataItem])
                        self.lockGrant[transaction].append(dataItem)
                    else:
                        self.grantOrder.append(['-1','-1'])
                    self.operationSchedule.append(operation)

                else:
                    self.operationSchedule.append('A' + transaction[1])
                    self.grantOrder.append(['-1','-1'])
                    self.waitOperations.append(operation)

    def getOperationSchedule(self):
        return self.operationSchedule

    def isDataItemGranted(self, dataItem, transaction):
        for grant in self.lockGrant:
            return bool((dataItem in self.lockGrant[grant] and grant != transaction))

    def getWaitOperations(self):
        return self.waitOperations

    def getAlllockGrant(self):
        return self.lockGrant

    def getGrantOrder(self):
        return self.grantOrder

    def displayOperationSchedule(self):
        print('='*30)
        print("Operation Order")
        print('='*30)
        schedule = self.getOperationSchedule()
        i = 0
        for operation in schedule:
            transaction = self.transactionTable.getTransactionFromOperation(operation)
            dataItem = self.transactionTable.getDataItemFromOperation(operation)
            if operation[0] == 'R':
                print(operation, ': Transaksi', transaction, 'melakukan read data', dataItem, end=' ')
                if self.grantOrder[i][0] != '-1':
                    print('(', self.grantOrder[i][0], 'granted on', self.grantOrder[i][1], ')')
                else:
                    print()
            elif operation[0] == 'W':
                print(operation, ': Transaksi', transaction, 'melakukan write data', dataItem, end=' ')
                if self.grantOrder[i][0] != '-1':
                    print('(', self.grantOrder[i][0], 'granted on', self.grantOrder[i][1], ')')
                else:
                    print()
            elif operation[0] == 'C':
                print(operation, ': Transaksi', transaction, 'melakukan commit')
            elif operation[0] == 'A':
                print(operation, ': Transaksi', transaction, 'melakukan abort terhadap operasi')

            i += 1
