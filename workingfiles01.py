# sales_log = open('spam_ortes.txt', 'w')
# 'w' for write / 'r' for read / 'a' for append
# sales_log.write("them spam van\n") - 
# sales_log.close()
performances = {'Ventriloquism':       '9:00am', 
                'Snake Charmer':       '12:00pm', 
                'Amazing Acrobatics':  '2:00pm', 
                'Enchanted Elephants': '5:00pm'}

schedule_file = open('schedule.txt', 'w')
for key, val in performances.items():
    schedule_file.write(key + "-" + val + "\n")
    