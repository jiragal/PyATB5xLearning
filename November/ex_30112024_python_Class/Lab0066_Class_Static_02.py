# 2nd Example for Static
#Static methods are more generally used in "Automation Project"
class ExcelReader:
    @staticmethod
    def read_from_excel():
        print("Static Excel Reading")


class MYSQCDBconnction:

    def readSQLFile():
        print("Reading from SQL")


class TC1:
    def testcases(self):
        ExcelReader.read_from_excel()
        MYSQCDBconnction.readSQLFile()


tc1_obj = TC1()
tc1_obj.testcases()  # testcaseses directly calling withut creating object
