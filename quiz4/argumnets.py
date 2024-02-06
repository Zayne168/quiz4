import argparse

def demo() -> None: 	
    parser=argparse.ArgumentParser() 	
    parser.add_argument(help='String: ',dest='mySTR',type=str)         	
    parser.add_argument(help='Integer: ',dest='myINT',type=int)   
    parser.add_argument(help='Float: ',dest='myFLOAT',type=float) 

    args = parser.parse_args()  	

    stringOne=args.mySTR 	
    integerOne=args.myINT
    floatOne=args.myFLOAT  	

    print("string: ",stringOne) 	
    print("Integer: ",integerOne)
    print("Float: ",floatOne)
