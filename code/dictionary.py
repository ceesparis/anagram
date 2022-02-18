import csv

with open('data/nl_woorden.csv', 'r') as file:
    csv_reader = csv.reader(file)

    with open('data/clean_woorden.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')
        unique_words = set()
        for line in csv_reader:
            if line: 
                clean = line[0]
                clean = clean.split('/')
                clean_word = clean[0]
                clean_word = clean_word.lower()
                if clean_word in unique_words:
                    continue
                unique_words.add(clean_word)

        for word in unique_words:
            csv_writer.writerow([word])