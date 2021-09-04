class TestDataEmptyArray:
    @staticmethod
    def get_array():
        seq = []
        return seq
class TestDataUniqueValues:
    @staticmethod
    def get_array():
        seq = [1,2]
        return seq
    @staticmethod
    def get_expected_result():
        return 0
class TestDataExactlyTwoDifferentMinimums:
    @staticmethod
    def get_array():
        seq = [1,1,2,3,4,5,6]
        return seq
    @staticmethod
    def get_expected_result():
        return 0
        
