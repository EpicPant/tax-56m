import pandas as pd

# batch_number = int(input('Batch No.')) - 1

starting_batch = int(input('Start with Batch #'))
no_of_batch = int(input('How many batch to run: '))

for i in range(no_of_batch):
    print('Batch #' + str(i + 1))

    csv_reader = pd.read_csv('56m.csv', delimiter=',', nrows=30, skiprows=30 * (starting_batch + i - 1))

    for index, row in csv_reader.iterrows():
        print(index, ' - ', row[0], '', row[1])
    
    print('Batch finished')
    if len(csv_reader.index) != 30:
        break