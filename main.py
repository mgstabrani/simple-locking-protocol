from transactionManager import transactionManager
from transactionTable import transactionTabel

file = input('Masukkan file: ')
transactionTable = transactionTabel(file)

transactionManager = transactionManager(transactionTable)
transactionManager.displayOperationSchedule()
