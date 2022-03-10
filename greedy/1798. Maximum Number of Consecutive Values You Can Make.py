from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        sorted_coins = sorted(coins)
        till_num = 1
        if sorted_coins[0] != 1:
            return 0
        for i in range(1, len(sorted_coins)):
            max_num = till_num + sorted_coins[i]
            if sorted_coins[i] == 1:
                till_num = max_num
            else:
                if sorted_coins[i] <= till_num:
                    till_num = max_num
                else:
                    for j in range(till_num+1, max_num):
                        if 0 <= j - sorted_coins[i] <= till_num:
                            continue
                        else:
                            return j
                    till_num = max_num
        return till_num+1


if __name__ == '__main__':
    print(Solution().getMaximumConsecutive([5521,1,8796,5541,8266,5361,6139,2089,1564,4746,1,8485,1,1,8816,7065,1,599,1,1,6207,4739,1,1,4236,1,688,1,1,950,1,1,1,3398,4690,1,1,2884,1,2030,1,2683,1,1,1,1,1,4463,452,5718,5181,1,9798,1,4508,1,7161,6442,9268,1,7243,1,798,4508,1,7308,5491,3475,7709,4265,1,1786,3593,1,3927,1,8253,9335,9586,1,27,3913,7417,6703,2403,1,1,1,8512,4822,7384,8483,1,1,1058,6172,414,1,1,1,2728,6631,317,1,7422,5325,1,1,3452,9941,7015,1,1,1,1,1,1,1,1,1,1,1,5608,1,6973,2868,1,667,9560,1,1,1,2761,1,1,1955,1895,1,1,7097,2617,6461,5747,1,4619,1,1,1,1,1,8517,1,2373,2811,8355,7992,1,1,1469,1258,2975,3885,1,1,7255,6535,1,4476,992,1,1,1,1,1,1,1,1,1,1,1,1,3085,5598,1,1115,1,9374,8203,6982,1,1,1,6194,9916,7918,6554,6026,1,1,1,1,3112,3656,799,1006,1,5445,4441,1,5291,5944,1,1,1291,1,1,2463,1,9657,1,7272,1,1,9788,1,1,6229,1,4006,1,1,3148,1113,1,1,1,1,1,1,8363,6491,1562,1,1,168,1,1,4972,26,1862,1,237,6919,9767,1,1,4727,2447,1,1,2102,4714,1,1,1,1,9549,1,1,1,6535,6296,1,1,6118,1,6558,1,8101,5174,1276,4358,1,4436,1,5752,1,9553,2278,1,4343,9037,1,1,1,1,1,1,2811,1,7728,1908,191,1,1,7572,8089,1,1,1,1,5967,1,5639,5839,3036,1,1,5081,4881,8335,5938,8802,1,1,1,1,8971,1,1608,7732,1,5279,1,7767,2908,1,7847,685,3426,1,1801,9214,1,1,1,7569,4767,1,1,889,3448,1,1,302,1,2607,1,2037,7824,1,4593,8948,7287,1,3133,1,1931,1,1,1,3464,1,1,1,1,3101,1,2166,1,3740,1,3840,1,1,6217,1,1,1,1,2637,4943,74,4444,1,1,1,8288,1,3568,5049,8808,9839,3797,1391,1,2908,1,1396,4890,1,1,1840,5965,443,303,1,1,9370,1,1,9456,3533,5546,6010,1,1,727,1,141,1,1,1,1,1,1,4118,7657,7036,1,1,8348,2799,1,1,1,1,1,2297,4945,1,9781,1,1,3385,466,4683,4652,1,1,4873,6783,1,3925,1,230,1,1,1,1,1,1818,1,1,8346,1,9159,4860,7940,1,7603,1,1619,1,1,4992,388,1711,1,5404,2069,8213,1,7455,1,9943,1,4935,6379,3071,1,5599,8219,1,8984,1,1,6109,1,5109,1,1843,1,1,1,1,1,1,3424,1,1075,9746,1,4130,3688,9908,1,7538,1,1657,1,194,1,2894,3186,2321,1832,2182,6189,9224,1,2393,1,1,1,9192,1324,716,1,1,1,6046,1,1,1,5665,1,1808,1,1,3217,2652,5886,1288,1,1,2239,1,1,8660,1185,1829,1,1,343,2668,8327,1,1,1,1,32,395,1,1,1,1,6640,693,1,5074,4747,4034,7063,9957,931,1,1,5933,1,6431,1,7134,7129,1,1,1,1,1,5619,4133,2641,347,1,2664,1,1,9870,1,7648,1,1,751,4834,1,1,3915,5160,1,1473,1017,1731,1,1,1,1,657,4355,8719,1,3239,2314,1,8076,9547,1292,1,1458,3250,1,1,1,1,1,1,5043,9317,1,1,1,1,6628,2849,1,1,8996,1,1,5023,8990,2936,1,9122,9754,1557,1,7605,7793,5835,1,1,2560,1,1,8157,1,1,1,3468,5862,6953,1,9125,1,1,2736,1,1,6086,1094,9814,1,1,1,1,1,1,7720,2186,1,1,1,1402,5550,1,715,1,2954,6467,1,1,4958,6405,1834,1,1,2726,1,1,1878,1,1,5554,9165,1262,6073,1,1,6907,1,1,4637,5455,1,6503,1,5671,2668,3070,8586,1,4022,8306,9044,1,9802,1,1,2760,7349,1,1,7848,3020,7494,1,6956,1,7215,1,1,1,2088,6808,8633,1,4209,1,1,1,5698,1,7646,5339,1,2089,8130,1,1,1,1,1,4946,5397,6401,1,38,1,7418,493,1,4250,1,1,4803,1,9536,3081,8482,1,1,1,1,9919,1,6286,4640,1,1,1,4600,1904,9744,1,1940,4637,5324,1,1,5113,1,1,1,1,4887,1,1,2339,1581,1680,1,1,581,1,5024,9435,1011,6385,4919,3148,5996,7460,1,1,671,1,9787,4486,123,1,4092,3650,1,1,1,1,9171,1,1,657,1,1,1,1,1,1,1,1,1,2411,1,2854,1,1,1,5614,8147,1,1557,1,1,9024,7132,3212,1,1876,1,2275,1,2262,1,1,1,1,740,1,1,1,1,1,8042,6622,1,1,1,9406,1,1,2984,1,5395,1,6082,1,2295,1,3721,5006,9451,1,1,2993,1,1,1,8878,3628,3970,1,1,1,5306,6300,1,4180,2815,4652,3263,3353,1,5739,1,1,8844,1,4148,1,6020,1,9561,1,6235,1,8638,231,9638,1,1,1,1,1,1,8206,541,1067,1,6505,429,1,8301,2700,5649,4443,4716,9098,6634,1,4621,8758,1911,5797,3360,1,1,1,1,9977,7907,1,1,6786,1,1,9887,1,1,7943,1,1,3375,1,1,1,1,6054,6529,8514,1646,2427,4281,1,3861,1,1,8578,1,1,4821,57,5745,3689,4555,6716,5931,1,1,1,8527,1,1,1974,6714,5608,1,1,863,4733,1,1,3609,2062,1,1,5966,2672,1,1,1,766,1,4961,1,1,1,1739,1,1,1,3140,1,1714,8182,1,1,1,1,4397,6501,517,1,3221,1,413,765,4604,115,1,1,1,5679,9218,1,1,5375,1,2603,10000,13,9799,9903,1,1,1,1,1,1,1,848,5826,3986,1,1033,4696,1,1,2814,1,1,6523,5540,7590,1437,1,3111,2624,6181,8224,529,7286,1,7981,985,1,6572,1684,1,1,1402,8184,9670,1,1,1,4708,1,1,1,1,1,1,5135,1,1,1363,8681,1,4047,1371,4277,6922,1,1,6450,1,4951,2590,1,1566,4865,1,1,4736,1,687,9632,1,9452,1300,2761,1,1,1,6385,1,1,1,1,6568,1,6604,1,6140,1,2146,110,4450,1390,1,1,7107,2517,1,1,1,5816,1067,1,1,5258,4271,7341,1653,7806,199,1,1,9775,1,1,8764,1577,1,3613,1,1,9914,1,7245,1,1,1,31,6812,8499,5095,6198,1,5334,1,1,1080,9477,1,1,4610,416,9058,4125,4994,5464,2188,7238,7299,1,1,1,3497,4942,8394,4629,9931,6033,1,1,3443,1,1,4285,3576,1,1518,2453,1,3979,1,5687,6253,5299,5211,1,1,2714,1,8713,6367,6989,9439,1,1,1,2950,1,1,4433,1,1,1,8176,5178,3333,1,1639,1,8475,1,143,1,1,1,1,1092,1,379,3519,5346,3460,1955,954,1,1539,1,4458,1,1,1,7923,2014,1,3138,7062,1,3747,1,1,5863,1,1,1,7446,8682,3450,4037,9251,7224,1,1,7566,6592,1,1,1,2070,7675,1,1,1,7063,1,13,271,1,3473,6938,1,1,1,1,1,9592,1,5585,1,6011,599,7433,2688,9949,4152,3544,6617,1,1,1,1,1,1,7935,8788,1,2801,7417,1,1,1,1,1,1,1931,1,1,9809,8485,5900,3607,9818,1,565,1,1,1,1616,1,1,8831,3137,1,1,1954,1569,1,1,326,5917,2497,1,1,9332,1,5649,1729,1,1,1742,1,3519,1,6408,8372,1,1,1,1,1,1478,1,9123,1,3576,6030,8523,3229,7229,1,1,1,1,1,7558,2941,6635,3324,1,1,2142,1,9845,7832,1,8038,7617,3991,7780,4170,8008,309,1,1,6837,1,1,1,2420,9261,3119,1,1976,3972,1797,6412,3866,1,1,896,1,5177,1123,6954,5286,1,484,1,6684,1,1,8679,2734,1,1,1,1,25,4203,1,1,2088,2013,5836,461,5194,1,8149,1,856,8839,1,9655,5626,5973,1,1,8620,1,1,3419,6319,1484,7879,1582,1,1,4695,925,1,3418,1,5140,3059,1,6086,7877,3841,1,1,1,4455,1,1,1,5708,1,9839,1,1,1,1,8344,8057,1,1,1276,4667,1,2531,6564,1,1,1,1,1,1,6574,6205,1,7228,1108,1,1,3174,1,904,6840,2492,1,6113,1,8789,1,1,1,1,422,4605,1958,1,1,251,1,2712,6352,1,6840,4164,1,5200,4276,1,302,6194,1,1,5378,1,1,1,5975,1,1251,1,1,1,9381,3610,1206,572,3891,312,3620,1,1,1,1,1,3976,4216,3500,1,1,1,6752,1,1,1,3455,1,1,1,5122,1,5230,2782,1,1,488,2943,1,1,1,366,243,1,6335,6325,7298,1,1,6720,8703,4364,1,1,3342,1,3626,1,3315,647,6017,1,3123,9974,1,1,5194,1,2662,6644,1,2899,1735,8653,2012,1,1,1,7023,4628,7298,1,1,1,1,1,2079,1839,1,1,5003,1,5600,1,425,1,8355,1,4752,1743,9343,8594,1,8818,8047,1,351,1,1481,1,1,3462,7861,661,1,2858,1,1482,7119,9012,4934,4269,1938,1,3928,1,6580,1,1,1,1,5613,1,1006,3399,1,8865,1,1,1,1,1,5351,2879,1029,1,7077,1,1,5751,1,8172,1618,1,5538,6401,2123,6721,1,1,6539,1096,7948,7826,1,2946,1106,1545,1,1,867,1,1,2473,8807,2627,1,1,1,1,9053,5247,2200,1,4348,4739,1,5650,1,9823,1,1,1,5772,1,1,8161,4805,9912,1,1,1,116,6706,4999,9357,7906,9947,2357,3296,1,1,1,1,1,4881,1,8022,9813,1,1677,7495,5069,1,1,8230,6030,9377,2014,2955,4891,8285,7698,1,1,4902,1,6077,1,1,7974,1,1,382,9170,1,1,1,1,7755,1,1,9994,1,3258,1,2068,550,1,7611,1,1,1622,1,1,1,9055,1,5101,1,1,1,2173,4959,1,1,9235,1,8259,1,1,1109,1,1,1,3312,1,1776,8490,1921,1,5781,1,5087,6870,1,8145,8621,5072,1,1,1,359,1,5650,1,1799,1,1,1894,1,1992,1,1,1,1,1,1,1,1,1,1,1,9716,1,1799,1,1,1,1,8691,1,1214,1,1,1,1,8494,4222,9739,1,1,1820,1,6419,1,5451,1,9412,1,6970,2882,5711,6590,1,1,1,1,1,8218,1,7489,1062,1,1,9381,2251,1,795,1,1,1,1,1,1,4959,1,1,1,1,3873,1,1,1,4589,4036,1329,1,8899,9902,6145,1,1666,9045,1,1,8499,4162,1,6743,1,980,1,8070,1,4536,1,7560,1,329,6343,5633,1,1,5540,9882,7550,1,3956,4560,1,1,2083,1,1,1,1,1,6521,1,9483,1,7695,1,1,5159,1,7519,8501,8642,2250,4204,4861,5181,4025,4266,1,9544,1281,7450,9854,8186,1,65,1,964,1,1,1,9190,3818,1,7133,6441,1994,5509,2624,1,1,1258,1,1,8458,1,1,2396,1,132,4272,426,7787,2251,1,1,5926,1,1451,4802,1,1481,6920,8353,1809,3282,9127,1,1,6220,9214,7757,566,1,8800,1,1,5119,7573,2673,1,7151,6473,1,9916,4451,1368,1,1,1,1,1,1,1,1263,4433,8771,16,573,26,1,6645,1,4045,5093,1,6187,7398,7492,1195,1,9152,2523,2947,1,2757,7934,7429,8344,1,1,1,8998,4998,1,1,4783,9458,2395,8362,4405,1,1887,1,1435,7260,1851,1496,7473,3188,1,1,6711,1490,8056,1393,1,4077,3451,6647,1,1,1,1,1,3692,1,9942,634,1,1,536,361,1,949,1,2577,1,1,1,1,3906,1,1,1,1,1,9622,1,4281,1,8624,4095,1680,1,1,1,2062,1,5725,9834,1,1,1,1,1565,881,4814,1,2857,8254,1,4332,1,1,3154,1,1,9934,4576,4909,1,9247,8103,1,1,1514,8980,8010,1006,1,1226,6898,7504,9724,1,8873,1,1,1,4664,1,1,1,1538,1,1,8098,1,1,6738,1,4700,1,1,4380,3606,5021,5207,8088,1,1,1,1,1,3902,528,7160,1,1,1687,1,1,1,1,1,1,2802,2259,2455,1,863,1,1,5048,1,485,9233,1,1,5548,1,1,3471,1312,8902,1,1,8054,1,1,5226,1,1,1,1,5228,1,1,7916,7828,1,1,6978,861,9922,1,1,1,1,5787,6308,5720,620,1,2807,7264,9849,2908,1,1,6616,6223,1,2182,1,5001,1,8942,1,2981,2543,6568,1125,732,8518,1856,2529,9323,3222,1,435,3555,7299,2936,4957,1,3050,4237,1,1,3554,2603,221,4963,2989,8491,8955,1,1,1,9079,5882,667,1,1,3924,1,1956,1,1,3606,1,6180,1,3717,6170,1,1,7257,1,1,901,1,1816,1,1253,1,1,8345,8750,5935,1,1,1,1,1,1,1,1,2654,8685,1938,1,9660,3567,1,1,1,6527,5572,9939,5016,1,1,5314,6933,200,2017,4167,1,1,1,1,1,1,1,1,1,2783,1,1,1,1,1,1,645,4524,1,3807,3928,2990,6258,1,1,1,2215,1,1,7002,8029,6442,8320,1359,1,1,8359,1,8359,1,1,8880,3822,1,3387,1,6240,1,1,7093,8077,6773,885,3416,3874,1,2120,1,1,1,913,1,1,22,8515,3345,1,1,1,9640,1,346,6779,1,9944,2509,1,1676,5314,1,7271,6798,1,1,1,252,3208,2554,7817,6113,4143,6933,1,1,9428,4273,1,7475,4165,1600,7631,1,2491,5603,1,1,1,1,9077,1,1,9104,1,1,1,9849,1,1,1,1,1,1,1,1,6114,1,4062,2101,1,7917,1262,9256,7039,4021,1,9068,7467,1,1,1,4310,5190,1,1,546,1,1,3147,1,8657,9838,4562,4718,1,1,7828,1,1,7816,1,1,1,6020,1,1,1,1,1,5051,1,1,4707,1,1985,3376,4593,1,71,1,979,9123,1,7370,1692,7227,2210,7833,8484,3719,1,9837,5899,845,1,1,1,1,9910,1,1,1512,1,1,3143,3374,1,1647,1,1,1,6187,864,398,4167,1,1,9793,5042,1860,1,5926,1,1,9441,1,1,2495,1,1315,857,6318,5248,1,3178,1,929,1361,1,2447,1,1,1,2783,1,6866,5640,1,526,3083,62,7579,1,1,8400,1,4123,8009,1,1,1,6609,1,7537,1,1,9559,1,7195,9061,2621,1,1,1,1,5631,7744,6088,4773,1,1703,1358,1,44,1,1,1,9108,4530,1,1880,2518,1,1,1,1,1150,2494,164,1,1,1,1,2561,3060,5126,5482,1,3052,7158,1,1,1,5988,4869,7999,1,1,1,1,1,1,1,1,1,1,8767,6128,1,2693,4972,9193,9930,1,1026,3420,1,1,1,7472,1,1,3047,1,1,4493,4589,1,1167,9518,7631,7087,1,1,1,9777,1,8322,1,1,6851,7348,1,3881,6479,1,1,1,1,1,1,1,5038,1,1,2366,6254,7454,1,1,7066,1,1,1,3883,1,1,7392,2350,5125,1,6413,1,6400,2929,4226,1,7239,1,1,3473,1,1,4939,1,1022,1,6685,3721,1,6752,9594,1,1,9291,5776,1,1,1,5670,4515,1,1,1,1082,536,1,1,1,6001,5055,1,7209,1,1,1,1,2451,1,1,4436,1,1,8995,6483,503,1,6453,1,3854,1,1,1,1570,1,1,3118,1,1866,1,8774,1,1,5062,1,1,1,9536,1,1171,1,9564,1,5427,1,1,1,1,1,6365,9077,1,2755,3389,7413,1,5656,2659,1,1,1,1,484,6245,9485,1,1,1,701,4182,2046,1,1,1,8561,9541,1,6342,5383,1,6840,1,3824,2783,1,7509,1,3506,1,1,7303,1,1,9848,397,2105,697,1,1,6193,1,1,1,1,1139,1,6734,9190,6809,1,1,1,3898,1,4336,6797,6033,1,7389,314,1,1,6979,1,1,7247,1,4040,1,1,8819,9526,1690,1,5376,7464,1,3633,1,963,1,8574,2223,1,9905,1,8958,7704,1,1,1,3191,6350,8602,8824,1,1,4929,1195,3364,7136,694,8884,625,6226,5929,1,3213,1138,1,1,7,4409,1,1058,1,3743,3689,6315,1,1,9115,4312,1,3412,6100,5890,1,1,1,1,1,9442,9834,2995,6861,1,1,1,1,1,1,6024,1,1,6641,1,9686,8540,1,1,3957,1,1,3145,1,2669,1,1,1,1,1,1,1,790,1,3547,1,3145,1,5606,1,2864,7661,215,8982,3522,5776,408,6119,1,4177,6137,1,1,1,1,6681,6906,1,1,1,4817,839,9991,1,8356,4152,9005,1770,9114,1,1460,1,1,2037,1,627,6417,308,9652,8969,8503,1,1796,1,4357,1695,1,1,8119,976,9763,1,3645,1,1,1,7244,3558,6957,6164,2595,1,1,1,5592,5679,4396,4828,1,1,6701,1,1,1,2503,8030,9707,1,1,1,1,1,1739,4253,2585,1,8035,1,7533,1,1,1,1,1,1956,1,1,1,528,6068,1962,1,6945,4354,1,3620,2913,1,1,1,1,1,1,6493,7932,5233,1,4510,1,1,1,8777,1,12,6142,1,2192,1,3356,8440,1,1,1,2623,6484,1,1,1,6733,1,1,1,9936,1,1,1,1,2305,391,1,4419,2379,6994,8639,1,165,1,1,1,1,1,9562,1,1,1724,1,1,1,1,8724,4117,1,1,3837,5739,1,9971,1,1,1,2225,6217,9004,1,5771,4334,1,6398,1,7468,3394,653,9517,9359,3218,653,7376,1105,6691,8957,1,1530,1,7034,7901,8373,1,5981,1,1513,1,1,1,240,8546,5873,1,7998,1138,1,1,1606,9197,1,7360,2851,1,1,1,7689,1,6971,4762,8332,1,1,1,1,7248,9927,400,5708,1,5581,2992,6349,1,1,9640,1,1217,1,1,1,4109,1,1,1,8430,5007,1,1,1,1,1,1,1,9315,184,270,7991,1,476,1,6818,6107,1,786,4808,3520,8549,1,1,4715,1,8937,7495,1,1,1,9752,4851,9988,2467,1,7354,3382,1,3230,7688,1,1,1,1,6242,3178,1,4299,2877,1,1,7074,4649,8224,7255,1,1,1,1,1,1,4944,1982,3854,1,7436,1,1,1,1,7510,9526,1,1,1,8380,1,7257,1,7422,3390,1,6706,1,1,402,3336,1,1,59,1,6090,1,1,1,1,1902,5772,6109,1,4961,1,1,517,1,9524,3990,6875,1,1,1,4946,1,1,1,1,1,3335,4546,3589,1,1,1,1,8135,9367,5780,1894,1,1,1,9083,1,5996,4771,1,1,5596,926,1,6448,978,9902,1,1,7641,9031,1,9761,1,1,6947,3989,2240,1,7382,7799,6313,7607,1,8398,3384,1203,1,1,1,1,1,3223,1,7688,1,1169,881,1,1,6027,9894,1,1,1,4710,1,1,1,1,6063,9221,358,1,1,1,635,1,2700,1,1762,3127,5993,1,8578,8613,4850,1,28,1,1,7637,6261,6137,9534,1,1,1,2298,3167,3639,7125,5895,623,1,5398,1,8965,1,4699,1,1,1,2368,1,5926,2979,1,1,9986,1,1463,8381,1,8072,1,1,4575,1,6753,1,5799,1,1025,1,6945,6254,1,1,1,1689,1,1,1,9136,1,2423,6130,1,1668,1,1,1,1,1738,1,1,1,1,2677,1,4855,9593,1221,1,1,8172,1,1714,1,1,4652,9187,1,1,1,1142,5385,2589,1,1,7066,4766,4050,1,1,5583,1,2061,1,6105,3794,1,1,3091,1,1635,1,1,1,1,7395,2511,1,1,1,1,9032,9905,1,1,1,1,1,1,8480,1,5377,1,1,7645,1,1,4903,9455,4412,1,1,2903,6654,1,3930,1,1,7356,7629,1,4964,5,1,3913,570,1,1,1,1,1,1227,9782,1,7994,1,8699,1,1,1982,1,8286,1,1,1,1467,2608,5414,1,1,1,4608,1,2856,1,963,503,6591,1,1,880,8810,8353,7678,1,1,1,8942,1,3298,9826,7925,1,1,226,2391,1,6901,205,6607,9136,5514,1,1,1486,1,3559,4522,1,4663,1,1,8531,1,4736,3783,8685,9392,2275,4042,7173,7461,8320,8803,5354,1,5342,8180,6275,7129,1,8245,5400,1,1,1,7362,1,1,6066,4497,1,1,1,3587,1,7583,1,1,5445,8859,1,1,1,1,1,1,1,6190,1,8115,76,1,1,1,1698,1,1,1,7826,1256,1,1,3222,1,1,5782,8363,4866,3174,1,3575,1,1,8946,2204,6510,1,1,6786,1,4828,2297,3785,1,1,9412,3705,1,1,4084,2077,9560,1,6400,1,1,1,9943,9335,4847,4028,1,4437,1,4277,7926,1,1,1,3312,3258,1767,6682,1,1,7596,1,1,1,1,1,1348,500,8266,2619,3596,2450,2474,2911,1,1702,1,1169,1,5803,9697,1,1,829,1,1,1,9188,1573,1762,166,1,1,2728,9167,1,2123,1,1,1,1,847,7294,4530,5527,1,8314,811,1,1,1,1,7190,1,7308,1,1,5179,1,3013,8614,1,3422,2757,1717,1,1,1,1,4531,5664,1,7381,8386,1822,1,4425,9246,569,8588,3577,1,217,6219,6374,771,2562,1,1,1,1,9094,7443,4616,8377,3771,1,3860,1,1,6343,1,2481,1,1,3436,1,1,1,1,1801,454,6804,1,1,1,1,1,1,1,1,1,4797,1,6949,8976,1,1,1,7763,1,1,8060,2649,5120,1590,1,1,3876,2977,1,5386,1,1,2922,1,1,5669,1,4846,6303,9425,1,5408,1,2036,1,1,1,1,3581,1,1,1,1,2526,1,1,2516,1,8869,1,8593,1,1,4712,8761,1,7468,1,4302,1,5806,1,871,1,4008,2580,1,3664,1,5614,3215,8722,1,9266,1,7243,1,1,1,1,1,1953,1,3219,9407,1,1,5063,1,3728,1,1,1475,1499,1,1,1,6160,2867,1,8983,1,4737,2071,9441,1,6678,8812,781,1,1,5267,5209,1,1645,1,1,3601,1,1,6165,1,1,796,1,1309,618,1,1,1,4962,1,1,6421,1,1230,8675,1,3150,1,1,1,1,6298,4404,8130,1,1,160,1,2746,4527,1,7546,1,936,653,1,8701,1,9256,1,1374,1,1,5749,2618,7391,4642,1,1737,1,1,1,3061,5457,1,1805,4781,1,1,1404,3173,1,3639,1272,933,1,1372,1,1,8264,1,1,588,1,979,8987,1,1,1,1,3227,5039,6545,1,1,1,1,6982,2244,1,1,1,1,1,1,1,1,5030,8473,5800,1,1,3105,1,4842,1,8684,3161,1475,9712,1,1,5445,1,1,1,1,1883,1,2779,1,7,1,4927,2189,1,1,4720,1,3251,9202,1,9620,1,8840,1,1,1,1,9646,3168,6694,7315,1,1,1,1,4720,1,1,1,7276,1,7174,5365,4208,1,1,1,1,1,1,1,1,1,1,1,1,1,655,1,1,1,5989,4944,1,1,4936,1,1,9907,1,6482,1702,1,1,1,1,1,5680,4583,9188,2393,9715,4666,1,1,1,1,1,8039,1,7757,1,1,1,6541,1,5013,309,1354,1,3032,1,9901,1,3756,2738,1,1,1,1,1,1,1,1,5866,1,1,1,887,2250,1,1,3788,1,2766,2706,1,4564,8488,1,4329,2256,2548,1,7877,5874,1,6399,1578,9159,8645,1,1,799,8497,1,1,6412,1,1,1,5133,8002,1,1,4005,2235,1,1,9192,1,1,4880,1,1,664,1,1,7099,632,1,9438,3578,1,1,4146,3619,1,6822,7934,3341,1,7861,1,5641,1,3002,1,1,1,9121,1,1,1,4149,1,1,7180,8687,8406,2809,4869,1824,1,1,6329,5314,2302,1,3085,6360,2349,6240,3847,1,1,1,1,1,1,1,1,1,7116,2168,2403,1,1,1,9075,4706,1963,1,1,6402,1,2399,5512,4504,702,1997,1,1,1,1,629,1,8530,650,1,6330,1,1,8120,1,1119,1,1,1,9320,5059,8879,1,1,1,8273,8863,6961,1,8132,2008,1,2142,3309,1,1,1,1,779,5727,6190,1876,1,6651,1,1,1,1726,2990,1338,1,1,1,1,1,6170,1,1,1,1,8814,6701,1,7022,4000,1,237,1,6928,2049,1,6736,1,231,3919,1,1,880,1,9633,1,4600,1,1,1,1,1,1,1,1764,9796,7583,1607,1,1,1,1,1511,3059,2939,1,250,1,1,1,3310,1752,1,1,1,6825,1,7361,1,5714,1,1,7334,3893,7219,6265,1,9565,6545,2012,1,1,1,435,1,9604,5038,1,2211,751,610,1,1,1,1931,1533,1,1,6729,1,1141,8240,1,2281,1,1,4215,5082,8527,8888,1309,1,2501,2148,1,1,5661,1,1,780,1,1,1,5572,8748,1,1,1,1,4008,4307,3198,3139,1,5495,9486,1,5652,5348,1,6920,8765,2356,5087,1,5886,3801,1,1,5587,8328,9466,1,1,2091,8155,1,2164,1,1,1,1,9886,1,1964,9890,5521,1,1,3478,7340,7382,1,5179,718,3407,1,3616,697,4047,1,1,6422,3525,4477,5084,1,1,1,1,1,1,7656,1,1389,6541,1,1,5124,1,1,4989,1,8540,8629,4658,1,1,4282,1,8946,1,4258,382,1,1746,5792,3268,4535,1,1,1,6357,1,9231,1,6941,7924,310,1,1,1,7875,7065,7335,1,1316,1684,1,1,9930,5393,3823,1,1,1,490,3088,61,7553,516,1,4817,1,1,4082,9367,1,8714,1,3244,8271,3471,9533,2877,1,9236,1,1099,3913,1,1002,1,6335,3194,9242,1,1,3717,9667,5600,1,7309,1,682,1,1,2721,1,4093,1,2061,1,1,9985,7310,2362,1,1,4482,1,1,9832,7057,1,1,1,1,1,3579,5489,2096,1,144,2683,1,2087,1,6230,1,1,1,1,3013,8909,6886,1,1,1,1,1,1,7094,493,1,1,1,1,1926,9008,943,9266,1,1,1,1,2821,244,1,9227,6661,5021,1,2133,1,3474,1,1481,1,7805,1268,2404,6834,1,4810,9468,9580,807,1,1,1,5257,9015,1,9334,2902,6503,863,4465,1,1,1,691,9990,1,1,4671,1,1,1,1,8237,7971,6967,1,1,1,1,1,5098,1,1,3573,8876,1957,1,3575,1,1,1,1,1,9167,3566,8740,1,1,2683,1,6818,1,4253,1,1,6944,1,1,2810,4282,7868,7823,7871,1,1,1277,1,1,6903,1,1,1,3486,1,1571,1,5540,7514,1,1,1,9347,1,1,881,9456,1,1956,9476,4551,1,2256,1,1,2365,1,1,6244,9307,6174,6357,1,6358,1,4933,9888,8619,1,1,7962,1,1,5672,3264,1916,2775,1,1,1,1,1,3406,2401,1,1,1,1,1,5825,6304,7463,1,1,9055,1329,5924,6988,7633,3931,1,1,469,1864,1,1,1,1,235,3396,2402,1,1,220,9849,1,9652,3623,1,8446,1,1,1,1,3176,1,1,1,1,2047,1,2145,1,1,1,1,4742,1,1,1,1,1,5756,1,4331,1,1,1,9749,248,1,5801,1,1,1,1,8303,1,1,3205,807,1,1,9408,9221,5681,1,6120,1,1,1038,1,1,586,2448,7186,1,443,1,1,1550,9798,7254,1,1,1,1,3945,1,1,9103,906,5512,1,5678,1,2029,4748,5923,1,1,220,1,1,6896,8245,1,1,8750,1,7853,1,3847,1,1,4702,1,1,1045,6894,1,117,1,8703,612,6943,1,1,1,3488,8337,1,1,2885,6472,1,1,1,1,2951,1705,4508,1,1,1,9204,2146,1,1,2044,9371,1,4406,6046,1,1,1,1,8338,1,1,1,1,3753,8007,4666,1902,1,1,2129,8229,5571,5529,1,5114,1,1,1,1,3120,1,1,1,9173,3628,1,2556,6602,6141,1,4652,871,2660,1,8440,890,877,1,1,7363,1,1,1,5139,8575,4260,1,1,1,1,8216,1,5327,6162,7100,1,9987,2813,467,5866,1,1,744,6678,2318,1,1,1,96,1,7339,1,1,1,1,4000,1,1,4425,1,1,670,8942,1,6489,4307,3815,1,1,1221,1,1,9693,6428,3274,1,1,1,1,1,6224,1,1,1,1,4480,1,9043,410,6301,7644,3099,1,1,8713,1,2312,6471,2213,99,1413,524,9893,2115,1,1,2846,3392,9946,1,1,1,1,6362,1,1,1,1,8191,3952,1,1,1,1,1,2353,1,1,1,7805,1,5566,1,6340,6000,6176,1,1,1,2812,5526,1,3787,1,1,6115,8880,1,729,1911,3889,1,1,4470,1516,3719,1,1,1234,117,1,1,1,4807,7329,1045,1,1,1,1,1,1,1,1,9548,7388,1,4848,1,7433,1,8812,1242,349,1,1,9554,1,1,1,752,7513,1,9550,1,1,5496,2265,1,1,1,1,1,1,6310,4675,5900,2288,9597,1,1,8375,8193,9987,1,5893,1,1,2616,5093,1,1,3596,4013,5408,1,1,759,1,7800,1,1588,4857,6907,1,4472,1,8476,1,7772,9456,8254,4517,437,7368,1,6884,511,1,1,1,1,9552,1,2790,6622,8361,1,5465,5295,3843,7481,1,4158,1,1,1,1,1,9111,8586,9287,1,3791,1824,5966,1,1,1,1,3746,1,43,4026,5923,1,8161,1,1509,1,1,6290,1,1,2349,7382,1889,6036,1,9777,1,1,1,1,6710,1,8288,7189,6457,987,1,1,1,43,1,1,6252,1,1891,1,5604,1601,1,9548,7278,1,9740,1,1,1,1,4781,2629,1,1,7601,1,1137,1,1,2708,1,3017,5593,1,1,2882,1,1,1,1840,599,1,6146,1,1,1,7361,1,5070,3838,1,4,9025,1,6400,9139,1,3869,1,1804,841,5466,359,4349,1,645,1,893,736,7393,3818,1435,1,1,1,9214,1,9029,437,846,1,1,9613,4297,1,1,1,6831,1,9676,1,9304,2281,2953,1,1,3123,953,4902,1,1,1,4062,1,1,2153,1,1,1615,1,1,1107,7036,1,6365,1,1,4549,1,6667,1,4348,4044,1,6295,839,2484,1,1,9136,1,1,1,1,1,1,1,5936,1,2505,1,8558,1,1,8981,1,8810,1000,2185,1,1,3715,5581,1,8261,8654,544,1,9217,8684,8826,9878,4791,1,1,1,2775,2538,6416,1,1,6823,1,9201,2920,1,3593,1,3660,7404,3350,1,9363,3777,1,1,9208,4054,1083,1,457,1,1504,1284,1,1,1,1,1,543,7330,5645,57,6236,1006,1,1,1,9551,8447,1,7767,3704,6165,1,1,3291,3636,6842,7842,1847,1,1,1,1141,1,1,1,1,5284,1,1,3461,1,1073,2438,1,1,1,1,5299,1,8623,8453,1,5758,1616,7736,1,2105,5043,9919,1,5247,7176,3947,1,1,1272,21,5612,1,1,1,1,7719,1,527,1,1,1,8929,538,1,8236,7786,8121,1,9836,1,1,1,1,1,1,8335,1,9655,7259,2630,1,1,1,1,1,426,1,1501,1,1085,1,2250,1452,241,315,7319,1,1,7263,1,278,1,1,7043,1,1,1,853,1,1,1,8082,8766,1,1864,1,1,1,9563,7385,1275,7542,1,1,1,1132,1,36,1,1,1,5972,5637,2906,1,1,1,333,5924,1,6703,1,1,1,5260,1,1013,1,1,1,1,1,9445,3648,1,4316,1,7819,1,1,6654,6659,3960,2947,6756,1,1,3450,1,6024,1,1,1,1,1,1,3863,2183,1,543,8744,274,5302,6271,1,1,1,1,9789,1,1,1,7725,1,1,586,1235,1,1,1,4845,1,1,1,6974,1,1,1,1,1,2148,8190,1,1,9087,2436,1,6518,348,1,1,1,1,1,6956,1,1,1,1,1,1,1,2202,1640,1,1,1,7294,1885,1,2191,1,6497,5377,1664,5868,1,1,4691,186,3541,3483,6932,3675,2310,8977,1,1,8751,6473,1,1,1,1904,1,1,1,6835,1,5114,8810,2599,1,868,1,1,9042,8882,8288,1,6868,1,4093,3356,1,1,1,2995,4814,1,1,6722,564,853,1,1,5378,1,3179,1,8643,5007,1,6716,1,1,1,1,6169,8021,5279,5207,6102,1,1,1,1,9303,336,1,1,1,1,2777,9240,2237,1,8397,1148,1343,150,3809,6646,2470,1,5446,6892,2064,9468,1,2012,6486,1,1,7192,4441,2519,1,7867,9748,1,7453,1,1,1,1,343,9856,8634,1,1,1,7138,1,3425,1,7654,1,1,1,1,1,9399,1,1,2448,8264,1,1,30,6497,1,1,6363,1,1,1,2676,3101,6058,75,5795,1,3610,5082,892,1904,1,1,3686,6643,9075,4483,4084,1,5957,7547,1,1,4890,1,2403,8962,4790,1,5440,7309,1689,9753,1,430,2099,1,1,1,5238,1,854,7575,3477,4183,1,1,6942,1365,1,9946,9395,6468,2251,1,5764,1,7420,1,9966,1613,67,195,7878,1511,6564,5940,1,5091,1,9250,1,5702,2468,1,1,4768,2629,1,1,6272,9915,6545,4054,3298,1,1,5748,4488,7952,2702,1384,1,1,3700,1,1,1,1,609,1,1,2142,2264,8735,1,1,1302,2457,1,8264,1,1,1,4992,1,1,1,1,1,7209,1,1,4580,4912,1,1,4727,3117,1770,1,1,1,6061,8368,1,1,4169,5146,1,7992,1,1,1,1,3268,1,1,1017,7860,207,1,1,1,1,1,911,1447,1,880,1,1,6179,8646,2305,1,1,1604,1,5527,1,1,1,1,9550,9450,1,1,1,4945,1,1,1,7197,8938,5624,6844,1,4806,374,9965,1,4388,1,1,1,2859,7940,1,1,2533,7692,1,1,6326,3164,7743,1,1,7866,7027,1,4091,1,4632,1,1,4463,1,2064,3663,1,1904,1,1,334,1,1,1,9390,1,4008,5335,1,1,2171,1,6482,9748,7169,6911,3658,1,1,1,3404,6373,4397,5819,1,7626,1,1,6977,1,9431,1,3924,4748,621,1,1,6846,9702,1,1,141,1,1,1,1,1,1,1231,1,6542,1,1,1,5653,1,1,1,1,1,10000,1,1,1,7359,1,1,1,1,3188,2079,1,1933,1,1,6273,1,2102,9237,8393,1,1,1299,1,9498,8341,1,1,1,1,8052,7343,7358,1,1,5571,1493,1,6009,1,8167,1,2523,1,1,1,6727,1,4032,1,4289,6323,1,1024,1,8826,1940,1388,1,1,1,1454,1,1,3225,1,1736,9352,8291,1979,1,1,1,1,1958,1,1,9983,1,9317,6162,1,8602,1,1,1,3992,1,4516,1,1,1,1278,1,1,1,1,7384,1,1,3043,1,9597,1,8240,5712,8828,9133,1,1,1644,2369,1,1,7484,1,1,6790,1,1,4905,1,1,1543,5139,5087,1,1,1,1,813,4475,8046,3770,1,7452,1,1,8248,1,1,1,1488,1,1,1,1,7134,3178,633,5685,1,1,1,1,8375,1,1,542,218,8241,8648,1,4847,1263,556,1,9719,23,1,9121,1,1,1,7018,9065,2922,8395,1,1,9957,9081,1,1,6071,1292,1,1484,1089,3099,8550,5067,790,1,3022,1758,4135,1,4756,4452,1,5640,1,8214,8382,5260,1,1,1,6838,7360,9636,1,1,2565,8918,1,5987,1869,1,95,4804,1,3651,8790,4559,3355,8655,5493,1705,1,1,4123,1,1,1,1,6850,1081,2325,7033,1,1,1,1,1,2273,2228,6565,2444,3825,1,4841,5689,1,1,1,1,1,6893,6036,1,7985,1,8384,3516,1,3142,2298,3659,5714,3381,3659,1,2916,9602,1,1,1630,110,7631,1193,1,1,8296,4900,8300,1,1,1,1,2137,1,198,1,6831,7316,4587,1,1,4588,1,1,1,1154,1,1,5285,1,2726,2998,1,6568,1,2361,3951,1,3591,1,6535,9934,2260,1,1,1960,4768,5585,872,2581,8819,1,1,5148,5573,9413,4953,9959,1,1,1,9318,1,1,1,163,1,6570,1,1,7576,5806,1,6057,324,1,4009,9983,1,1,893,2816,1,1,544,1,1,1,267,3744,1,8578,9575,1,1,389,5288,1,1,210,8957,1,1988,1,4792,828,1,1,1,1,1810,5178,1,7712,3936,6959,4731,7809,1,1,1,5424,8073,9,1,1,1,1,1,1,6796,1,1,5303,1,1,3966,5352,1,5091,1,1,1,2121,1,9939,1115,4014,1,2203,1,9634,1,1,1,1503,7720,1,1,1,1,1,1,7194,1,1,1,1604,1,1,1,1,1,1,1,1,5549,1,1,4160,1686,8842,1,1,4739,2094,1,1,1,1,1,6163,539,1,234,1,1,1435,1,1,4908,1,526,2320,1,1,7176,2631,1,1,1,1,672,7730,1,1,3219,1005,7563,1,1,1,1,4345,1,8243,6340,1,1,4027,1,1,1,2502,1,1,7185,1,1,1,2497,1,9376,1,717,1249,1,1,1,1,4259,1502,3637,1,1850,1,5089,5330,1,1652,999,1,1,8631,3232,1,3477,1,2001,7380,1,1,1,484,4463,1,1,6190,7084,1582,1,1,8816,683,1,1,8244,1,8775,4228,1,5920,1,1,1,4645,6454,1616,7374,920,1,1,960,1,1,132,1,1,1,1,7275,1,9289,1,2477,1711,2000,5735,9410,1,1,419,1,1,1601,2590,95,8659,1,3463,7942,8703,1,1,6473,7680,5401,8726,1,1,1,1,3003,803,1,1,1,1,8136,6027,1,1,1,1,1,1,1,6140,1,4715,1,1,1,1,1925,8892,1,1,1,8100,1,1,1,4105,1,7975,1,1,1,1,1923,4948,1,8530,3101,1,3061,3652,1,1,1,1199,1243,1,9161,4128,1,1,1,1,3567,9028,4126,1,2590,1,3116,1,1,6013,1,1,1,1,9966,1,1,62,1,1,2875,1,6162,1,1,1,2198,1,9752,5241,1,2200,1,1,2704,1,1,1,1,3122,1,2623,6925,1,1,1,1,1,1,1,1,5981,1,1,1,1,1,668,1,2532,1656,2995,1,1,7008,2305,8974,1,577,5802,1,1,7969,6456,1,1,1,1,5963,1,9970,1,5975,6115,1,9336,8527,1,1,1,1,1,1,1,1,1,1,1,9855,7282,1,1,1,1,8836,6194,1,1,1,9381,1,1,1015,9942,1,1,867,5386,303,1,8806,9715,6418,8421,1,7411,869,7945,1,7038,1,5497,1,1,1,1,6427,9328,1,1,126,2876,1,735,1,1,2177,936,1,1,5027,1,3909,1,8732,4657,2416,1,9011,1,1,5658,3654,1,3295,1,8435,4185,3060,3171,1,1,4000,1,1294,1,1,9256,3995,2121,1,1,1,6767,4897,4682,1,1451,5627,1,1,1,1,1,1,1,1523,5315,1,3235,1,1216,4384,5351,1,1332,1,1635,1,4867,8430,1,6743,3556,882,1,1,9957,1,1,190,1,1617,1,4577,1,5762,6560,6298,1641,1,9260,2172,655,1,6451,1,1,1,1258,1,1,9621,468,5586,7305,1,1,190,1,1,1,3805,2415,4435,5827,1,5213,1,222,1,2723,5468,7630,1,1,5147,1,1,1,2670,1,1,4087,1,1,6930,7763,1,1,8317,1,1,1,1,1,7319,1,1,1,3549,1,518,6829,7,1,1,5135,1,1,1,1287,1,1,3209,84,1,7561,1,7795,632,5208,7828,8810,2045,1,1,3923,4215,1,1,1,5330,1821,5913,1,1,8479,1,3576,1,7619,1,5189,8106,1,8167,1,1,1,3379,1789,1,5316,7049,3809,1,894,1,4820,3113,5351,3352,6974,1,8287,1,375,1,750,186,1,1,1679,5174,1,1,1,1,9924,1,1,1,9219,1126,3013,1,1,1,1,1,1,7012,1,1,9396,8799,1,3301,1238,8785,4370,1,6743,1,1,8953,1,1,762,1041,1840,1432,1441,1,4830,7010,4500,9312,1,1,2353,6374,5067,105,1,862,2460,1,8000,7162,6997,7211,1,1,1,1,8075,3463,2903,2862,8141,4677,1,1,2719,1305,1,1,9138,1,9889,9479,1,7848,1,4341,1,7388,1,2335,9521,4919,3266,1,1,8009,5529,4809,3420,1,6289,7525,1,1,4202,1,1,270,75,7915,1,9030,1,5080,1,6198,3649,1,1,1,7966,86,7959,1,1,1,1,1,3495,8476,213,8772,1,3356,53,9713,1,2629,2048,1,1,1,1453,1,1,6859,1,1,283,6397,7703,1,177,5724,1,1,1,395,1,9142,1,287,1,1,1,6403,3701,765,1,1,1,9167,1498,4165,1,1,2367,1,1,3594,1,1,1,1,2727,1,3024,9679,881,1,1,1,1,3114,1,1,1,1,1,1,1,7909,1,831,1,1,1,9036,1,1,1629,6942,3415,1,9323,105,1,6900,1,6948,1,1,1515,1,8937,1134,9719,1,9695,9421,1,266,4046,4866,439,1,1,1,1,1,6012,1,1,1,713,1,4139,1,4088,805,1,2015,1,1,1,1,7396,1,1,1,1,1,6770,8153,3958,1,1,2868,693,1,1,1,1,4885,3394,3739,4028,3280,1,107,1,1,1,1,6398,7245,1,1,1,842,1,1,6410,7996,6980,9558,1,6882,4411,6977,1,5710,9387,2677,1,1,9966,1,5823,1,1,1865,8894,3661,1,5026,1,918,2709,1,7478,5344,1,9525,8950,1,1,9048,7221,1,1,2373,1,1,1,1,1,7734,180,1,6775,2581,1,1,1,1,1,1421,2077,700,6913,2863,3836,445,5444,1,8344,1,1,7929,4658,1,1,4691,1,1,5975,1,2812,3000,1,1,8772,117,1,4451,7248,9573,5015,1,1,642,1,7414,9345,1,1,1,2436,4303,9328,1,1,3336,1,2353,1,7214,1045,1,341,1,1,9639,223,931,2581,1,1,1,1,6308,1,1,6706,1,1,5431,1,609,7645,1,7333,1407,1,3694,1834,4447,1973,6304,3822,8375,1,1,1,1,1,1,5103,4303,845,1,5662,1,1,1,1,1,1976,1,4323,7836,1,4918,1,1,1,1,1432,1,2889,8686,1,1,9748,1,1,1,6413,1,6574,5081,1,1,5223,6230,4044,1,1,1,1287,1,6688,1,1,1,1,1,1,1,1,8187,3148,4966,2720,1,1,1,1,1,1717,9147,1,1929,8864,1,2509,4070,1,3693,4981,2107,1,4769,4283,6431,1,1,1491,1,1,9226,7810,2402,920,9173,1,660,1,1,1,2289,673,4694,6524,1,1120,1887,9237,1,4507,3541,1,1,5292,6150,5479,9895,4020,1,1,1,4429,1,1,1,5798,1,1,6186,6939,2476,851,1,1,8195,1,1,6710,66,1,7857,9405,7005,1840,2254,1,1,1,4483,1,1,238,5312,1,9828,2565,1,1,1,1,6039,9318,5226,1843,8650,822,1,1,2177,2448,9726,8954,5353,7878,1,519,76,9239,1,6547,1,4845,4509,20,1,1,1,1,1,9992,1,9922,3182,7635,9432,7003,6839,1,1,3255,5257,1193,8986,1,3279,4165,1,1,1,6302,9791,5695,1,1,1,1,1,1,429,486,1,1,9228,3171,1,2634,1,2033,1659,8306,1,1,8182,1,7618,1,761,9766,761,4328,1,1,4748,1,1,6795,15,1,1,1,6285,2217,1,1,1,2673,1,4141,1,1,755,1,5383,1,1,1,1,7272,1,1,7550,1,1,1,1,6913,1,1,1,5025,8228,341,5518,3339,7135,7607,8028,1,1,1,7669,7062,730,1,1,3200,1,2516,3117,6683,6477,1,2653,3648,1,183,6495,1,2421,93,1,4548,1921,6723,1,2198,1688,1,290,1,1,1,4054,1,1,1,1,1,1,7769,6435,9352,1,7233,1,7635,8384,1,5590,1,4729,1,1,1045,1,1,7455,1,9306,4840,3948,9970,4527,8239,4478,1,1,6048,1,1838,1,2529,1,7491,1]))
