import hashlib


class Design:
    def __init__(self, name, lower_left_x, lower_left_y, upper_right_x, upper_right_y, polygon_count, md5sum):
        self.name = name
        # 将坐标从微米转换为毫米
        self.lower_left_x = lower_left_x / 1000
        self.lower_left_y = lower_left_y / 1000
        self.upper_right_x = upper_right_x / 1000
        self.upper_right_y = upper_right_y / 1000

        self.polygon_count = polygon_count
        self.md5sum = md5sum

        self.area = self.calculate_area()
        self.density = self.calculate_density()

    def calculate_area(self):
        """计算设计的面积"""
        width = self.upper_right_x - self.lower_left_x
        height = self.upper_right_y - self.lower_left_y
        return width * height

    def calculate_density(self):
        """计算设计的密度"""
        return self.polygon_count / self.area


class Library:
    def __init__(self):
        self.designs = []

    def add_design(self, design):
        """向库中添加一个设计"""
        self.designs.append(design)

    def print_designs_by_density(self):
        """按密度排序并打印设计的名称和md5sum"""
        sorted_designs = sorted(self.designs, key=lambda x: x.density, reverse=True)
        for design in sorted_designs:
            print(f"{design.name} - {design.md5sum}")


# 从testdata.txt读取并执行
if __name__ == "__main__":
    library = Library()
    with open("testdata.txt", "r") as file:
        # 使用 next() 跳过文件的标题行
        next(file)

        for line in file:
            data = line.strip().split("\t")

            # 将数据进行正确的类型转换
            name = data[0]
            lower_left_x = float(data[1])
            lower_left_y = float(data[2])
            upper_right_x = float(data[3])
            upper_right_y = float(data[4])
            polygon_count = int(data[5])
            md5sum = data[6]

            design = Design(name, lower_left_x, lower_left_y, upper_right_x, upper_right_y, polygon_count, md5sum)
            library.add_design(design)

    library.print_designs_by_density()

