"""
非常clever的二分法的应用。首先，有个前提条件是肯定的，那就是该序列一定有peak值得存在。分析如下，首先，如果该序列中存在先递增后递减的情况（整个序列是
没有单调性的），那么可有一个转折的峰值点；如果是先递减和递增，那么转折点虽然不是的，但最差情况下，左右两个端点是的，因为，题目告诉了nums[-1]和nums[n]
都是负无穷大。除此之外，如果序列是递增或递减的，那么两个端点之一肯定是一个peak。
接着，就是二分法的应用。首先，找到中点位置，并将中点位置与中点位置加一的值大小比较，如果大于，那么假设这个序列是单调的，后面的一段mid+1~right必定
有peak，因为最坏情况是单调的，如果事故递增，返回right，如果递减，返会mid+1。同样，如果小于，也是一样分析，这样就能很快找到peak。
"""
class Solution:
    def findPeakElement(self, nums):
        # 第二种
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[mid+1]:
                right=mid
            else:
                left = mid+1
        return left

        # 第一种解法
        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     if left == right:
        #         return left
        #     if right - left == 1:
        #         return left if nums[left] > nums[right] else right
        #     mid = (left + right) // 2
        #     if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        #         return mid
        #     if nums[mid+1] > nums[mid] > nums[mid-1]:
        #         left = mid+1
        #     else:
        #         right = mid-1


