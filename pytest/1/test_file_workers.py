from src.file_workers import read_from_file


# def test_read_from_file():
#     test_data = ['one\n', 'two\n', 'three']
#     assert test_data == read_from_file('testfile.txt')

def create_test_data(test_data):
    with open('testfile.txt', 'a') as f_o:
        f_o.writelines(test_data)

def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)                 #открываем txt записываем данные(test_data сверяем их с нашей типо БД read_from_file а наша фикстура в conftest очищает ее в начале
    assert test_data == read_from_file('testfile.txt')









