import csv
# Reading genebank
with open("AOL_query_2.txt", "r+") as handle:
    file = handle.readlines()
    res = []
    for line in file:
        x = line.strip()
        if x:
            res.append(x)
    version = [res[3]]
    #inititlizing 3 var for journal name, publication number, version
    new_list_key = []
    new_list_value = []
    new_version =[]
    for journal_index in range(len(res)):
        if "VERSION" in res[journal_index]:
            version = res[journal_index]
        if "JOURNAL" in res[journal_index]:
            new_list_key.append(res[journal_index])
            new_list_value.append(res[journal_index + 1])
            new_version.append(version)
            continue
    #making a list of pairs with jounal and the publication number
    journal_pair = list(zip(new_list_key, new_list_value))
    print(len(journal_pair))
    print(new_version[10])
    new_journal_version_paire = zip(new_version, journal_pair)

#writing the output into csv file having 2 col
#version of the protien, journal and accession
with open('_Output_3.csv', 'w') as output:
    excel_file = csv.writer(output)
    for data in new_journal_version_paire:
        excel_file.writerow(data)