solve = Solution()
nums = [-9977,-9972,-9946,-9934,-9894,-9856,-9853,-9788,-9752,-9738,-9707,-9541,-9528,-9489,-9467,-9451,-9428,-9408,-9366,-9283,-9241,-9160,-9151,-9129,-9122,-9052,-9047,-9043,-9040,-9030,-8958,-8954,-8935,-8917,-8891,-8831,-8756,-8677,-8654,-8611,-8590,-8574,-8544,-8517,-8506,-8464,-8428,-8412,-8398,-8332,-8318,-8285,-8283,-8273,-8259,-8162,-8066,-8065,-8000,-7996,-7985,-7982,-7972,-7970,-7948,-7825,-7817,-7783,-7759,-7751,-7728,-7725,-7718,-7573,-7556,-7549,-7417,-7390,-7370,-7329,-7277,-7147,-7119,-7105,-7091,-7088,-7045,-7034,-6949,-6945,-6941,-6932,-6888,-6883,-6875,-6868,-6854,-6790,-6718,-6678,-6658,-6612,-6580,-6537,-6512,-6492,-6482,-6479,-6434,-6411,-6339,-6330,-6309,-6276,-6230,-6147,-6133,-6106,-6062,-5992,-5966,-5939,-5913,-5886,-5838,-5813,-5763,-5732,-5725,-5718,-5698,-5693,-5677,-5624,-5604,-5583,-5578,-5573,-5486,-5380,-5352,-5349,-5327,-5266,-5262,-5259,-5248,-5224,-5215,-5145,-5132,-5129,-5012,-4964,-4961,-4960,-4908,-4893,-4815,-4774,-4732,-4705,-4602,-4567,-4520,-4452,-4409,-4384,-4355,-4333,-4249,-4149,-4135,-4108,-4059,-4004,-3811,-3809,-3795,-3770,-3748,-3746,-3698,-3693,-3646,-3619,-3544,-3528,-3476,-3409,-3391,-3372,-3368,-3292,-3266,-3256,-3245,-3178,-3116,-3113,-2950,-2942,-2922,-2886,-2867,-2864,-2862,-2811,-2700,-2691,-2637,-2628,-2571,-2568,-2505,-2481,-2468,-2454,-2402,-2318,-2305,-2295,-2269,-2229,-2179,-2128,-2060,-2058,-2018,-1913,-1846,-1808,-1805,-1771,-1744,-1740,-1735,-1623,-1572,-1538,-1516,-1513,-1472,-1435,-1409,-1384,-1348,-1297,-1286,-1282,-1257,-1248,-1163,-1133,-1091,-1050,-997,-972,-957,-922,-921,-913,-832,-700,-663,-548,-528,-458,-446,-440,-413,-406,-394,-377,-368,-299,-175,-170,-92,-63,-8,114,143,144,145,203,296,315,320,380,440,453,460,524,561,564,570,578,589,612,652,661,696,715,743,744,773,797,814,834,859,894,964,1044,1061,1096,1218,1250,1306,1350,1386,1387,1427,1430,1442,1454,1520,1529,1540,1549,1559,1572,1593,1608,1627,1631,1673,1719,1725,1785,1820,1866,1888,1890,1911,1968,1987,2011,2034,2070,2084,2094,2119,2126,2158,2177,2208,2223,2295,2300,2316,2341,2385,2395,2412,2417,2436,2459,2523,2639,2662,2670,2757,2802,2815,2848,2856,2946,2977,3018,3056,3065,3086,3099,3166,3333,3438,3483,3517,3563,3568,3592,3615,3618,3622,3646,3647,3683,3705,3720,3742,3815,3870,3879,3923,3926,3936,4011,4037,4084,4105,4153,4213,4228,4242,4336,4337,4444,4461,4469,4491,4582,4629,4650,4800,4826,4867,4900,4932,4970,4983,5005,5090,5109,5124,5153,5218,5223,5249,5269,5334,5429,5447,5470,5521,5526,5530,5532,5533,5554,5562,5610,5613,5644,5724,5754,5778,5784,5803,5828,5876,5920,5938,5971,6008,6018,6026,6036,6142,6143,6172,6184,6232,6234,6284,6307,6375,6385,6452,6475,6511,6557,6562,6568,6569,6583,6594,6627,6636,6664,6707,6731,6738,6754,6781,6810,6911,6991,7017,7112,7125,7145,7245,7251,7264,7267,7330,7335,7382,7432,7441,7468,7498,7549,7570,7615,7672,7727,7764,7796,7799,7842,7843,7870,7916,7926,7950,7996,7998,8030,8033,8043,8064,8080,8115,8121,8154,8197,8235,8239,8334,8359,8368,8370,8394,8411,8424,8548,8549,8588,8668,8783,8785,8791,8803,8809,8841,8842,8891,8901,8931,8933,9059,9254,9268,9324,9330,9382,9427,9484,9526,9530,9669,9676,9716,9744,9758,9832,9926,9936,9969,9991,9920,9869,9814,9789,9615,9603,9565,9541,9524,9507,9470,9426,9385,9265,9217,9167,9154,9040,9000,8963,8951,8914,8784,8776,8766,8744,8742,8658,8651,8646,8613,8557,8550,8490,8450,8392,8324,8320,8305,8124,8114,8013,7969,7947,7905,7896,7881,7869,7851,7719,7661,7605,7445,7412,7402,7328,7320,7318,7195,7114,7082,7057,7055,7018,7000,6950,6948,6817,6765,6753,6751,6732,6701,6658,6643,6637,6580,6410,6361,6336,6325,6236,6177,6157,5987,5939,5889,5859,5788,5733,5709,5707,5704,5698,5693,5690,5656,5576,5575,5569,5490,5481,5421,5300,5186,5112,5026,4964,4782,4754,4683,4677,4535,4521,4493,4475,4323,4283,4238,4221,4217,4169,4111,4090,3978,3970,3950,3944,3940,3896,3869,3868,3852,3795,3785,3721,3691,3681,3677,3653,3591,3583,3540,3526,3450,3426,3421,3387,3369,3345,3322,3096,3078,3053,3012,2952,2923,2918,2917,2842,2770,2741,2738,2568,2556,2460,2441,2317,2265,2230,2197,2079,2060,1962,1943,1900,1809,1652,1647,1522,1432,1401,1397,1389,1275,1266,1144,1095,1087,1081,1079,1057,1014,960,910,748,686,644,632,488,328,218,205,163,136,59,29,-166,-209,-365,-373,-385,-414,-419,-470,-487,-607,-777,-778,-784,-800,-825,-843,-864,-909,-975,-1131,-1154,-1211,-1229,-1233,-1347,-1365,-1380,-1417,-1640,-1692,-1715,-1719,-1782,-1838,-2022,-2039,-2053,-2081,-2141,-2205,-2224,-2300,-2338,-2485,-2535,-2572,-2592,-2598,-2604,-2610,-2747,-2826,-2907,-2947,-3049,-3083,-3124,-3136,-3138,-3175,-3218,-3219,-3242,-3264,-3286,-3311,-3335,-3401,-3439,-3455,-3480,-3486,-3502,-3509,-3515,-3601,-3716,-3775,-3785,-3898,-3954,-3993,-4050,-4069,-4111,-4134,-4227,-4264,-4287,-4295,-4389,-4419,-4495,-4507,-4556,-4561,-4566,-4675,-4724,-4804,-4834,-4835,-4839,-4858,-4862,-4894,-5015,-5030,-5031,-5264,-5344,-5357,-5407,-5480,-5492,-5512,-5696,-5733,-5788,-5852,-5855,-5861,-5871,-5881,-5920,-6024,-6058,-6072,-6082,-6181,-6219,-6275,-6373,-6386,-6408,-6436,-6444,-6534,-6542,-6551,-6652,-6750,-6845,-6886,-6907,-6961,-6993,-7002,-7020,-7021,-7189,-7206,-7212,-7219,-7297,-7317,-7438,-7471,-7504,-7520,-7628,-7681,-7748,-7854,-7873,-7928,-7959,-8020,-8076,-8115,-8119,-8120,-8127,-8137,-8183,-8192,-8303,-8313,-8322,-8361,-8373,-8377,-8426,-8449,-8545,-8595,-8669,-8695,-8701,-8703,-8930,-8939,-8953,-9101,-9116,-9219,-9238,-9291,-9331,-9345,-9383,-9392,-9427,-9444,-9543,-9622,-9696,-9746,-9755,-9770,-9828]
print(solve.findPeakElement(nums))
print(nums[580:583])