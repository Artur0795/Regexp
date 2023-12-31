from pprint import pprint
import csv
import re


def names_sorting():
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        if len((re.sub(name_pattern, name_substitution, line).split())) == 3:
            column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
            column[1] = re.sub(name_pattern, name_substitution, line).split()[1]
            column[2] = re.sub(name_pattern, name_substitution, line).split()[2]
        elif len((re.sub(name_pattern, name_substitution, line).split())) == 2:
            column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
            column[1] = re.sub(name_pattern, name_substitution, line).split()[1]
            column[2] = ''
        elif len((re.sub(name_pattern, name_substitution, line).split())) == 1:
            column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
            column[1] = ''
            column[2] = ''
    return


def phone_number_formatting():
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list:
        column[5] = phone_pattern.sub(phone_substitution, column[5])
    return


def duplicates_connecting():
    contact_list = {}
    for column in contacts_list[1:]:
        last_name = column[0]
        if last_name not in contact_list:
            contact_list[last_name] = column
        else:
            for index, item in enumerate(contact_list[last_name]):
                if item == '':
                    contact_list[last_name][index] = column[index]

    for last_name, contact in contact_list.items():
        for contacts in contact:
            if contact not in contacts_list_updated:
                contacts_list_updated.append(contact)
    return contacts_list_updated


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as in_file:
        rows = csv.reader(in_file, delimiter=",")
        contacts_list = list(rows)
        contacts_list_updated = []
        names_sorting()
        phone_number_formatting()
        duplicates_connecting()
    with open("phonebook.csv", "w") as out_file:
        datawriter = csv.writer(out_file, delimiter=',')
        datawriter.writerows(contacts_list_updated)
    pprint(contacts_list_updated)