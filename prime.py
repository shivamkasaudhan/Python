#  bool is_Prime(int n){
#       if(n <= 1) return false;
#       for (int i = 2; i * i <= n; i++){
#         if (n % i == 0)return false;
#       }
#       return true;
#     }

a = input("a: ")
if(a<=1):
    print(False)
for i in range(a**0.5):
    if(a&i==0):
        print(False)
print(True)