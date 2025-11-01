import argparse

parser = argparse.ArgumentParser(description = "simple calculator")

parser.add_argument("num1",type=int,help="First Number")
parser.add_argument("operator",choices=["+","-","*","/"],help="Operator to perform")
parser.add_argument("num2",type=int,help="Second Number")

args = parser.parse_args()

if args.operator == "+":
    print(args.num1 + args.num2)

elif args.operator == "-":
    print(args.num1 - args.num2)

elif args.operator == "*":
    print(args.num1 * args.num2)

elif args.operator == "/":
    print(args.num1 / args.num2)
    
else:
    print("Error!")