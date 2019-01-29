'''
@author: roberto.flores
'''
import unittest
import islands

class Test(unittest.TestCase):

    def testNone(self):
        actual   = islands.process( None )
        expected = -1
        self.assertEqual( expected, actual )

    def test00(self):
        actual   = islands.process( [] )
        expected = 0
        self.assertEqual( expected, actual )

    def test01Land(self):
        actual   = islands.process([
            "L"
        ])
        expected = 1
        self.assertEqual( expected, actual )

    def test01Cloud(self):
        actual   = islands.process([
            "C"
        ])
        expected = 0
        self.assertEqual( expected, actual )

    def test01(self):
        actual   = islands.process([
            "WCLWCLLLWCCWL"
        ])
        expected = 3
        self.assertEqual( expected, actual )

    def test02(self):
        actual   = islands.process([
            "CCCCC",
            "CCCCC",
            "CCCCC",
            "CCCCC"
        ])
        expected = 0
        self.assertEqual( expected, actual )

    def test03(self):
        actual   = islands.process([
            "LW",
            "CC",
            "WL"
        ])
        expected = 1 
        self.assertEqual( expected, actual )

    def test04(self):
        actual   = islands.process([
            "LL",
            "WC",
            "CC",
            "LL",
            "WW",
            "CC"
        ])
        expected = 1
        self.assertEqual( expected, actual )

    def test05(self):
        actual   = islands.process([
            "LL",
            "LW",
            "LC",
            "LL",
            "LW",
            "CW",
            "CW",
            "CL",
            "WC",
            "LC",
            "WC",
            "CL",
            "WC",
            "LL",
            "LL",
            "WW",
            "CW",
            "LC",
            "LC",
            "LL",
            "CL",
            "LW",
            "WC",
            "WC",
            "LC",
            "WL",
            "CL",
            "CL",
            "WC",
            "WC",
            "CL",
            "WW",
            "CL"
        ])
        expected = 4
        self.assertEqual( expected, actual )

    def test06(self):
        actual   = islands.process([
            "WWCCCLCCLWLWCLWLLCCC",
            "LWCLCWCWWCWCLWWLLWLW",
            "LLCWLWWWWWLCLWWLCWCW",
            "WCCWCWWLWCWWWWWLLCWW",
            "WWWCLCCLLLCWCCWWWLWL",
        ])
        expected = 5
        self.assertEqual( expected, actual )

    def test07(self):
        actual   = islands.process([
            "CCWLWCLLCLLCCLLCWLWWCW",
            "CWWCLWWLLWLCCCLLCCLWCL",
            "WWCWWCCLLCLCCWLLWWLWLW",
            "CWWWCWWWWCWLCWCLWCLWLL",
            "WCLWLCCWWLWCCWLLLLLLCL",
            "CLLCWCCWLWCWLCWWLLWLWC",
            "LLWLWWWCLLLCWLCWLWLLLC",
            "WLCLLLLLWLLCWLWWWLWLWC",
            "WCLCLCLWCLCLWWWWCWCWWC",
            "LLWWLLCLCWWLLLCCWLCWLC",
            "LCCWLCWWCCCCWCCLLCLCLC",
            "CLLCWLLCLCCWLLCWWLLLWW",
            "LCLCLLCWLWLWWWLCCWWLWW"
        ])
        expected = 4
        self.assertEqual( expected, actual )

    def test08(self):
        actual   = islands.process([
            "LCLWWW",
            "CCWLWW",
            "LWCWLL",
            "CCWLCL",
            "WCLLCC",
            "LWWCWL",
            "LLWCWW",
            "LWLCCC",
            "WLWLLL",
            "CCCCCC",
            "WCCWLL",
            "CCLLCL",
            "WLCLLC"
        ])
        expected = 3
        self.assertEqual( expected, actual )

    def test09(self):
        actual   = islands.process([
            "CLLC",
            "LLCL",
            "WLCL",
            "CLLW",
            "LWWL",
            "WWCL",
            "CCLL",
            "WCCW",
            "CWWC",
            "WWWL"
        ])
        expected = 3
        self.assertEqual( expected, actual )

    def test10(self):
        actual   = islands.process([
            "LWCCCLW",
            "WLWLCWW",
            "LCCWWLC",
            "LCLWWLL",
            "LWCWCWL",
            "LCCLWCC",
            "LCWLLWL",
            "CLCCWWL",
            "CLWLWWW",
            "CCWLLCW"
        ])
        expected = 4
        self.assertEqual( expected, actual )

    def test11(self):
        actual   = islands.process([
            "CCLWCW",
            "CLLWWL",
            "LCWLWL",
            "WWCWLW",
            "CWWCWW",
            "WCLWWL",
            "CLCLWW",
            "WWCLWC",
            "CLLCWL",
            "CCWWCW",
            "WWCWLL",
            "WWCWCC",
            "CLCCLC",
            "CCWWLW",
            "LCLLCW",
            "CCCLLC",
            "WCLCCL",
            "CLWLWW",
            "CCWLWW",
            "LWLWWL",
            "LCLWLC",
            "WCLCCC",
            "LWCLCL",
            "WLWCLW",
            "LCCCCC",
            "LCLCLW"
        ])
        expected = 9
        self.assertEqual( expected, actual )

    def test12(self):
        actual   = islands.process([
            "WWLLLCWCCCWCWC",
            "WWLWCLLWLWLLLW",
            "CCLLWWCCWCCCWC",
            "LLCCWWLLWCCWCC",
            "WWLCCWCCCWWWCL",
            "WWLWCCWWWCLLLL",
            "CCWWCCCCWCWCWC",
            "LWWWLCCLCWWLCL",
            "LWWWLWLCWCCCWL",
            "WLCWLLWWCCWWCW",
            "LCCLLWCLWWWCWL",
            "CLWWWLWWLWWWCL",
            "WCWLWCLLCCWLWL",
            "WWLWCLWWWLWWLC",
            "CCWLWWCCWWWLWW",
            "CWWWCCCCWLCCWW",
            "WCWWWCLLWCLCWW",
            "CCLWCLWCCWCWCC",
            "WLCWWLWCLWCCLW",
            "WWLLCLCLCCCCLL",
            "LWWWLLWWWWWWCL",
            "WLWLLCWCCLLWLC",
            "CCWCCLCWWLCWCW",
            "WCLLWLCCCLWCCC",
            "WWWWWWLCWCCWWC",
            "WLLLWCCLLWCCCC",
            "LLCWCLCCLWWWWW",
            "CWCCWCLLWLCCWC",
            "WLCWCLCCWCWCCW",
            "LLCLWCWCWCLLCL",
            "LWLLCLCWLLCWLW",
            "CWLWWLLCCCLLWC",
            "CCWCLLWWLCLLLL",
            "WWCLCLWWWCLWCC",
            "LWLCLWLWWCLLWL",
            "WLCCWCWLLLWWWW"
        ])
        expected = 16
        self.assertEqual( expected, actual )

    def test13(self):
        actual   = islands.process([
            "LWLWCWWWLWWCLCLWLWLLWCWCCWWLWLWWCLWLWC",
            "WCCCLLCCCLWCCCCLLCWLCCLWCWCLCWWLWCWLWL",
            "CCCLWLLLWWLWCWCWWCCWCWWLLCCWLCLWWCWCLL",
            "CWLWCLWLCWLCWLCWCLLCWLWCWCWCCWCWLCWCWW",
            "CCWLCCLWCLWLLCCWLCCLCLLWLWCLLCLWCLWCLW",
            "CCLLCLCWCLLWCWWLLCCLWCLCCLCWCLWCLCCCWW",
            "LWWLCCLCCLWCCWWCWCWCCCCLCLLCLWCCWCCLCL",
            "WLCWCLWCWCLLLLCWLWCCLCWLWCWWWCWLLLLLLW",
            "WCCCCLWLWCWWCWCWLWCCWWWWWCCLCLLLLLLCCW",
            "LCWLLLCLWLLWCWLLWLLLLWLWCCLCWCLLLCWWWC",
            "WWWCWLLWCLCWCCLLCWLWLWCCLWLCWCWWCCLCCL",
            "WWWLCCLLLCWWWWCLCLCCLLWWWCLLCLWWLWCLCC",
            "CCWCWWWCWCCLWCCWLCWCCWWCCLWCWCCCCCCLCC",
            "WLCLWLCLCWCWLLCLWLCLLWCWCWLWLWLLWCWWCL",
            "WWCWCLLLCLWCLWCLCLWWWLLLCCWCCLWCLWCLLC",
            "LCCLCLWWCWWLWCLCWCWLCCCCWWLWLCLCWLWLLW",
            "CWLLWLWWLCWWLLLLWLCLCCLWWCWWLLCWLLCWWC"
        ])
        expected = 9
        self.assertEqual( expected, actual )

    def test14(self):
        actual   = islands.process([
            "CLLLWLWCWWLLLCWCWCCCCLWCCLCLWWCWCCLWLCWWLLCLLWW",
            "LCCLWCCWLCLLWCLCLCWLCLWLCLWLLCCCCLCLCWCWCWCCLCL",
            "WLWWCWLLCLLLCLLCLWWCCCLCCWCLWLCCLWCWCWWWCCCLCLC",
            "WWWWWLCCLCLLCLCCCCLLCCLCWWCLLLLLLCCWCWLLLCWLLWC",
            "LCLLCLLLWLCCWCWLCCWLCLCCWCCWLCWCCWLLCLCWWCLLLCW",
            "WCCLLLWCCWCWLWWCLCWCLCCCLCWLLWCCLWLLCWCCCCWCWWW",
            "CLCCWCLWWWLLCWLWCCWWLLLLLWLCLWWWWWWCLLLCWWWCWCW",
            "LCLWLWCCLCLWCCLCWLLLWWCCCCCCLCCCCCCWWCLWWWWWWWL",
            "WWWCLWCCWLWCWLCLWCCCCCLLCWWCLLLLCLCWCLCLCLWLCCC",
            "CCWWWCLWCLLWWLCCWLCWLLWCCLCLWLWCLLWLLCLWCLCLCLC",
            "CWWCCWWWCCCLCWCCLCLWWWLCWLCLLCLWLLCCLLWWLLWCWCC",
            "LWLWLWLCCCCWWWCCLWWLWWWWCWWWWCLLWWCCCLLWWLLLWLL",
            "CCWCCCWCLWWCWLLCWLCCWWWCCCCLCWWWWWLLWLWCCLWCCWW",
            "LLWLWCCCLWWWLCCWCCLWLCCLLLCCLWWLLWCCLCCCCLCLCWW",
            "LLCCCLCCLCWLLLLCLWWCLLCLLLWCLCCLWCCLWCLWCWLWWLW",
            "LLCWWWWCWLLWLLCCWLLLLCCLCLWWLWWLCLLLWCWLCCWLWWL",
            "CCWCCCCLLCLCCWWLWLWCLCWCLCCCWCCCWWCWCLLWWLWWLWL"
        ])
        expected = 8
        self.assertEqual( expected, actual )

    def test15(self):
        actual   = islands.process([
            "LCCWWWLWLLWWCWWLC",
            "CLWCCCWWWLCCWCCCL",
            "LLWCWWCLLLCLCCLWC",
            "WLWLCCLCCCCCLWCLL",
            "LLLLCWCCWCCLLCCCC",
            "CCCLCWWLLCLWWWCWC",
            "LLCCLLWLWWCWLWWLC",
            "WLLLWWCLLCCWWLWLC",
            "WCWLCLWCLWLLWWLCW",
            "WCLWCLCCLCLWLCCCW",
            "CLLLWWWWLCLLWWLLC",
            "CWCWLWWWCWWLWWCWW",
            "WLCWLLCCLLLLCCWCC",
            "LLLCCCCCWCLCLLCLC",
            "LLLLCWCCWLWWCCWCC",
            "CLLWLWCLWCLWLLWCW",
            "WLWLWWCLCWWCLLLWW",
            "WLLCWLCWWCCCWWWCC",
            "LCCCWLLCWLCCLCLCC",
            "LWLLLWLWCLLCWLLLC",
            "LLWLLWWCWWCLLWCCC",
            "CLLLWLLCCLWLWCLCL",
            "CLLCWWLCLWCLLWWLC",
            "CCCLWWCWWCLCWCLLC",
            "LWWWLWLCCCCLLWCCC",
            "WLLWWLCLLCWWCWLCL",
            "WLLCWLCCLLLLCWLCC"
        ])
        expected = 6
        self.assertEqual( expected, actual )

    def test16(self):
        actual   = islands.process([
            "LWCLWWWCWWWCWLLCLCLCWCCCWCLWWCCCCWLCLLLCLCCLLWL",
            "CCCWLWLCWLWLWLWCCWCWWWLWLWCWWLLLCCCCLWWLLLWCLLC",
            "LWLWLCCWWLCLCLCWWWWCLLLLLWLCCLCLLWLCWCCLCLLWWCW",
            "LWWCWCCWWCWLLCLWCCWWWCLWCCCWWWCLWWWCCCCCLLWWWLC",
            "CCLCLCLWWCLLCWLCLCWCCCWCCLLWLLWLCCWLCWWLCLLCCCL",
            "CCCLCWWCWCLLCWCLLWLWLCWLLCLCLCWCWLCCCCWCCCCLCLL",
            "LCLCWLCLLLWWCCLCWWWCCCLWWCLLWCLWCCWWCCLWLLLWCCL",
            "CCLLLCWLCWWLCWWWCWCCWLWWCWLLWWWWLLWCLCLLCLWCLWL",
            "WCWLCLWWWLCWCWLWLCCWCCLCCCCWCWWLWLCCLLCWLCWCWCC",
            "CLCWWLWCWCWCCCLLLLLLWWWLLWWLLWWLCLCLCWWCCLLLWCL",
            "LLWCCWCWWLLLWCCLWCWCCCWWLLWCWWWWWCCCLWLWLLLWWLL",
            "LCWCLWLCWLWWWCCWWLLLCCWCWLLCLCWLLLWLWCLLCCWWLLC",
            "LLCWWWWCLWCLCWLLCWCLWLCCWLLWWLCLWCLCWCLWCCCCWLW",
            "LLLLWLLLLLWWCWLCWLWLWCWWLLWCCCCCLWCWLCLCCLWLLCL",
            "WWWCLWWWCLLCCCCLLWCCLWCWCWCCLWWWCWWWLWWWLLLLLLW",
            "LCLLCWLWLCLLWCCLWCLLCLCCWLLCCCWCLWLCWLCWWWWWWLL",
            "WCCWCLWWLWLCCWCWLWWLWCWWLWCCWLLLLCCCCLCCCWWWWCW",
            "CWWCLLWCWLLWWWLCCCCLWWLCLWCLLCWCWWWWCCCLWLLLLCW",
            "WWCLCCWWCWCCWWWWLLLLCLCWCCWCCCLLLLLWWWWCLLCWWCW",
            "CCCLWWLLCCLLLLLWWLWWLCCLWCCCCLCWCCLLCLCCCWWCWLL",
            "LWWLWLCCWCLCLWCLCWLWWLWCCLCCLWLWLCWCLCWWCCWCLLW",
            "WLCCCCLCCLWLWLLCLLCLLLLLWLCWCWCWWWCLWWLLLWWCWLW",
            "LLCLWWCCCCLCLLCWLLWLCWCCCCLCCLLCLWCCWLWLCCCWWWL",
            "CLWCCCCCLWLLWWWLLLCLLCWCCWWLWWWWCWWWCWWWCLLCWWL",
            "CWWLCCWLLLWLCLWWCCWCWWLWLWWWWLLLWCLLCCCLCWWLLWC",
            "LLCWWCWCWCLWWLLWLCCWLWWWLLLCCLWWWLWLLWWWCLWCCWW",
            "WWLWCCCWLLLCCLWCLCCWWLLLWCCWLCCCCCCCCCWLCCCWWCW",
            "CLLCCCCLCCLLWWWCLLLWLCCCWCLCLWLCLWCWLWLCLLCCLWW",
            "CCWWCCLWWWWLWLCCWCLWLCWCCWCLCLCCLCCLLCWCWLCLWWL",
            "CCWCWWWWLWLCWLCLCLCLCCLWCWWWWLLCWCWLLCWWWCCCCWW",
            "WLCWCLWLCLWWLWWCWWCLLLWCLWWLLLWCWCLWCLWLCCWCLCW",
            "CWLLLLWCLCWLLCCLWCWLLWCCCCWWLCWCWCLLLCLWCWLLWLC",
            "CWLCLWCWLLLCCWCCCWCWLLWCCLLWLCLWWLLCLCLLCLWWCCL",
            "LLCWLWWCCWWCWCLCCLLLWCCLLWLWLCWWWLWLCLCWCWCWCLC",
            "CLLLLLLCLWLLCLWLWLCCWWWLWWWCCWCWLLLWCLLLWCCLLWW",
            "WCLCCWWWCLLCLWCLWLLWWCCWCWCCCCWLWWCLWWWLCCWWLCW",
            "WLWWLWWCCWWWLLCWCWCCCCCLCCLWLCWWWWCCLLLWLWCLLWW"
        ])
        expected = 11
        self.assertEqual( expected, actual )

if __name__ == "__main__":
    unittest.main()

