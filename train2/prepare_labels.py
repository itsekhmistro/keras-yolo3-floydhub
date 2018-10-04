import csv
with open('stage_1_train_labels.csv', newline='') as csvfile:
   csv_source = csv.reader(csvfile, delimiter=',', quotechar='|')
   with open('test_data.csv', 'w', newline='') as csvfile:
      csv_target = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      # Skip header.
      row = csv_source.__next__()
      print(row)
      for row in csv_source:
        if row[5] != '1':
          # Skip rows with no boxes.
          continue
        # print(row)
        # break
        # Update image path.
        row[0] = "./train2/stage_1_train_images/{}.dcm {}".format(row[0], int(float(row[1])))
        # Convert points.
        row[2] = int(float(row[2]))
        row[3] = int(float(row[1]) + float(row[3]))
        row[4] = int(float(row[2]) + float(row[4]))
        row.pop(1)
        # print(row)
        csv_target.writerow(row)
        # break