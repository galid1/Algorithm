class Solution:
    def validUtf8(self, data):
        def get_head_five_bits(bits):
            return bits.zfill(8)[:5]

        def get_byte_cnt(head_five_bits):
            if head_five_bits == '11110':
                return 4
            elif head_five_bits[:4] == '1110':
                return 3
            elif head_five_bits[:3] == '110':
                return 2
            elif head_five_bits[0] == '0':
                return 1
            else:
                return 5

        def is_mid_byte(head_two_bits):
            return head_two_bits[:2] == '10'


        idx = 0
        while idx < len(data):
            head_byte = str(bin(data[idx]))[2:]
            head_byte_four_bits = get_head_five_bits(head_byte)
            byte_cnt = get_byte_cnt(head_byte_four_bits)

            if byte_cnt == 5:
                return False

            for i in range(idx+1, idx+byte_cnt):
                if i >= len(data):
                    return False

                head_two_bits = bin(data[i])[2:].zfill(8)[:2]
                if not is_mid_byte(head_two_bits):
                    return False

            idx = idx + byte_cnt

        return True


s = Solution()
# data = [197,130,1]
# data = [235,140,4]
# data = [255]
# data = [145]
# data = [240,162,138,147,145]
# data = [248,130,130,130]
data = [230,136,145]

# for d in data:
#     print(bin(d))
print(s.validUtf8(data))

