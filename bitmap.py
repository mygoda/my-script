# 使用 python 实现 bitmap 位图
# 思路： 使用数组实现 bitmap 位图


class BitMap(object):
    """
        位图
    """

    def __init__(self, num):
        self.index = self.get_bitmap_index(num=num)
        # 初始化位图，所有的都为0
        self.bitmap = [0 for i in range(self.index)]

    def get_bitmap_index(self, num):
        """
            默认向上取整， 由于 python 一个整型为4个字节，并且有一位为符号位，因此目前只能有31位可以表示数字
        :param num: 
        :return: 
        """
        return int((num + 31 - 1) / 31)

    def get_bit_index(self, num):
        """
            获取 当前这个数在哪一个位置上
        :param num: 
        :return: 
        """
        return num % 31

    def set(self, num):
        # 计算当前元素在数组中的位置
        ele_index = self.get_bitmap_index(num)
        bit_index = self.get_bit_index(num=num)
        ele = self.bitmap[ele_index]
        self.bitmap[ele_index] = ele | (1 << bit_index)

    def clear(self, num):
        # 计算当前元素在数组中的位置
        ele_index = self.get_bitmap_index(num)
        bit_index = self.get_bit_index(num=num)
        ele = self.bitmap[ele_index]
        self.bitmap[ele_index] = ele & (~(1 << bit_index))

    def test(self, num):
        """
            判断是否为1
        :param num: 
        :return: 
        """
        ele_index = self.get_bitmap_index(num)
        bit_index = self.get_bit_index(num=num)
        if self.bitmap[ele_index] & (1 << bit_index):
            return True
        return False