from mysql import connector
from PyPDF2 import PdfFileReader, PdfFileWriter
from os.path import isfile
from Networking.networking import net_main


def mysql_query_read_connection(q_server, q_user, q_passwd, q_query):
    connection = connector.connect(server=q_server, username=q_user, password=q_passwd, readonly=True)
    results = connection.execute(q_query)
    return results


def pdf_watermark(input_file, watermark, output_file, password):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)
    pdf_reader = PdfFileReader(input_file)
    pdf_writer = PdfFileWriter()
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(0)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)
    choice = input('Do you want to encrypt? ')
    if choice.lower() == 'y':
        pdf_writer.encrypt(user_pwd='letmein', owner_pwd=password, use_128bit=True)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)


def word_finder(inputs):
    r_access = 'r'
    lists = []
    try:
        if isfile(inputs):
            with open(inputs, r_access) as rf:
                lines = [x for x in rf.read().split('\n') if x]
                for line in lines:
                    lists.append(line.split())
    except Exception:
        lists = inputs
    finally:
        print(lists)


if __name__ == '__main__':
    print("Main Menu")
    print("1. Add a water mark to PDF\n"
          "2. Find a word\n"
          "3. Read from a database\n"
          "4. Configure Switch\n")
    print()
    choices = int(input("Make your selection "))
    if choices == 1:
        file_in = 'C:/Users/setup/OneDrive/Documents/Project(s)/PeaceOfMinduML.pdf'
        water_file = 'C:/Users/setup/OneDrive/Documents/Project(s)/WaterMarkText.pdf'
        file_out = ''
        paswd = ''
        pdf_watermark(file_in, water_file, file_out, paswd)
    elif choices == 2:
        fin = "../src/Words.txt"
        word_finder(fin)
    elif choices == 3:
        query = ""
        server = ""
        passwd = ""
        user = ""
        mysql_query_read_connection(server, user, passwd, query)
    elif choices == 4:
        net_main()
    else:
        print('Invalid Choice')
