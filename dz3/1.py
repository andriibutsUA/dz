import json
import ast


class FindData:
    def __init__(self, file_name, object_list):
        self.file_name = file_name
        self.object_list = object_list

    def find(self, object_id):
        with open(self.file_name, 'r') as f:
            data = json.load(f)
        for d in data[self.object_list]:
            if d['id'] == object_id:
                print(d)
                return d

    def add(self, dictionary):
        the_id = dictionary['id']
        with open(self.file_name, 'r') as f:
            data = json.load(f)
        data[self.object_list].append(dictionary)
        with open(self.file_name, 'w') as f:
            json.dump(data, f)
        print(data[self.object_list])
        return the_id

    def remove(self, object_id):
        result = False
        with open(self.file_name, 'r') as f:
            data = json.load(f)
            for d in data[self.object_list]:
                if d['id'] == object_id:
                    index_of = data[self.object_list].index(d)
                    result = True
                    data[self.object_list].pop(index_of)
                    with open(self.file_name, 'w') as k:
                        json.dump(data, k)
        print(data[self.object_list])
        return result

    def update(self, data):
        if 'id' not in data:
            print('You did not provide id')
        else:
            with open(self.file_name, 'r') as f:
                json_data = json.load(f)
                for d in json_data[self.object_list]:
                    if d['id'] == data['id']:
                        for key in d:
                            if key in data:
                                d[key] = data[key]
            with open(self.file_name, 'w') as f:
                json.dump(json_data, f)
            print(json_data[self.object_list])
            return True

    def choose_action(self):
        print('Choose action:')
        print('1. Find')
        print('2. Add')
        print('3. Remove')
        print('4. Update')
        choice = input('>>> ')
        if choice == '1':
            input_id = int(input('Enter id to find: '))
            self.find(input_id)
        elif choice == '2':
            input_dictionary = ast.literal_eval(input('Enter dictionary to add:\n'))
            self.add(input_dictionary)
        elif choice == '3':
            input_id = int(input('Enter id to remove: '))
            self.remove(input_id)
        elif choice == '4':
            input_data = ast.literal_eval(input('Enter data with id to update '))
            self.update(input_data)

x = FindData('data.json', 'cars')
x.choose_action()