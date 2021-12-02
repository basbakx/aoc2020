int result = 0;
void setup() {
 String[] low = loadStrings("1.txt");
 String[] high = loadStrings("2.txt");
 String[] rule = loadStrings("3.txt");
 String[] password = loadStrings("4.txt");
 
 
 for (int i = 0; i < password.length; i++) {
   String str = password[i];
   char ch =  char(rule[i].charAt(0));
   int count = 0;
   
   if(str.charAt(int(low[i]) - 1) == rule[i].charAt(0) ){
     count++;
   }
   if(str.charAt(int(high[i])- 1) == rule[i].charAt(0) ){
     count++;
   }
   if(count == 1){
     result++;
   }
  
 }
 println(result);
}