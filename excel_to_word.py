import csv


class ExcelToWord():
    """
    变量名及其含义
    seq_num：表格中所需数值所处列数
    sort_method：如何排序，包括：max 最大值，min 最小值，positive 大于等于0，negative 小于0
    sort_num：最大最小值要几个，正负时可不填
    """
    def __init__(self, seq_num=3, sort_method='max', sort_num=5, csv_name='aaa.csv', txt_name='bbb.txt'):
        self.seq_num = seq_num
        self.sort_method = sort_method
        self.sort_num = sort_num
        self.csv_name = csv_name
        self.txt_name = txt_name


    # 从csv文件中导出数据，存储为字典组成的列表
    # 入参：seq_num 第几列
    #       filename 文件名
    # 出参：bank_number_list 列表，共后续使用
    def csv_to_list(self):
        bank_number_list = []
        with open(self.csv_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            i = 1
            for row in reader:
                # 提取种类名称
                if i == 5: # 第5列数据（表格如果变化，也需要改变）
                    self.type = row[self.seq_num-1]
                # 提取实际数据
                if i >= 8: # 第8列开始为分行数据（表格如果变化，也需要改变）
                    if row[1] != '':
                        bank_number_list.append({'bank_name':row[1], 'number_value':row[self.seq_num-1]})
                i += 1
        self.bank_number_list = bank_number_list


    # 从列表中按需求选取最大的n个/最小的n个/大于0/小于0的数值
    def select_from_list(self):
        selected_list = []
        if self.sort_method == 'max':
            procedure_list = self.bank_number_list
            # 先排序，再筛选
            for i in range(1, len(procedure_list)):
                key = procedure_list[i]
                for j in range(i):
                    if key['number_value'] > procedure_list[j]['number_value']:
                        procedure_list.pop(i)
                        procedure_list.insert(j, key)
                        break
            for i in range(self.sort_num):
                selected_list.append(procedure_list[i])

        if self.sort_method == 'min':
            procedure_list = self.bank_number_list
            # 先排序，再筛选
            for i in range(1, len(procedure_list)):
                key = procedure_list[i]
                for j in range(i):
                    if key['number_value'] < procedure_list[j]['number_value']:
                        procedure_list.pop(i)
                        procedure_list.insert(j, key)
                        break
            for i in range(self.sort_num):
                selected_list.append(procedure_list[i])

        if self.sort_method == 'positive':
            for data in self.bank_number_list:
                if data['number_value'] >= 0:
                    selected_list.append(data)

        if self.sort_method == 'negative':
            for data in self.bank_number_list:
                if data['number_value'] < 0:
                    selected_list.append(data)

        self.selected_list = selected_list

    # 将选择结果存储至txt文件
    def list_to_txt(self):
        if self.sort_method == 'max':
            print(self.type)
            print(self.selected_list)

        if self.sort_method == 'min':
            pass

        if self.sort_method == 'positive':
            pass

        if self.sort_method == 'negative':
            pass



# 测试脚本
if __name__ == '__main__':

    etw = ExcelToWord(seq_num=3)
    # 需要第几列的数据，源文件的文件名是什么
    etw.csv_to_list()
    # 需要提取哪种数据类型，需要最大/最小的几行
    etw.select_from_list()
    # 目标文件的文件名是什么
    etw.list_to_txt()
